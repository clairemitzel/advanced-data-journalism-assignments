import requests, mechanize 
from bs4 import BeautifulSoup

url = 'https://www.mshp.dps.missouri.gov/HP71/SearchAction?searchDate=10/31/2017'

br = mechanize.Browser()
br.open(url)
html = br.response().read()

soup = BeautifulSoup(html, "html.parser")

main_table = soup.find('table')

row_list = main_table.find_all('tr')

for r in row_list:

    cell_list = r.find_all('td')

    if len(cell_list) > 0:
        for c in cell_list:
        	print c.text.strip()

        print '----------'

print 'IT WORKED!'