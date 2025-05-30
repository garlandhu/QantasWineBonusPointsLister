from bs4 import BeautifulSoup
from QantasWineBonusPointsLister.WineDeal import WineDeal
import re


class WebpageParser:
	def feed(self, html_text):
		soup = BeautifulSoup(html_text, "html.parser")
		if soup("div", test=re.compile("No products found")):
			return None

		wine_deal_list = []

		wine_listings_elements = soup.find_all("a", href=lambda value: value and value.startswith("/p/"))
		for wine_listing_element in wine_listings_elements:
			name_element = wine_listing_element.find("span", lambda value: value)
			basic_name_element = wine_listing_element.find("h4")
			bonus_points_element =  wine_listing_element.find("span")
			price_element = wine_listing_element.find("span", text=lambda value: value and value.startswith("$"))
			if price_element is None:
				continue
			wine_deal_list.append(WineDeal(
				name=name_element.string if name_element else basic_name_element.string,
				bonus_points=int(bonus_points_element.get_text(strip=True).strip("Earn").strip("Bonus Points").replace(",", "")),
				price=float(price_element.string.strip("$")),
				link="https://wine.qantas.com" + wine_listing_element.get("href"),
			))

		return wine_deal_list
