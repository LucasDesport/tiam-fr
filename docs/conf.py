# -- Project information --

project = 'TIAM-FR'
copyright = '2024, Centre for Applied Mathematics of Mines Paris - PSL'
author = 'L. Desport, S. Chlela, M. Codet, C. Barnet, S. Selosse'
release = '1.0'

# -- General configuration --

extensions = [
    'myst_parser',
    'sphinx.ext.mathjax',
    'sphinx.ext.imgmath',
    'rst2pdf.pdfbuilder',
]

myst_enable_extensions = ["colon_fence", "linkify", "dollarmath", "amsmath"]

# MathJax configuration (optional)
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
mathjax_config = {
    "tex2jax": {
        "inlineMath": [ ["$", "$"], ["\\(", "\\)"] ],
        "displayMath": [ ["$$", "$$"], ["\\[", "\\]"] ],
        "processEscapes": True,
    },
    "TeX": {
        "equationNumbers": { "autoNumber": "AMS" }
    }
}

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML output options --

html_theme = 'alabaster'
html_static_path = ['_static']

# -- LaTeX output options --

latex_engine = 'pdflatex'

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'preamble': r'''
        % Custom LaTeX commands
        \usepackage{amsmath,amsfonts,amssymb,amsthm}  % Math symbols
        \usepackage{graphicx}  % Graphics
        \usepackage{hyperref}  % Hyperlinks in PDF
    ''',
    'figure_align': 'htbp',
    # Ensure blank pages are added if needed to start each chapter on a new page
    'extraclassoptions': '',  # Leave this blank or omit to allow normal chapter-start behavior
}

# LaTeX document settings
latex_documents = [
    ('index', 'TIAM-FR.tex', 'TIAM-FR Documentation',
     'Lucas Desport, Sophie Chlela, Marie Codet, Charlène Barnet, Sandrine Selosse', 'manual'),
]

# Source file suffixes
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# PDF output options
pdf_documents = [('index', 'MyProject', 'My Project Documentation', 'Author Name')]

# Display URLs as footnotes in LaTeX output
latex_show_urls = 'footnote'
