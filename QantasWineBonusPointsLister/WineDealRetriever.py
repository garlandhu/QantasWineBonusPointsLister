import requests


class WineDealRetriever:
	def __init__(self, wine_deal_url, parser, number_of_pages_to_scan, retry_attempts):
		self._wine_deal_url = wine_deal_url
		self._parser = parser
		self._number_of_pages_to_scan = number_of_pages_to_scan
		self._wine_deal_list = []
		self._retry_attempts = retry_attempts
		
	def get_wine_list(self):
		for _ in range(self._retry_attempts):
			wine_list = self._get_wine_list()
			if len(wine_list) != 0:
				break
		return wine_list
	
	def _get_wine_list(self):
		for counter in range(1, self._number_of_pages_to_scan):
			page = requests.get(self._wine_deal_url.format(counter), timeout=10)
			new_deals = self._parser.feed(page.text)
			if new_deals:
				self._wine_deal_list += new_deals
			else:
				break

		print(f'Scanned {counter - 1} pages of wine deals.')
		return self._wine_deal_list
