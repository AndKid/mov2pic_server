def get_navigation(selector):
    nav = {}
    nav_uri_list = selector.xpath('//*[@class="nav"]/li/a/@href')
    nav_title_list = selector.xpath('//*[@class="nav"]/li/a/text()')
    nav_uri_list[0] = "/movies.html"
    for i in range(len(nav_uri_list)):
        nav.update({nav_uri_list[i]: nav_title_list[i]})
    return nav


def get_next_page(selector):
    next_page = selector.xpath('//a[@rel="next"]/@href')
    return next_page[0]
