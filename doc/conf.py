# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

topdir = os.path.split(os.path.split(__file__)[0])[0]
serverdir = os.path.join(topdir, "src/server")
#serverUtildir = os.path.join(serverdir, "util")
sys.path.insert(0, serverdir)
#sys.path.insert(0, serverUtildir)

import server

project = 'RotorHazard'
copyright = '2024, Michael Niggel and other contributors'
author = 'RotorHazard Development Team'
version = '1'
release = server.RELEASE_VERSION

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_material'
html_static_path = ['_static']
html_logo =  '../main/src/server/static/image/RotorHazard Logo.svg'

html_theme_options = {
    'color_primary': 'orange',

    'repo_url': 'https://github.com/RotorHazard/RotorHazard',
    'repo_name': 'RotorHazard',
    'repo_type': 'github',

    'globaltoc_depth': 2,
    'globaltoc_collapse': True,
}