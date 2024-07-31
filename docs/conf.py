# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'TIAM-FR'
copyright = '2024, Centre for Applied Mathematics of Mines Paris - PSL'
author = 'Author One, Author Two, Author Three'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# Import necessary modules
from recommonmark.parser import CommonMarkParser

extensions = [
    'myst_parser',
    'rst2pdf.pdfbuilder',
    # other extensions if any
    'recommonmark',
    'sphinx_markdown_tables',
]

# Set the source suffix for Markdown files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Set the master doc (usually index)
master_doc = 'index'

# List of patterns, relative to source directory, that match files and directories to ignore when looking for source files.
exclude_patterns = []

# Set the source parser for Markdown
source_parsers = {
    '.md': CommonMarkParser,
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for MyST-Parser -------------------------------------------------
# https://myst-parser.readthedocs.io/en/latest/syntax/optional.html

myst_enable_extensions = ["dollarmath"]

# -- Options for rst2pdf -----------------------------------------------------
pdf_documents = [
    ('index', 'TIAM-FR', 'TIAM-FR Documentation', 'Author One, Author Two, Author Three'),
]
