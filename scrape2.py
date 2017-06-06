from lxml import html
import requests
from time import sleep
import pandas as pd

def AmzonParser(i):
	url = "http://www.amazon.com/dp/" + i
	# print("Processing: " + url)
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
	page = requests.get(url,headers=headers)
	try:
		doc = html.fromstring(page.content)
		XPATH_CATEGORY = '//a[@class="a-link-normal a-color-tertiary"]//text()'
		XPATH_INGREDIENT = '//div[@id="important-information"]//div[@class="a-section content"]//text()'
		XPATH_PROD_DESCRIPTION = '//div[@id="productDescription"]//text()'
		RAW_CATEGORY = doc.xpath(XPATH_CATEGORY)
		RAW_INGREDIENT = doc.xpath(XPATH_INGREDIENT)
		RAW_PROD_DESCRIPTION = doc.xpath(XPATH_PROD_DESCRIPTION)
		CATEGORY = ' > '.join([i.strip() for i in RAW_CATEGORY]) if RAW_CATEGORY else None
		INGREDIENT = ''.join(RAW_INGREDIENT).strip() if RAW_INGREDIENT else None
		if "Legal Disclaimer" in INGREDIENT:
			INGREDIENT = INGREDIENT[0:INGREDIENT.find("Legal Disclaimer")]
		PROD_DESCRIPTION = ''.join(RAW_PROD_DESCRIPTION).strip() if RAW_PROD_DESCRIPTION else None
		if page.status_code == 200 and "pets" or "pet" in CATEGORY:
			print(i,",",INGREDIENT+PROD_DESCRIPTION)

	except:
		print(i)

def ReadAsin():
	# AsinList = csv.DictReader(open(os.path.join(os.path.dirname(__file__),"uniq_prod_id.txt")))
	AsinList = pd.read_csv("uniq_prod_id.txt")
	c = 1;
	for i in AsinList.ProductId.values:
		AmzonParser(i)
		if c % 20 == 0:
			sleep(30)
		sleep(5)
		c += 1


if __name__ == "__main__":
    ReadAsin()