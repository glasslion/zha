The Makefile and .travis.yml are good references that help you understand how to deploy this blog system.

To reduce the complexities, statics like sass should be precompiled and stored in the theme directory. Thus themes should have their own documentions about installation and build process.


## Build THE SITE

```bash
git clone https://github.com/glasslion/zha.git

# checkout theme
git clone https://github.com/glasslion/pelican-zha.git

cd zha

# checkout plugin
git clone https://github.com/getpelican/pelican-plugins.git official_plugins

# Install packages
mkvirtualenv zha
pip install -r requirements.txt

# build
make regenerate

make server

```

## QINIU CDN

Qiniu is used to host theme statics.

Usage:
```bash
cd zha/plugins

# Define these environment variables: ACCESS_KEY, SECRET_KEY, BUCKET
python qiniu-upload.py

```
