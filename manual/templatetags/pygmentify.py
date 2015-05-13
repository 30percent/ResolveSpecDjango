'''
from django import template
from django.template.defaultfilters import stringfilter
import warnings
warnings.simplefilter('ignore')
from pygments.lexers import LEXERS, get_lexer_by_name
warnings.resetwarnings()
from pygments import highlight
from pygments.formatters import HtmlFormatter
from lxml import html

def pygmentify_text(text):
    default_lang = 'text'

    #a tuple of known lexer names
    lexer_names = reduce(lambda a,b: a + b[2], LEXERS.itervalues(), ())

    #default formatter
    formatter = HtmlFormatter(encoding='utf-8', linenos='inline')

    html_node = html.fragment_fromstring(text, create_parents='div')
    new_html_node = html_node
    for code_node in html_node.findall('pre'):
        if not code_node.text:
            continue
        lang = code_node.attrib.get('lang', default_lang)
        if lang not in lexer_names:
            lang = default_lang
        lexer = get_lexer_by_name(lang, stripall=True)
        new_code_node = html.fragment_fromstring(highlight(code_node.text, lexer, formatter))
        new_html_node.replace(code_node, new_code_node)
    #need to strip the enclosing div
    return html.tostring(new_html_node,
                         encoding=unicode, method='xml')[5:-6]


register = template.Library()

#truncate after set character length
@register.filter
@stringfilter
def pygmentify(value):
    try:
        res = pygmentify_text(value)
    except Exception, e:
        print e
        print 'value="%s"' % value
        res = value
    return res
'''
import re 
import pygments 
from django import template 
from pygments import lexers 
from pygments import formatters 
 
register = template.Library() 
regex = re.compile(r'<code(.*?)>(.*?)</code>', re.DOTALL) 
 
@register.filter(name='pygmentify') 
def pygmentify(value): 
    last_end = 0 
    to_return = '' 
    found = 0 
    for match_obj in regex.finditer(value): 
        code_class = match_obj.group(1) 
        code_string = match_obj.group(2) 
        if code_class.find('class'): 
            language = re.split(r'"|\'', code_class)[1] 
            lexer = lexers.get_lexer_by_name(language) 
        else: 
            try: 
                lexer = lexers.guess_lexer(str(code_string)) 
            except ValueError: 
                lexer = lexers.PythonLexer() 
        pygmented_string = pygments.highlight(code_string, lexer, formatters.HtmlFormatter()) 
        to_return = to_return + value[last_end:match_obj.start(0)] + pygmented_string 
        last_end = match_obj.end(2) 
        found = found + 1 
    to_return = to_return + value[last_end:] 
    return to_return 
