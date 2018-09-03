from bs4 import BeautifulSoup as bs
import requests

import nltk
import matplotlib

import csv


# url getter: checks if website is 200, returns html
# html cleaner: returns clean content
# tokenizer: returns clean tokens

def scraper(url):
	# cleans html and returns a string
	r = requests.get(url)
	soup = bs(r.text, 'html.parser')
	uncleaned_content = soup.find_all('p')
	cleaned_content = [ str(item.get_text()) for item in uncleaned_content ]
	content = "".join(cleaned_content)
	
	return content


def tokenizer(content):
	# tokenizes, and returns clean  tokens
	stopwords = [ word.strip().lower() for word in open("./stopwords.txt") ]
	tokens = [ tok for tok in content.split() ]
	clean_tokens = [tok for tok in tokens if len(tok.lower()) > 1 and (tok.lower() not in stopwords)]
	
	return clean_tokens


def freq_dist(clean_tokens):
	freq_dist = nltk.FreqDist(clean_tokens)

	items = [ (v, k) for k, v in freq_dist.items() ]
	items.sort()
	items.reverse()
	items = [ (k, v) for v, k in items]

	return items


def csv_exporter(items):
	with open('output.csv', 'w') as f:
		writer = csv.writer(f, delimiter=',')
		for row in zip(items):
			writer.writerow(row)


def main():
	# url = "https://realpython.com/flask-by-example-part-3-text-processing-with-requests-beautifulsoup-nltk/"
	url = "https://realpython.com/setting-up-sublime-text-3-for-full-stack-python-development/"
	content = scraper(url)
	clean_tokens = tokenizer(content)

	to_export = freq_dist(clean_tokens)
	csv_exporter(to_export)

def test(url):
	print(f'{url} passed through quickprime!')
	return url

if __name__ == '__main__':
	main()
