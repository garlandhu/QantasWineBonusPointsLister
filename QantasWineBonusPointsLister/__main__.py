import argparse
from QantasWineBonusPointsLister.Lister import Lister
from QantasWineBonusPointsLister.WebpageParser import WebpageParser
from QantasWineBonusPointsLister.WineDealRetriever import WineDealRetriever
from QantasWineBonusPointsLister.WineDealTabulator import WineDealTabulator


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-n', '--noninteractive', action='store_true', help='Noninteractive module that will print only 10 listings')
	args = parser.parse_args()
	
	lister = Lister(
		retriever=WineDealRetriever(
			wine_deal_url='https://wine.qantas.com/c/browse-products/page-{}?BonusPoints=1&sort=featured',
			parser=WebpageParser(),
			number_of_pages_to_scan=10,
		),
		tabulator=WineDealTabulator(
			include_links=args.noninteractive,
		),
	).run(
		interactive=(not args.noninteractive),
		options_to_display=10 if args.noninteractive else None,
	)
