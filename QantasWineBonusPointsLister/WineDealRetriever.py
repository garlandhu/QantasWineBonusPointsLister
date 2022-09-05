import requests


class WineDealRetriever:
	def __init__(self, wine_deal_url, parser, number_of_pages_to_scan):
		self._wine_deal_url = wine_deal_url
		self._parser = parser
		self._number_of_pages_to_scan = number_of_pages_to_scan
		self._wine_deal_list = []
		
	def get_wine_list(self):
		for counter in range(1, self._number_of_pages_to_scan):
			page = requests.get(self._wine_deal_url.format(counter))
			new_deals = self._parser.feed(page.text)
			if new_deals:
				self._wine_deal_list += new_deals
			else:
				break
		
		print(f'Scanned {counter - 1} pages of wine deals.')
		return self._wine_deal_list
