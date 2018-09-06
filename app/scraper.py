from bs4 import BeautifulSoup as bs
import requests

# scraper.py -> accepts url, returns text content stripped of html
# url getter: checks if website is 200, returns raw_html
# html cleaner: returns clean_content (json?)

def scraper(url):
	r = requests.get(url)
	soup = bs(r.text, 'html.parser')
	uncleaned_content = soup.find_all('p')
	cleaned_content = [ str(item.get_text()) for item in uncleaned_content ]
	content = "".join(cleaned_content)
	
	return content