# Copyright (C) ALbert Mietus, SoftwareBeterMaken.nl; 2011-2024
#  STANDARD CONFiguration for Sphinx-doc
# -*- coding: utf-8 -*-

import os
on_rtd = os.environ.get('READTHEDOCS') == 'True'

print("Using std_conf [%s-version]" % ('RTfD' if on_rtd else 'local'))

###
### File/Project layout
###

master_doc = 'index'
source_suffix = '.rst'
exclude_patterns = ['**/.#*', '**/_*', '*VENV*']
html_static_path = ['_std_settings/static/']
templates_path = ['_templates']

###
### Kick off
###
try:    extensions = extensions
except NameError: extensions=[]

show_authors = False # Always me

rst_epilog = None
rst_prolog = """
.. include:: /_generic.inc

"""

###
### Normal HTML output
###

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'collapse_navigation': True,
    'display_version': True,
    'style_external_links': False,
    'prev_next_buttons_location': 'both',
    # 'vcs_pageview_mode': 'view',
}
html_style = 'SwBMnl+rtfd.css'

html_context={'display_github':False} 

#html_logo= ...file...
#html_theme_options['logo_only']=True # True: only logo, False: Logo & name

# sphinx.ext.todo
#-----------------
extensions.append('sphinx.ext.todo')
todo_include_todos=True

# sphinx.ext.autodoc'
#--------------------
extensions.append('sphinx.ext.autodoc')
autodoc_member_order='bysource'


# plantUML
#---------
extensions.append('sphinxcontrib.plantuml')
plantuml_syntax_error_image=True
plantuml_output_format='svg_img'                                     # Override this, when dito is used:
#plantuml_output_format='png'                                        ## dito only can be png?
if on_rtd:
    #  in `.readthedocs.yaml`
    #     post_install:
    #      - curl -o ${READTHEDOCS_VIRTUALENV_PATH}/libexec/plantuml.jar -L https://github.com/plantuml/....
    # Make use of that plantUML version
    import os
    _path=os.environ['READTHEDOCS_VIRTUALENV_PATH'] + '/libexec/'
    plantuml = f'java  -Djava.awt.headless=true  -jar {_path}plantuml.jar'
    #print(f'DEBUG: plantuml={plantuml}')
else: #local
    #plantuml = 'java  -Djava.awt.headless=true  -jar /Users/albert/Apps/PlantUML/libexec/plantuml-1.2024.4.jar' # NEW
    plantuml = 'plantuml' # The one in VENV

if True or DEBUG:
    import subprocess
    result = subprocess.run(plantuml.split() +['-version'], stdout=subprocess.PIPE)
    print(f"Using plantuml -version: {result.stdout}")


# Needs
#------
extensions.append('sphinxcontrib.needs')
needs_include_needs = True
needs_id_required = True
needs_id_regex = r'^[A-Z][A-Za-z-0-9_]{4,}'
needs_extra_options = ['project', 'category']

needs_types = [
    dict(directive="demo", title="Demonstrator",   prefix="D_", color="#9DC5BB", style="node"),
    dict(directive="req",  title="Requirement",    prefix="R_", color="#C5EBC3", style="frame"),
    dict(directive="spec", title="Specification",  prefix="S_", color="#FEDCD2", style="component"),
    dict(directive="impl", title="Implementation", prefix="I_", color="#DF744A", style="artifact"),
    dict(directive="test", title="Test_Case",      prefix="T_", color="#F6E27F", style="folder")
]

needs_layouts = {
    'clean_collapsed': {'grid': 'simple',
                 'layout': {
                     'head': [
                         '<<meta("type_name")>>: **<<meta("title")>>** <<meta_id()>>  <<collapse_button("meta", '
                         'collapsed="icon:arrow-down-circle", visible="icon:arrow-right-circle", initial=True)>> '],
                     'meta': [
                         '<<meta_all(no_links=True)>>',
                         '<<meta_links_all()>>'],
                 }}}
needs_default_layout = 'clean_collapsed'

