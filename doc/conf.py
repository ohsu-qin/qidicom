import os
import qidicom

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'sphinx.ext.todo']
autoclass_content = "both"
source_suffix = '.rst'
master_doc = 'index'
project = u'qidicom'
copyright = u'2014, OHSU Knight Cancer Institute'
version = qidicom.__version__
pygments_style = 'sphinx'
htmlhelp_basename = 'qidicomdoc'
html_title = "qidicom v%s" % version
