# -*- coding: utf-8 -*-
#
# em documentation build configuration file, created by
# sphinx-quickstart on Mon Sep 21 23:09:24 2015.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
from flask import request
# import em_examples

sys.path.append(os.path.abspath('./_ext'))
# sys.path.append(os.path.abspath('./em_notebooks'))


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinxcontrib.bibtex',
    'matplotlib.sphinxext.plot_directive',
    'edit_on_github',
    'purpose',
    'question',
    'geosciapp',
    # 'sphinx_nbexamples'
    # 'sphinx_gallery.gen_gallery',
]

bibtex_bibfiles = ['./content/references.bib']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = ['.rst']

# sphinx_gallery_conf = {
#     # path to your examples scripts
#     'examples_dirs' : 'em_notebooks',
#     # path where to save gallery generated examples
#     'gallery_dirs'  : 'auto_examples'}


    # Sphinx Gallery
sphinx_gallery_conf = {
    # path to your examples scripts
    'examples_dirs' : '../../simpeg/em_notebooks',
    'gallery_dirs'  : 'auto_examples'
}


# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'em'
# copyright = """
# <div>
# <a rel="license" href="http://creativecommons.org/licenses/by/4.0/" style="float:right;height:3em;line-height:3em;padding:10px 0 0 1em;">
# <img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" />
# </a>
# 2015-2016, <a href="http://em.geosci.xyz/contributors">em.geosci.xyz Developers.</a><br />
# Except where noted, this work is licensed under a <br />
# <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>

# """
author = u'GeoSci Developers'


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.0.5'
# The full version, including alpha/beta/rc tags.
release = '0.0.5'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = [
    '_build', 'AUTHORS.rst', 'README.md', '.ipynb_checkpoints', 'lib/*.rst',
    'content/equation_bank/*',
    'content/maxwell1_fundamentals/maxwell_variables.rst',
    'error.rst',
    'content/geophysical_surveys/airborne_fdem/transmitters_and_receivers.rst',
    'content/geophysical_surveys/airborne_fdem/systems.rst',
    'content/geophysical_surveys/airborne_tdem/systems.rst',
    'content/case_histories/case_histories.rst'
                    ]

linkcheck_ignore = [
    'http://www.austhaigeophysics.com/A%20Comparison%20of%202D%20and%203D%20IP%20from%20Copper%20Hill%20NSW%20-%20Extended%20Abstract.pdf',
    'http://scitation.aip.org/content/aip/journal/jcp/9/4/10.1063/1.1750906',
    'http://www.ga.gov.au/metadata-gateway/metadata/record/gcat_aac46307-fce8-449d-e044-00144fdd4fa6/',
    'https://linkedin.com/in/*',
    'http://dx.doi.org/10.1071/EG08027',
    'http://www.publish.csiro.au/paper/PVv2010n149p23',
    'http://www.zenyatta.ca',
    'https://gif.eos.ubc.ca/sites/default/files/Yang16.pdf',
    'https://www.google.ca/url?sa=t&rct=j&q=&esrc=s&source=web&cd=2&ved=0ahUKEwjy65rOo8fRAhVJ1WMKHYO7CJAQFggkMAE&url=http%3A%2F%2Fwww.dmec.ca%2FDMEC%2Fmedia%2FDocuments%2FLalor%2520Symposium%2FLalor_Symposium_Oct-2014_Handout.pdf&usg=AFQjCNHYYoQbCDs7vftzMyfuY28XUkTItQ&sig2=KDwe8n7CRvmEvAOAcKh5Zg&cad=rja',
    'https://gif.eos.ubc.ca/sites/default/files/McMillan_parametric.pdf',
    'http://seg.org',
    'http://library.seg.org/doi/',
    'http://www.publish.csiro.au/EX/pdf/ASEG2016ab212',
    'https://notebooks.azure.com/import/gh/geoscixyz/em-apps',
    'https://notebooks.azure.com/import/gh/simpeg/em-notebooks',
    'https://www.onepetro.org/conference-paper/SEG-2012-1478',
    'https://doi.org/*',
    'http://canada.debeersgroup.com/* ',
                    ]
linkcheck_retries = 3
linkcheck_timeout = 900

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# number figures
numfig = True

# -- Edit on Github Extension ---------------------------------------------

edit_on_github_project = 'geoscixyz/em'
edit_on_github_branch = 'main'
check_meta = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

# on_rtd is whether we are on readthedocs.org
import os
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# Theme options are theme-specific and customize the look and feel of a
# theme further.
# html_theme_options = {
#     # Navigation bar title. (Default: ``project`` value)
#     'navbar_title': "EM.geosci",

