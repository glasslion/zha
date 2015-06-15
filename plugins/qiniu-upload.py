import os
import sys

import qiniu

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ACCESS_KEY = os.environ['QINIU_ACCESS_KEY']
SECRET_KEY = os.environ['QINIU_SECRET_KEY']
BUCKET = os.environ['QINIU_BUCKET']

auth = qiniu.Auth(ACCESS_KEY, SECRET_KEY)
token = auth.upload_token(BUCKET)
bucket = qiniu.BucketManager(auth)


def upload_theme_assets(parent_path='output'):
    abs_path = os.path.join(BASE_DIR, parent_path, 'theme')
    abs_parent_path = os.path.join(BASE_DIR, parent_path, '')
    asset_paths = []
    for root, dirs, files in os.walk(abs_path):
        files[:] = [f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        for filename in files:
            if filename.endswith('scss'):
                continue
            file_path = os.path.join(root, filename)
            remote_path= file_path.replace(abs_parent_path, '')
            ret, info = qiniu.put_file(token, key=remote_path, file_path=file_path)
            if not ret:
                print info
                sys.exit()


def clear_remote_theme_assets():
    ret, eof, info = bucket.list(BUCKET, prefix="theme", limit=100)
    file_list = ret['items']
    for fil in file_list:
        ret, info = bucket.delete(BUCKET, fil['key'])
        if not ret:
            print info
            sys.exit()


def main():
    clear_remote_theme_assets()
    upload_theme_assets()



if __name__ == '__main__':
    main()

