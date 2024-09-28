# -- Path setup --------------------------------------------------------------
from os.path import abspath, dirname
here = abspath(dirname(__file__))
# -- Project information -----------------------------------------------------
project = 'Downwind Core'
copyright = '2024, Guto Maia'
author = 'Gustavo Maia Neto (Guto Maia)'
from dw_core import __version__
release = __version__
# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx_autodoc_typehints',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
    'sphinxcontrib.plantuml',
    'sphinx_multiversion',
]
plantuml = f'java -jar {here}/plantuml.jar'
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
# -- Versioning --------------------------------------------------------------
smv_tag_whitelist = r'^v\d+\.\d+.\d+.*$'
smv_branch_whitelist = r'^(\d+\.\d+\.x)|(feat/.*)|(fix/.*)$'
smv_remote_whitelist = None
smv_released_pattern = r'^tags/.*$'
smv_outputdir_format = '{ref.name}'
smv_prefer_remote_refs = False
smv_latest_version = f'v{release}'
