import pyperclip


class WineDeal:
	def __init__(self, name, link, bonus_points, price):
		self._name = name
		self._link = link
		self._bonus_points = bonus_points
		self._price = price
		self._value = price / (bonus_points * 100)
		
	@property
	def name(self):
		return self._name
	
	@property
	def link(self):
		return self._link
			
	@property
	def bonus_points(self):
		return self._bonus_points
			
	@property
	def price(self):
		return self._price

	@property
	def value(self):
		return self._value	

	def copy_to_clipboard(self):
		pyperclip.copy(self._link)
		print(f'Copied {self._link} to clipboard')
