import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
# beautiful soup web scraping template

my_url = 'https://media.wizards.com/2019/downloads/MagicCompRules%2020191004.txt'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
# convert webpage to string
string = str(page_soup)
# a regex to find a single number followed
# by a period (ex. 1. and not 100.1.)
numberPeriod = r"((?<!...)\b[0-9]\. )"
# use regex to list all numbers (soon)
rules = re.split(numberPeriod, string)
print (rules[0])

