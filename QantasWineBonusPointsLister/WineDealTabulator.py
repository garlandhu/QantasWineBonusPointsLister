from tabulate import tabulate


class WineDealTabulator:
	def __init__(self, include_links):
		self._include_links = include_links

	def print(self, wine_list, len):
		print(tabulate(
			[{
				'Value': wine.value,
				'Name': wine.name,
				'Price': wine.price,
				'Bonus': wine.bonus_points,
			} |
			({
				'Link': wine.link
			} if self._include_links else {})
			for wine in wine_list[:len]],
			headers="keys",
		))
