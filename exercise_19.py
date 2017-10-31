#!/usr/local/bin/python3.4


##
## Practice Python Course: Exercise 19
## Decode a Web Page 2
##
# Using the requests and BeautifulSoup Python libraries, print to the screen the full 
# text of the article on this website: 
# http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
# The article is long, so it is split up between 4 pages. Your task is to print 
# out the text to the screen so that you can read the full article without having 
# to click any buttons. (Hint: The post here describes in detail how to use the 
# BeautifulSoup and requests libraries through the solution of the exercise posted here.)
# This will just print the full text of the article to the screen. It will not make it 
# easy to read, so next exercise we will learn how to write this text to a .txt file.

import requests 
from bs4 import BeautifulSoup


def getPage(url):
	req = requests.get(url)	
	print('HTTP code is ' + str(req.status_code))
	doc = req.content
	parseDoc(doc)

def parseDoc(doc):
	soupdoc = BeautifulSoup(doc, 'html.parser')
	soupdoc.prettify()
	souptag = soupdoc.find_all('p') # Grabs all <p> tags in the doc
	count = 0	# Used to print out line count
	for stuff in souptag:		# for all of the stuff in souptags
		if int(stuff.attrs['data-reactid']) < 317: # convert the data-reactid=x value to int and maek sure value is under 317
			print(str(count) + '   ' + stuff.text + '\n') # print out text
			count += 1
	


def main():
	url = 'http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture'
	getPage(url)

if __name__ == '__main__':
	main()
	
exit()