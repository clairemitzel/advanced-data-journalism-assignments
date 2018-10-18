import requests, mechanize #Will import the library from BeautifulSoup
from bs4 import BeautifulSoup #Import BeautifulSoup

url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
#This is the URL the commandline will scrape
br = mechanize.Browser() #Mechanize the browser
br.open(url) #Open the URL mentioned above
html = br.response().read()#get response from browser

soup = BeautifulSoup(html, "html.parser")#parse html from web page

main_table = soup.find('tbody',
    {'id': 'mrc_main_table'}#find the table to scrape data
)

row_list = main_table.find_all('tr')#the rows equate to main table

for r in row_list:#for each row in the list

    cell_list = r.find_all('td')#finds every cell in the row

    if len(cell_list) > 0:#if letter count is > 0
        for c in cell_list:#for each cell
            print c.text.strip()#print text of each cell

        print '----------'#print line to separate entries

print 'IT WORKED!'#print at the end of list