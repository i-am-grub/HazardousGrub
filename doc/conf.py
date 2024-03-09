# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

topdir = os.path.split(os.path.split(__file__)[0])[0]
serverDir = os.path.join(topdir, 'src/server')
utilDir =os.path.join(serverDir, 'util')
interfaceDir = os.path.join(topdir, 'src/interface')
sys.path.insert(0, serverDir)
sys.path.insert(0, utilDir)
sys.path.insert(0, interfaceDir)

import server

project = 'RotorHazard'
copyright = '2024, Michael Niggel and other contributors'
author = 'RotorHazard Development Team'
release = server.RELEASE_VERSION
version = release.split("-")[0]

rst_prolog = f"""
.. |project_release| replace:: {release}
"""

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_material'
html_static_path = ['_static']
html_logo =  os.path.join(serverDir, 'static/image/RotorHazard Logo.svg')

html_theme_options = {
    'nav_title': 'RotorHazard',
    'color_primary': 'orange',

    'repo_url': 'https://github.com/RotorHazard/RotorHazard',
    'repo_name': 'RotorHazard',
    'repo_type': 'github',

    'globaltoc_depth': 2,
    'globaltoc_collapse': True,
}

html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "searchbox.html"]
}

extensions = ['sphinx_material',
              'sphinx.ext.autosectionlabel',
              'sphinx_substitution_extensions',
              'sphinx_copybutton'
              ]