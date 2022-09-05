from bs4 import BeautifulSoup
from QantasWineBonusPointsLister.WineDeal import WineDeal



class WebpageParser:
	empty_page_class_title = "productListingstyled__NoProducts-sc-1yu9dv6-21 lhaZtS"
	wine_listing_class_title = "ProductCardstyled__ProductContainer-sc-1ntcau0-1 iwRuYS"	
	bonus_points_class_title = "ProductCardstyled__SpotLight-sc-1ntcau0-27 dJmRvS"
	listing_detailed_name_class_title = "ProductCardstyled__Name-sc-1ntcau0-9 EJGYI"
	listing_basic_name_class_title = "ProductCardstyled__Brand-sc-1ntcau0-8 kCrfxB"
	price_class_title = "ProductCardstyled__CashPriceText-sc-1ntcau0-17 wuhKx"
	link_class_title = "ProductCardstyled__Thumbnail-sc-1ntcau0-4 kUVstW"

	def __init__(self):
		super().__init__()
		self._done = False
		self._wine_deal_list = []

	def feed(self, html_text):
		soup = BeautifulSoup(html_text, "html.parser")
		if soup("div", {"class": self.empty_page_class_title}):
			self._done = True
		else:
			wine_listings_elements = soup.find_all("div", {"class": self.wine_listing_class_title})
			for wine_listing_element in wine_listings_elements:
				name_element = wine_listing_element.find("span", {"class": self.listing_detailed_name_class_title})
				basic_name_element = wine_listing_element.find("h4", {"class": self.listing_basic_name_class_title})
				bonus_points_element =  wine_listing_element.find("span", {"class": self.bonus_points_class_title})
				price_element = wine_listing_element.find("span", {"class": self.price_class_title})
				link_element = wine_listing_element.find("div", {"class": self.link_class_title})
				
				self._wine_deal_list.append(WineDeal(
					name=name_element.string if name_element else basic_name_element.string,
					bonus_points=int(bonus_points_element.get_text(strip=True).strip("Earn").strip("Bonus Points").replace(",", "")),
					price=float(price_element.string.strip("$")),
					link="https://wine.qantas.com" + link_element.a.get("href"),
				))

	@property
	def done(self):
		return self._done
		
	@property
	def wine_deal_list(self):
		return self._wine_deal_list
