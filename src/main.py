import urllib2
from bs4 import BeautifulSoup

def scrape(url):
	pass









def test():
	scrape_page = 'http://www.carrollcountytimes.com/carrollliving/ph-cc-living-religion-20170622-story.html'
	page = urllib2.urlopen(scrape_page)

	parsed = BeautifulSoup(page, 'html.parser')

	print(parsed)

if __name__ == "__main__":
	test()