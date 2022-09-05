from QantasWineBonusPointsLister.Lister import Lister
from QantasWineBonusPointsLister.WebpageParser import WebpageParser
from QantasWineBonusPointsLister.WineDealRetriever import WineDealRetriever
from QantasWineBonusPointsLister.WineDealTabulator import WineDealTabulator


if __name__ == '__main__':
	Lister(
		retriever=WineDealRetriever(
			wine_deal_url='https://wine.qantas.com/c/browse-products/page-{}?BonusPoints=1&sort=featured',
			parser=WebpageParser(),
			number_of_pages_to_scan=10,
		),
		tabulator=WineDealTabulator(),
	).run()
	