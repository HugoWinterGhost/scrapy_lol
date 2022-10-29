import scrapy


class WebcrawlerItem(scrapy.Item):
  pass

class ReviewLoLItem(scrapy.Item):
  name = scrapy.Field()
  role = scrapy.Field()
  rank = scrapy.Field()
  fame = scrapy.Field()
  victory = scrapy.Field()
  ban_rate = scrapy.Field()
  kda = scrapy.Field()
  pentas_match = scrapy.Field()
