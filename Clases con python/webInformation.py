import requests
from bs4 import BeautifulSoup



class WebInformation():
	def __init__(self, url):
		self.url = url

	def reverseip(self):
		if self.url.startswith("http://"):
			target_url = self.url.replace("http://", "")
		else:
			target_url = self.url
		data = {"remoteHost": target_url}
		con = requests.post(
			url ="http://www.ipfingerprints.com/scripts/getReverseIP.php",
			data=data
		)
		soup = BeautifulSoup(con.text)
		response = list()
		for link in soup.find_all("a"):
			current_link = link.get("href")
			response.append(current_link[11:-2])
			return response

	def technologies(self):
		if not self.url.startswith("http://"):
			if self.url.startswith("www"):
				url = "http://"+self.url
			elif not self.url.startswith("www"):
				url = "http://www."+self.url
			else:
				return "Bad URL"
		con = requests.get(url=url)
		headers = con.headers.get("server")
		return headers

