import scrapy


class CommunitiesSpider(scrapy.Spider):
    name = "communities"
    allowed_domains = ["reddit.com"]
    start_urls = ["https://www.reddit.com/best/communities/1/"]

    def parse(self, response):
        containers = response.xpath('//div[@class="community-list"]/div')

        for container in containers:
            category = container.xpath('//div[@class="community-list"]/div/div/h6/text()').get().strip()
            subreddit = container.xpath('.//a/text()').get().strip()
            yield {
                'url': f'https://www.reddit.com/{subreddit}/',
                'subreddit': subreddit,
                'image': container.xpath('.//faceplate-img/@src').get(),
                'category': category,
                'members': container.xpath('.//faceplate-number/@number').get(),
                'description': container.xpath('./@data-public-description-text').get()
            }

        for url in response.xpath('//div[@id="directory-pagination"]/a/@href').getall():
            yield response.follow(url, self.parse)
