############################################################
# -*- coding: utf-8 -*-
#
#  o-o   o--o  o   o  o-o
#  |  \  |   | |   | |
#  |   O O--o  |   |  o-o
#  |  /  |   | |   |     |
#  o-o   o--o   o-o  o--o
#
#
#   o-o  o--o o--o  o     o-o   o-o
#  |     |    |   | |    o   o |
#   o-o  O-o  O--o  |    |   |  o-o
#      | |    |     |    o   o     |
#  o--o  o--o o     O---o o-o  o--o
#
# python-based service for victron cerbo > v3.00
#
# (c) 2024 by mworion
# Licence MIT
#
###########################################################

# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'dbus-seplos'
copyright = '2024, mworion'
author = 'Michael Würtenberger'

# The full version, including alpha/beta/rc tags
version = '0.0.3'
release = '0.0.3'
master_doc = 'index'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['rst2pdf.pdfbuilder', 'sphinx.ext.autosectionlabel',
              'sphinx.ext.githubpages']

# drawio_binary_path = '/Applications/draw.io.app/Contents/MacOS/draw.io'
# diagrams_exporter_path = './'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

pdf_documents = [('index', u'dbus-seplos', u'dbus-seplos', u'mworion')]
# index - master document
# rst2pdf - name of the generated pdf
# Sample rst2pdf doc - title of the pdf
# Your Name - author name in the pdf

html_theme_options = {
    'logo': 'mw.png',
    'logo_name': True,
    'fixed_sidebar': True,
    'page_width': '1400px',
    'sidebar_width': '300px',
    'base_bg': '#FFFFFFFF',
    'base_text': '#FFFFFFFF',
    'body_bg': '#FFFFFFFF',
}

latex_logo = '_static/mw.png'
latex_show_urls = 'inline'
latex_show_pagerefs = True
latex_elements = {
    'papersize': 'a4paper',
}
