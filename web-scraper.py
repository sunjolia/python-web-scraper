import urllib2
import csv
from datetime import datetime
from bs4 import BeautifulSoup

#webpage to scrape
jobs_page = 'https://www.ideo.com/jobs/'

#actual html of page
page = urllib2.urlopen(jobs_page)

#page parsed for bs4
soup = BeautifulSoup(page, 'html.parser')

job_container = soup.find('h2', attrs={'class': 'JobsListing--JobTitle'} )
job = job_container.text

print job
# open a csv file with append, so old data will not be erased
with open('index.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 writer.writerow([job])
