import urllib2
from bs4 import BeautifulSoup
import re

def parse_details(details):
	details.strip(' ')
	split_ind = details.find(',')

	org     = details[:split_ind].strip(' \,')
	address = details[split_ind:].strip(' \,')
	return (org, address)



def get_phone(info):
	if info == None: return None
	pattern = re.compile(".*?(\(?\d{3}\D{0,3}\d{3}\D{0,3}\d{4}).*?")
	match   = re.match(pattern, info)

	try:
		return(match.group(0).strip(' '))

	except:
		return None

def get_contact(info):
	pass

def get_link(info):
	pass



#we are converting from cleaned paragraph strings to lists here
def parse_paragraph(paragraph):
	org, org_link, contact, phone, address = None, None, None, None, None

	para_split       = paragraph.split('Information:')

	#real lazy right here
	try:
		details, info = para_split[0], para_split[1]
	except:
		details, info = para_split[0], None

	org, address = parse_details(details)

	org_link = get_link(info)
	contact = get_contact(info)
	phone = get_phone(info)







	return [org, address, phone]


	#return org, org_link, contact, phone, address

#for cleaning this awful looking paragraphs
def convert_paragraph(paragraph):
	line = str(paragraph).strip('\n \<p>\</p>')
	line = line.strip('.')

	if line.find('Return to top') != -1:
		return False

	return parse_paragraph(line)

def scrape(url):
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page, 'html.parser')

	paragraphs = soup.find_all('p')

	for i in range(len(paragraphs)): 
		line    = convert_paragraph(paragraphs[i])

		if i not in range(253,266) and i != 0:
			if line != False:
				print('%s:::%s\n' % (i, line))


def test():
	info = ' 410-489-2999, 301-829-2403, <a href="mailto:Gerald.baker@worldnet.att.net">Gerald.baker@worldnet.att.net</a>'


if __name__ == "__main__":
	test()

	#scrape_page = 'http://www.carrollcountytimes.com/carrollliving/ph-cc-living-religion-20170622-story.html'
	#scrape(scrape_page)


