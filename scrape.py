from lxml import html
import requests

# page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
page = requests.get("https://www.amazon.com/dp/B0013Z0PTW")
tree = html.fromstring(page.content)

# #This will create a list of buyers:
# buyers = tree.xpath('//div[@title="buyer-name"]/text()')
# #This will create a list of prices
# prices = tree.xpath('//span[@class="item-price"]/text()')
#
# print('Buyers: ', buyers)
# print('Prices: ', prices)

ingredients = tree.xpath('//div[@id="important-information"]//div[@class="a-section content"]/text()')
ingredients = tree.xpath('//div[@id="important-information"]/div[@class="a-section content"]/text()')

print(ingredients)