import requests


url = "http://www.k165.com/movies.html"


def get_html_content(url):
    html = requests.get(url)
    return html.content

#print get_html_content(url)
