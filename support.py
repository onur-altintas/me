
# DO NOT MODIFY THIS FILE

import os
from google.appengine.ext.webapp import template

def render_page(templatefilename = 'py.html', replacementmap = { }):
    ''' Render a page using the given template and return as a string '''
    templ = os.path.join(
          os.path.dirname(__file__),
          'templates/' + templatefilename)
    if not os.path.isfile(templ):
        raise Exception('Error:  Template ' + templatefilename + 'not found.')
    return template.render(templ, replacementmap)
