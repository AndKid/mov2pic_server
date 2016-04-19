def get_header_background(selector):
    backgrounds = selector.xpath('//div[@class="photo-pic"]/a/img/@src')
    url_prefix = "http://www.wufafuwu.com"
    for index in range(0, 7):
        backgrounds[index] = url_prefix + backgrounds[index]
    return backgrounds[0:8]
