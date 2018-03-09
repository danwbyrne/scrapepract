import urllib2
from bs4 import BeautifulSoup


#for cleaning this awful looking paragraphs
def clean_paragraph(paragraph):
	line = str(paragraph).strip('\n \<p>\</p>')
	line = line.strip('.')

	if line.find('Return to top') != -1:
		return False

	information_ind = line.find('Information:')







	return line


def scrape(url):
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')

	paragraphs = soup.find_all('p')

	for i in range(len(paragraphs)): 
		line    = clean_paragraph(paragraphs[i])

		if i not in range(253,266) and i not in [0]:
			if line != False:
				print('%s    %s\n' % (i,line))










def test():
	scrape_page = 'http://www.carrollcountytimes.com/carrollliving/ph-cc-living-religion-20170622-story.html'
	scrape(scrape_page)

if __name__ == "__main__":
	test()