# demonstrating-the-theory

A collection of demonstrations

## Usage

### Building the book

The local version, which is pushed to GitLab can be found in:
C:\Users\rhaaksman\demolab
If you'd like to develop and/or build the demonstrating-the-theory book, you should:

1. Clone this repository
2. Run `pip install -r requirements.txt` (it is recommended you do this within a virtual environment)
3. (Optional) Edit the books source files located in the `demonstrating-the-theory/` directory
4. Run `jupyter-book clean demonstrating-the-theory/` to remove any existing builds
5. Run `jupyter-book build demonstrating-the-theory/`

A fully-rendered HTML version of the book will be built in `demonstrating-the-theory/_build/html/`.

Use Anaconda prompt, and activate the 'demolab' environment to build the book
Run from within the book folder:
<jb build --all .>
To clean the book:
<jb clean .>
Within MS Visual Studio Code:
<description><commit>
And:
<Sync Changes>

### Hosting the book

Please see the [Jupyter Book documentation](https://jupyterbook.org/publish/web.html) to discover options for deploying a book online using services such as GitHub, GitLab, or Netlify.

For GitHub and GitLab deployment specifically, the [cookiecutter-jupyter-book](https://github.com/executablebooks/cookiecutter-jupyter-book) includes templates for, and information about, optional continuous integration (CI) workflow files to help easily and automatically deploy books online with GitHub or GitLab. For example, if you chose `github` for the `include_ci` cookiecutter option, your book template was created with a GitHub actions workflow file that, once pushed to GitHub, automatically renders and pushes your book to the `gh-pages` branch of your repo and hosts it on GitHub Pages when a push or pull request is made to the main branch.

## Issues

https://github.com/executablebooks/jupyter-book/issues/1991
https://myst-nb.readthedocs.io/en/latest/render/interactive.html#ipywidgets

https://myst-nb.readthedocs.io/en/latest/render/interactive.html#ipywidgets
Widgets often need a kernel

Note that ipywidgets tend to behave differently from other interactive viz libraries. They interact both with Javascript, and with Python. Some functionality in ipywidgets may not work in rendered pages (because no Python kernel is running). You may be able to get around this with tools for remote kernels, like thebelab.

IMPORTANT!!!!!!!!!!!!

I discovered that the culprit was parse: myst_enable_extensions: ipywidgets in the _config.yml file. If the ipywidgets extension was enabled, it would screw up some parts of the book, such as equations, and makeup such as pictures, contents, index, bibliography etc.

If i disabled the ipywidgets extension the book renders properly.

https://myst-nb.readthedocs.io/en/latest/render/interactive.html#ipywidgets

Note ipywidgets does not seem to work for e.g. interactive plots, instead use bokeh
Note that if you place two pieces of python bokeh code (for e.g. two individual interactive plots), only the last piece of code compiles correctly
This was solved by placing notebook_output() at the beginning of each piece of code

## Contributors

We welcome and recognize all contributions. You can see a list of current contributors in the [contributors tab](https://github.com/classroom-demonstrations/demonstrating-the-theory/graphs/contributors).

## Credits

This project is created using the excellent open source [Jupyter Book project](https://jupyterbook.org/) and the [executablebooks/cookiecutter-jupyter-book template](https://github.com/executablebooks/cookiecutter-jupyter-book).

# https://mstruwig.com/posts/jupyterbook-video/
