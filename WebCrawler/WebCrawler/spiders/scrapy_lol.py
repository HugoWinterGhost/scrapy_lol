from asyncio.windows_events import NULL
import scrapy
import math
from scrapy import Request
from WebCrawler.items import ReviewLoLItem


class ScrapyLolSpider(scrapy.Spider):
  name = 'scrapy_lol'
  allowed_domains = ['u.gg']
  start_url = ['https://www.leagueofgraphs.com/fr/champions/builds']

  def parse_lol(self, response):
    champions_list = response.css('div.box-padding-10-dark-only table tr')
    
    # Boucle qui parcours l'ensemble des éléments de la liste des champions
    for champion in champions_list:
      item = ReviewLoLItem()

      # Nom du champion
      try:
        item['name'] = champion.css('td span.name::text')[0].extract().strip()
      except:
        item['name'] = 'NaN'

      # Rôle du champion
      try:
        item['role'] = champion.css('td div.txt i::text')[0].extract().strip()
      except:
        item['role'] = 'NaN'

      # Classement du champion
      try:
        item['rank'] = champion.css('td.text-right::text')[0].extract().strip().replace('.', '')
      except:
        item['rank'] = 'NaN'
      
      # Popularité du champion
      try:
        fame_temp = champion.css('td progressbar')[0].attrib['data-value']
        fame_temp_float = float(fame_temp)
        item['fame'] = f'{round(fame_temp_float * 100, 2)}%'
      except:
        item['fame'] = 'NaN'

      # Taux de victoire du champion
      try:
        victory_temp = champion.css('td progressbar')[1].attrib['data-value']
        victory_temp_float = float(victory_temp)
        item['victory'] = f'{round(victory_temp_float * 100, 2)}%'
      except:
        item['victory'] = 'NaN'

      # Taux de ban du champion
      try:
        ban_rate_temp = champion.css('td progressbar')[2].attrib['data-value']
        ban_rate_temp_float = float(ban_rate_temp)
        item['ban_rate'] = f'{round(ban_rate_temp_float * 100, 2)}%'
      except:
        item['ban_rate'] = 'NaN'

      # KDA du champion
      try:
        kda_temp = [element.extract() for element in champion.css('td.text-center.hide-for-small-down span::text')]
        item['kda'] = ' / ' . join(kda_temp)
      except:
        item['kda'] = 'NaN'

      # Pentas par match du champion
      try:
        item['pentas_match'] = champion.css('td.text-center.hide-for-small-down::text')[4].extract().strip()
      except:
        item['pentas_match'] = 'NaN'

      yield item
  
  def start_requests(self):
    for url in self.start_url:
      yield Request(url = url, callback = self.parse_lol)
