import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# beautiful soup web scraping template

my_url = 'https://media.wizards.com/2019/downloads/MagicCompRules%2020191004.txt'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

print (page_soup)