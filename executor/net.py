import requests
from parserme import parse_background, parse_content


def get_html_content(url):
    html = requests.get(url)
    return html.content


# parse_background(get_html_content("http://www.wufafuwu.com/a/ONE_tupian/list_11_80.html"))
# parse_content(get_html_content("http://www.k165.com/movies/866/page/4.html"))
