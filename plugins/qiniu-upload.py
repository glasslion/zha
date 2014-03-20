import os

from sevencow import Cow

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ACCESS_KEY = os.environ['QINIU_ACCESS_KEY']
SECRET_KEY = os.environ['QINIU_SECRET_KEY']
BUCKET = os.environ['QINIU_BUCKET']

cow = Cow(ACCESS_KEY, SECRET_KEY)
bucket = cow.get_bucket(BUCKET)

def upload_theme_assets(parent_path='output'):
    abs_path = os.path.join(BASE_DIR, parent_path, 'theme')
    asset_paths = []
    for root, dirs, files in os.walk(abs_path):
        files[:] = [f for f in files if not f[0] == '.']
        dirs[:] = [d for d in dirs if not d[0] == '.']
        for filename in files:
            filepath = os.path.join(root, filename)
            asset_paths.append(filepath)
    abs_parent_path = os.path.join(BASE_DIR, parent_path, '')
    names = { path:path.replace(abs_parent_path, '') for path in asset_paths }
    bucket.put(*asset_paths, names=names)


def clear_remote_theme_assets():
    file_stats = bucket.list_files(prefix='theme')
    file_keys = [ item['key'] for item in file_stats['items'] ]
    bucket.delete(file_keys)


def main():
    clear_remote_theme_assets()
    upload_theme_assets()


if __name__ == '__main__':
    main()

