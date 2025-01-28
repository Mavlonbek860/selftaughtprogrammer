from urllib import request
import collections
collections.Callable = collections.abc.Callable
from bs4 import BeautifulSoup

class Scraper:
	
	def __init__(self, site):
		self._site = site
	
	def scrape(self):
		response = request.urlopen(self._site)
		html = response.read()
		soup = BeautifulSoup(html, 'html.parser')
		for tag in soup.find_all('a'):
			url = tag.get('href')
			if url and 'htm' in url:
				yield url

site = 'https://www.geeksforgeeks.org/html-tutorial/?ref=shm'

def printer(page):
	response = request.urlopen(page)
	html = response.read()
	soup = BeautifulSoup(html, 'html.parser')
	title = soup.find_all('title')
	for tag in soup.find_all('h2'):
		#file = open(str(title[0])[7:len(title[0]) - 8] + '.txt', 'w')
		print(tag)
		#file.write(str(tag))
		#file.close()
		for link in soup.find_all('a'):
			print(link.get('href'))

for link in Scraper(site).scrape():
	printer(link)
	break