#     # Tab name for entire site. (Default: "Site")
#     'navbar_site_name': "Contents",

#     # A list of tuples containing pages or urls to link to.
#     # Valid tuples should be in the following forms:
#     #    (name, page)                 # a link to a page
#     #    (name, "/aa/bb", 1)          # a link to an arbitrary relative url
#     #    (name, "http://example.com", True) # arbitrary absolute url
#     # Note the "1" or "True" value above as the third argument to indicate
#     # an arbitrary url.
#     'navbar_links': [
#           # ('<i class="fa fa-home" aria-hidden="true"></i>', "http://geosci.xyz", '1'),
#           ('Why', 'content/introduction/introduction_about'),
#           ('Who', 'contributors'),
#           # ("Maxwell", "maxwell1_fundamentals/index"),
#           # ("Static", "maxwell2_dc"),
#           # ("FDEM", "maxwell3_fdem"),
#           # ("TDEM", "maxwell4_tdem"),
#           # ("Surveys", "geophysical_surveys"),
#     ],

#     # Render the next and previous page links in navbar. (Default: true)
#     'navbar_sidebarrel': True,

#     # Render the current pages TOC in the navbar. (Default: true)
#     'navbar_pagenav': False,

#     # Tab name for the current pages TOC. (Default: "Page")
#     'navbar_pagenav_name': "Page",

#     # Global TOC depth for "site" navbar tab. (Default: 1)
#     # Switching to -1 shows all levels.
#     'globaltoc_depth': -1,


#     # Include hidden TOCs in Site navbar?
#     #
#     # Note: If this is "false", you cannot have mixed ``:hidden:`` and
#     # non-hidden ``toctree`` directives in the same page, or else the build
#     # will break.
#     #
#     # Values: "true" (default) or "false"
#     'globaltoc_includehidden': "true",

#     # HTML navbar class (Default: "navbar") to attach to <div> element.
#     # For black navbar, do "navbar navbar-inverse"
#     'navbar_class': "navbar navbar-inverse",

#     # Fix navigation bar to top of page?
#     # Values: "true" (default) or "false"
#     'navbar_fixed_top': "true",

#     # Location of link to source.
#     # Options are "nav" (default), "footer" or anything else to exclude.
#     'source_link_position': "footer",

#     # Bootswatch (http://bootswatch.com/) theme.
#     #
#     # Options are nothing (default) or the name of a valid theme
#     # such as "amelia" or "cosmo".
#     'bootswatch_theme': "yeti",

#     # Choose Bootstrap version.
#     # Values: "3" (default) or "2" (in quotes)
#     'bootstrap_version': "3",
# }

# html_sidebars = {'**': ['localtoc.html', 'github_sourcelink.html']} #, 'sourcelink.html']} #, 'searchbox.html']}


# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'Electromagnetic Geophysics'

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = 'EM'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = 'disclogo-02.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'favicon.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {
#    '**': [
#        'globaltoc.html',
#        'searchbox.html',
#        'sourcelink.html',
#        ],
# }

# show_related = True

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
#html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'emdoc'

# -- Edit on Github Extension ---------------------------------------------

edit_on_github_project = 'geoscixyz/em'
edit_on_github_branch = 'master'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',

# Latex figure (float) alignment
#'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  (master_doc, 'em.tex', u'em Documentation',
   u'UBCGIF', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = 'favicon.ico'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'em', u'em Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  (master_doc, 'em', u'em Documentation',
   author, 'em', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
# epub_title = project
# epub_author = author
# epub_publisher = author
# epub_copyright = copyright

# The basename for the epub file. It defaults to the project name.
#epub_basename = project

# The HTML theme for the epub output. Since the default themes are not optimized
# for small screen space, using the same theme for HTML and epub output is
# usually not wise. This defaults to 'epub', a theme designed to save visual
# space.
#epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or 'en' if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the Pillow.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#epub_show_urls = 'inline'

# If false, no index is generated.
#epub_use_index = True


# Example configuration for intersphinx: refer to the Python standard library.
# intersphinx_mapping = {'https://simpeg.readthedocs.org/en/latest/': None}

# -- User Defined Methods ------------------------------------------------
sys.path.append(os.getcwd())

from _ext import (
    make_contributorslist, make_formula_sheet, make_case_histories,
    checkDependencies,
    # supress_nonlocal_image_warn,
    copyImages,
    # supress_citation_not_referenced,
    # supress_nonlocal_image_and_citation_not_referenced
)

make_contributorslist()
# make_formula_sheet()
make_case_histories()
# checkDependencies()
# supress_nonlocal_image_warn()
# supress_citation_not_referenced()
# supress_nonlocal_image_and_citation_not_referenced()
copyImages()
