import scrapy

class MySpider(scrapy.Spider):
    name = "my_spider"  # Unique name for the spider
    start_urls = ["https://lu.ma/5bhpkke4?tk=Quu1Oy"]  # Replace with your target website

    def parse(self, response):
        # Extracting all text from the page
        page_text = response.xpath("//body//text()").getall()
        cleaned_text = " ".join(text.strip() for text in page_text if text.strip())

        yield {
            "url": response.url,
            "content": cleaned_text
        }
