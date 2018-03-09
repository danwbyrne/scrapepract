import urllib2
from bs4 import BeautifulSoup

def scrape(url):
	page = urllib2.urlopen(url)
	parsed = BeautifulSoup(page, 'html.parser')

	paragraphs = parsed.find_all('p')

	for i in range(len(paragraphs)): 
		line = str(paragraphs[i]).strip('\n \<p>\</p>')
		print('%s    %s\n' % (i,line))










def test():
	scrape_page = 'http://www.carrollcountytimes.com/carrollliving/ph-cc-living-religion-20170622-story.html'
	scrape(scrape_page)

if __name__ == "__main__":
	test()