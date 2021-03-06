def get_movie_list_title(selector):
    title = selector.xpath('//*[@class="nav nav-tabs"]/li/h4/text()')
    return title[0]


def get_movie_sort(selector):
    sorts = {}
    sort_uri = selector.xpath('//*[@class=" nav-tab-right"]/a/@href')
    sort_title = selector.xpath('//*[@class=" nav-tab-right"]/a/text()')
    sort_uri_active = selector.xpath('//*[@class="active nav-tab-right"]/a/@href')
    sort_title_active = selector.xpath('//*[@class="active nav-tab-right"]/a/text()')
    sorts.update({sort_uri[0]: sort_title[0], sort_uri_active[0]: sort_title_active[0]})
    return sorts


def get_movie_list(selector):
    movie_list = dict()
    movie_url = selector.xpath('//*[@class="span1"]/a/@href')
    movie_img = selector.xpath('//*[@class="span1"]/a/img/@src')
    movie_title = selector.xpath('//*[@class="span8"]/p[1]/a[1]/text()')
    movie_des = selector.xpath('//*[@class="span8"]/p[2]/text()')
    movie_list.update({"movie_url": movie_url, "movie_img": movie_img, "movie_title": movie_title, "movie_des": movie_des})
    return movie_list
