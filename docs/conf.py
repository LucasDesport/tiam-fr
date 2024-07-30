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

extensions = [
    'myst_parser',
    'rst2pdf.pdfbuilder',
    # other extensions if any
]

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
