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
