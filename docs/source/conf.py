# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FixedIncome2025'
copyright = '2025, Prof. Scott Chiu, Rutgers Business School'
author = 'Prof. Scott Chiu, Rutgers Business School'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [  'nbsphinx', 
                'sphinx.ext.autodoc', 
                'sphinx.ext.napoleon',
                'sphinx.ext.mathjax', 
                'sphinx.ext.viewcode', 
                'sphinx_copybutton', 
                'sphinx_rtd_dark_mode'   # for sphinx_rtd_theme only
             ]

default_dark_mode = False

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import sphinx_rtd_theme             # if this is commented out, the sphinx_rtd_dark_mode extension will have to be commented out as well
html_theme = "sphinx_rtd_theme"

# html_theme = 'alabaster'
html_static_path = ['_static']

master_doc = 'index'
nbsphinx_allow_errors = True
nbsphinx_execute = 'never'

# Show "View on GitHub" / "Edit on GitHub" links (sphinx_rtd_theme)
html_show_sourcelink = True
html_context = {
   'display_github': True,
   'github_user': 'ScottChiuNYC',
   'github_repo': 'FixedIncome2025',
   'github_version': 'master',
   # path to the docs root in the repo, with leading & trailing slashes
   'conf_py_path': '/docs/source/',
}
