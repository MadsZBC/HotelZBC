# Configuration file for the Sphinx documentation builder

# -- Project information -----------------------------------------------------
project = 'ZBC Hotels'
copyright = '2024, ZBC Hotels'
author = 'ZBC Hotels'
release = '0.1.0'
version = '0.1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',  # Include documentation from docstrings
    'sphinx.ext.napoleon', # Support for NumPy and Google style docstrings
    'sphinx.ext.viewcode', # Add links to source code
]

# Add any paths that contain templates here, relative to this directory
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'  # Read the Docs theme
html_static_path = ['_static']