# conf.py

# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('../../'))

# -- Project information -----------------------------------------------------

project = 'AINewsTracker'
copyright = '2023, Antoine Boucher, Mohamed Ilias, Makhlouf Hennine'
author = 'Antoine Boucher, Mohamed Ilias, Makhlouf Hennine'

# The full version, including alpha/beta/rc tags
release = '0.1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
]

templates_path = ['_templates']

source_suffix = '.rst'
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'

html_static_path = ['_static']

# If false, no module index is generated.
html_domain_indices = False
