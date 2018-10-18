#!/bin/sh

source activate jupyter_blog_env
cd /Users/danielborcherding/Documents/Studium/DataScience/jupyter-blog
pelican content
cd output
python -m pelican.server