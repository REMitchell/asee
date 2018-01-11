#https://peer.asee.org/advanced_search?collection_id=&page=2&published_after=&published_before=&q=culture&q_in%5B%5D=title&q_in%5B%5D=content&year=

import requests
from bs4 import BeautifulSoup


class ASEEcrawler:
	def getPage(self, url):
		print("Retrieving URL:\n"+url)
		session = requests.Session()
		headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"}
		try:
			req = session.get(url, headers=headers)
		except requests.exceptions.RequestException:
			return None
		bsObj = BeautifulSoup(req.text, "lxml")
		return bsObj

	def safeGet(self, pageObj, selector):
		childObj = pageObj.select(selector)
		if childObj is not None and len(childObj) > 0:
			return childObj[0].get_text()
		return ""

	def parseArticle(self, articlePage):
		title = self.safeGet(articlePage, 'h2')
		abstract = self.safeGet(articlePage, 'div#abstract')
		print('\n---------------------------------')
		print("\nTITLE IS:")
		print(title)
		print("ABSTRACT IS:")
		print(abstract)

	def getArticles(self, articleLinks):
		for articleLink in articleLinks:
			self.parseArticle(self.getPage('https://peer.asee.org/'+articleLink))


	def startSearch(self, term):
		# Limit to 10 pages -- remove references to 'i' if you want EVERYTHING
		i = 1
		searchPage = self.getPage('https://peer.asee.org/advanced_search?collection_id=&page=1&published_after=&published_before=&q='+term+'&q_in%5B%5D=title&q_in%5B%5D=content&year=')
		while 'No results' not in self.safeGet(searchPage, 'h3.panel-title'):
			articleLinks = searchPage.select('h2.panel-title')
			articleLinks = [link.find('a').attrs['href'] for link in articleLinks]
			self.getArticles(articleLinks)
			if i > 10:
				break
			i += 1
			searchPage = self.getPage('https://peer.asee.org/advanced_search?collection_id=&page='+str(i)+'&published_after=&published_before=&q='+term+'&q_in%5B%5D=title&q_in%5B%5D=content&year=')


crawler = ASEEcrawler()
crawler.startSearch('culture')