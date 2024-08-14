# -- Project information -----------------------------------------------------

project = 'TIAM-FR'
copyright = '2024, Centre for Applied Mathematics of Mines Paris - PSL'
author = 'Author One, Author Two, Author Three'
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'myst_parser',
    'sphinx.ext.mathjax',
    'sphinx.ext.imgmath'
    # Other Sphinx extensions
]

myst_enable_extensions = [
    "amsmath",      # Allows LaTeX math
    "dollarmath",   # Enables $...$ and $$...$$ syntax
    "colon_fence",  # Enables ::: for block content
]

# Optional: Configure the path to MathJax (not always needed, default usually works)
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
#mathjax_path = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/MathJax.js?config=TeX-AMS-MML_HTMLorMML'


templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for LaTeX output ------------------------------------------------

latex_engine = 'pdflatex'  # or 'xelatex' or 'lualatex', depending on your needs

latex_elements = {
    'papersize': 'a4paper',  # Options: 'a4paper', 'letterpaper'
    'pointsize': '10pt',     # Options: '10pt', '11pt', '12pt'
    'preamble': r'''
        % Custom LaTeX commands can go here
        \usepackage{amsmath,amsfonts,amssymb,amsthm}  % For math symbols
        \usepackage{graphicx}  % For including graphics
        \usepackage{hyperref}  % For clickable links in the PDF
    ''',
    'figure_align': 'htbp',  # Positioning of figures
    # Additional settings:
    # 'extraclassoptions': 'openany',  # Remove blank pages between chapters
    # 'fncychap': '\\usepackage[Bjarne]{fncychap}',  # Custom chapter styling
}

# Grouping the document tree into LaTeX files. List of tuples.
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'TIAM-FR.tex', 'TIAM-FR Documentation',
     'Author One, Author Two, Author Three', 'manual'),
]

# Other LaTeX settings
latex_show_urls = 'footnote'  # How to display URLs: 'no', 'footnote', 'inline'
