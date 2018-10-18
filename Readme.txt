Readme for blog posts!

Interesting themes
storm
Casper2Pelican
pelican-fh5co-marble

1.) source activate jupyter_blog_env
2.) cd /Users/danielborcherding/Documents/Studium/DataScience/jupyter-blog
3.) To add new post: put jupyter notebook into content and create .ipynb-meta file. Insert information as before
4.) pelican content
5.) cd into output
6.) python -m pelican.server ----> localhost:8000 shows website in the browser



How to write a script

1.) write: #!/bin/sh
2.) save it as file.command
3.) run in terminal: chmod +x file.command

Install package commands

To install a specific package such as SciPy into an existing environment:
	conda install --name myenv scipy=0.15.0

To create an environment
	conda create --name myenv

To create an environment with a specific version of Python
	conda create -n myenv python=3.4

To activate an environment
	source activate myenv

To use pip in an environment
	conda install -n myenv pip
	source activate myenv
	pip <pip_subcommands>

To show all packages of current environment
	conda list