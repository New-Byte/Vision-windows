from bs4 import BeautifulSoup
from googlesearch import search
import webbrowser as wb
import random 
import sys

query = sys.argv[1]
urls = list(search(query, tld="co.in", num=5, stop=5, pause=2))
url = random.choice(urls)
wb.open(url)

