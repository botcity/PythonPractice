#!/usr/local/bin/python3.4


##
## Practice Python Course: Exercise 17
## Decode a webpage
##
# Use the BeautifulSoup and requests Python packages to print out a list of all the 
# article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

def parseDoc(var):
	soup = BeautifulSoup(var, 'html.parser')
	soup.prettify()
	soup_h2 = (soup.find_all('h2', class_='story-heading'))
	for link in soup_h2:
		if link.a:
			print(link.a.text.replace("\n", " ").strip() + "\n")
		else:
			print(link.contents[0].strip())
	


def getPage(site):
	page = requests.get(site)
	page = page.content
	parseDoc(page)



def main():
	print("This is a cool NyTimes homepage article title grabber!" + "\n#########################################"
	+ "\n#########################################\n")
	site = "http://www.nytimes.com"
	getPage(site)


if __name__ == "__main__":
	main()
	
exit()
