import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import json
# beautiful soup web scraping template

my_url = 'https://media.wizards.com/2019/downloads/MagicCompRules%2020191004.txt'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")

# convert webpage to string
string = str(page_soup)

# using "Glossary" to split up the rules
splitByGloss = string.split("Glossary")

# the chunck of the rules that actually matters
ruleChunk = splitByGloss[1]

# a regex to find a single number followed
# by a period (ex. 1. and not 100.1.)
numberPeriod = r"((?<!...)\b[0-9]\.) (.*)"
# use regex to list all numbers (soon)
contents = re.findall(numberPeriod, ruleChunk)

# empty dictionary to be stored with rules
RulesObj = {}

# add default rules section to main rules dict
for i in contents:
    text = i[1].split("\r")
    RulesObj[i[0]] = {
        "title": text[0]
    }
# regex to find 3 nums followed by a period,
# but nothing after. (ex. 100. and not 100.1.)
sections = r'((?<!...)\b[0-9][0-9][0-9]\.) (.*)'

allSections = re.findall(sections, ruleChunk)

# put all sections into RulesObj
for i in allSections:
    text = i[1].split("\r")
    for j in RulesObj:
        if i[0][0] == j[0]:
            RulesObj[j][i[0]] = {
                "title": text[0]
                }


# regex for rules ###.#. and not ###.#[a-Z]
rules = r"((?<!...)\b[0-9][0-9][0-9]\.[0-9]\.) (.*)"

allRules = re.findall(rules, ruleChunk)

# put all rules in sections
for i in allRules:
    text = i[1].split("\r")
    for firstKey in RulesObj:
        for section in RulesObj[firstKey]:
            if i[0][0] == section[0]: 
                RulesObj[firstKey][section][i[0]] = {
                    "rule": text[0]
                }


subRules = r"((?<!...)\b[0-9][0-9][0-9]\.[0-9][a-z]) (.*)"

allSubRules = re.findall(subRules, ruleChunk)

# put all subrules in rules
for i in allSubRules:
    text = i[1].split("\r")
    for firstKey in RulesObj:
        for section in RulesObj[firstKey]:
            for rule in RulesObj[firstKey][section]:
                if rule[0:5] == i[0][0:5]:
                    RulesObj[firstKey][section][rule][i[0]] = text[0]

with open('data.json', 'w') as fp:
    json.dump(RulesObj, fp)