# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import server

project = 'RotorHazard'
copyright = '2024, Michael Niggel and other contributors'
author = 'RotorHazard Development Team'
release = server.RELEASE_VERSION
version = release.split("-")[0]

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_material'
html_static_path = ['_static']
html_logo =  'static/image/RotorHazard Logo.svg'

html_theme_options = {
    'color_primary': 'orange',

    'repo_url': 'https://github.com/RotorHazard/RotorHazard',
    'repo_name': 'RotorHazard',
    'repo_type': 'github',

    'globaltoc_depth': 2,
    'globaltoc_collapse': True,
}