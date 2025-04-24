import scrapy


class QiitaTrenD1Spider(scrapy.Spider):
    name = "qiita_tren_d1"
    allowed_domains = ["qiita.com"]
    start_urls = ["https://qiita.com/"]

    def parse(self, response):
        pass
