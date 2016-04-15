def get_movie_title(selector):
    title = selector.xpath('//h4[1]/text()')
    return title[0]


def get_movie_summary(selector):
    content = selector.xpath('//div[@id="post_0"]//div[@class="popover-content"]/text()')
    return content


def get_movie_content(selector):
    content = selector.xpath(
        '//*[@class="post"]/text() | //*[@class="post"]/img/@src | //*[@class="d_post_content"]/text() | //*[@class="d_post_content"]/img/@src')
    return content
