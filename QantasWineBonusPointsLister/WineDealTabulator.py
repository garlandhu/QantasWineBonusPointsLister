from tabulate import tabulate


class WineDealTabulator:
	def __init__(self, include_links, for_github_markdown):
		self._include_links = include_links
		self._for_github_markdown = for_github_markdown

	def print(self, wine_list, len):
		print(tabulate(
			[{
				'Point Cost (c)': wine.value,
				'Name': wine.name,
				'Price': wine.price,
				'Bonus': wine.bonus_points,
			} |
			({
				'Link': wine.link
			} if self._include_links else {})
			for wine in wine_list[:len]],
			headers="keys",
			tablefmt="github" if self._for_github_markdown else "simple",
		))
