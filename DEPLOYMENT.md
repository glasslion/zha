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


## travis
Inspired by [Publish your Pelican blog on Github pages via Travis-CI](http://blog.mathieu-leplatre.info/publish-your-pelican-blog-on-github-pages-via-travis-ci.html), I use travis to auto publish this blog.

To avoid accidental changes, changes made outside the mster branch, is published to [zha-beta](https://github.com/glasslion/zha-beta) repo.
After ckecking http://glasslion.github.io/zha-beta/, we then merge changes into the master branch and publish to the real site.


*What's inside secure?*

For now, there's only a github token, used to push compiled htmls to Github repo's gh-pages branch, token name is `zha_travis_auto_publish`.
To generate secure: `travis encrypt GH_TOKEN=xxxx --add`
