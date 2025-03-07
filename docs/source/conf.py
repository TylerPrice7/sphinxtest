# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import sys
import os
from pathlib import Path
# Get the root directory of your Sphinx project
docs_root = Path(__file__).resolve().parents[2]  # Adjust if necessary

# Find all subdirectories that contain Python files
for py_dir in docs_root.rglob("*"):
    if py_dir.is_dir() and any(f.suffix == ".py" for f in py_dir.iterdir()):
        sys.path.insert(0, str(py_dir))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'CCC'
copyright = '2025, Tyler'
author = 'Tyler'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.builders',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'furo'
html_static_path = ['_static']
html_css_files = ['custom.css']