from tabulate import tabulate


class WineDealTabulator:
	def print(self, wine_list, len):
		print(tabulate(
			[{'Value': wine.value, 'Name': wine.name, 'Price': wine.price, 'Bonus': wine.bonus_points, 'Link': wine.link} for wine in wine_list[:len]],
			headers="keys",
		))
