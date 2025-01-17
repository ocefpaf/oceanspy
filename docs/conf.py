#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# oceanspy documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  9 13:47:02 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import datetime

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#
import os
import sys
import urllib

import yaml

sys.path.insert(0, os.path.abspath(".."))
import oceanspy  # noqa E402
from oceanspy.open_oceandataset import _find_entries  # noqa E402

# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.mathjax",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "numpydoc",
    "nbsphinx",
    "IPython.sphinxext.ipython_directive",
    "IPython.sphinxext.ipython_console_highlighting",
]

autosummary_generate = True
numpydoc_class_members_toctree = True
numpydoc_show_class_members = False

# never execute notebooks: avoids lots of expensive imports on rtd
# https://nbsphinx.readthedocs.io/en/0.2.14/never-execute.html
nbsphinx_execute = "never"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
project = "OceanSpy"
copyright = "2018-%s, OceanSpy developers" % datetime.datetime.now().year
author = "Mattia Almansi"

# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#
# The short X.Y version.
version = oceanspy.__version__
# The full version, including alpha/beta/rc tags.
release = oceanspy.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Theme options are theme-specific and customize the look and feel of a
# theme further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {"logo_only": True}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/oceanspy_logo_white.png"

# -- Options for HTMLHelp output ---------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "oceanspydoc"


# -- Options for LaTeX output ------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
    (master_doc, "oceanspy.tex", "OceanSpy Documentation", "Mattia Almansi", "manual")
]


# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "oceanspy", "OceanSpy Documentation", [author], 1)]


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "oceanspy",
        "OceanSpy Documentation",
        author,
        "oceanspy",
        "One line description of project.",
        "Miscellaneous",
    )
]


# This is processed by Jinja2 and inserted before each notebook
nbsphinx_prolog = r"""
{% set docname = env.doc2path(env.docname, base='docs') %}

.. only:: html

    .. role:: raw-html(raw)
        :format: html

    .. nbinfo::

        This page was generated from `{{ docname }}`__.

    __ https://github.com/hainegroup/oceanspy/blob/main
        /{{ docname }}
"""


# Get custom people data into sphinx
# Borrowed from Pangeo's website
with open("data/people.yml") as people_data_file:
    people = yaml.load(people_data_file, Loader=yaml.FullLoader)
people.sort(key=lambda x: x["last_name"].lower())

html_context = {"people": people}


# Create page with
# Datasets available on SciServer
citations = {
    "Almansi et al., 2017 - JPO.": "https://journals.ametsoc.org"
    "/doi/full/10.1175/JPO-D-17-0129.1",
    "Magaldi and Haine, 2015 - DSR.": "https://www.sciencedirect.com/"
    "science/article/pii/S0967063714001915",
    "Fraser et al., 2018 - JGR.": "https://agupubs.onlinelibrary.wiley.com"
    "/doi/full/10.1029/2018JC014435",
}
rst = open("datasets.rst", "w")
rst.write(
    ".. _datasets:\n\n"
    "========\n"
    "Datasets\n"
    "========\n\n"
    "List of datasets available on SciServer.\n\n"
)

# SCISERVER DATASETS
url = (
    "https://raw.githubusercontent.com/hainegroup/oceanspy/"
    "main/sciserver_catalogs/datasets_list.yaml"
)
f = urllib.request.urlopen(url)
SCISERVER_DATASETS = yaml.safe_load(f)["datasets"]["sciserver"]

for name in SCISERVER_DATASETS:
    if name in ["Arctic_Control", "LLC4320", "HYCOM", "HYBRID", "CORE"]:
        continue

    # Section
    rst.write(".. _" + name + ":\n\n")
    rst.write("{}\n{}\n{}\n\n".format("-" * len(name), name, "-" * len(name)))

    cat, entries, url, intake_switch = _find_entries(name, None)
    metadata = {}
    for entry in entries:
        if intake_switch:
            mtdt = cat[entry].metadata
        else:
            mtdt = cat[entry].pop("metadata", None)
        metadata = {**metadata, **mtdt}

    # Description
    toprint = metadata.pop("description", None)
    for add_str in ["citation", "characteristics", "mates"]:
        thisprint = metadata.pop(add_str, None)
        if thisprint is not None:
            if add_str == "mates":
                add_str = "see also"
            if thisprint[-1:] == "\n":
                thisprint = thisprint[:-1]
            toprint += "\n{}:\n\n* {}\n".format(
                add_str.capitalize(), thisprint.replace("\n", "\n* ")
            )
    for n in SCISERVER_DATASETS:
        toprint = toprint.replace(n, n + "_")
    for cit in citations:
        toprint = toprint.replace(cit, "`{}`_".format(cit))
    rst.write(toprint + "\n\n")

    # Commands
    rst.write("Run the following code to open the dataset:\n\n")
    rst.write(
        ".. code-block:: ipython\n"
        "    :class: no-execute\n\n"
        "    import oceanspy as ospy\n"
        "    od = ospy.open_oceandataset.from_catalog('{}')\n\n"
        "".format(name)
    )

for k, v in citations.items():
    rst.write(".. _`{}`: {}\n".format(k, v))
rst.close()
