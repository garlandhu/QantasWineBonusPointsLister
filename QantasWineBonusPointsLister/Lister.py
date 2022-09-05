
class Lister:
	def __init__(self, retriever, tabulator):
		self._retriever = retriever
		self._tabulator = tabulator
		
	def run(self):
		wine_list = self._retriever.get_wine_list()
		print(f'Found {len(wine_list)} deals')
		ordered_wine_list = sorted(wine_list, key=lambda wine: wine.value, reverse=True)
		
		options_to_display = int(input('How many shall I list? '))
		self._tabulator.print(ordered_wine_list, len=options_to_display)
		while True:
			index_to_clipboard = int(input('Copy link to clipboard '))
			ordered_wine_list[index_to_clipboard].copy_to_clipboard()
