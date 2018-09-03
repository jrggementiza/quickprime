from bs4 import BeautifulSoup as bs
import requests


import nltk
import matplotlib

import csv

# scraper
# url getter: checks if website is 200, returns raw_html
# html cleaner: returns clean_content (json?)

# tokenizer: returns tokens

# cleaner: returns clean_tokens

# to display:
# total word count
# all words (ordered by)
# top 10 words
# rare 10 words
# longest word

def scraper(url):
	r = requests.get(url)
	soup = bs(r.text, 'html.parser')
	uncleaned_content = soup.find_all('p')
	cleaned_content = [ str(item.get_text()) for item in uncleaned_content ]
	content = "".join(cleaned_content)
	
	return content


def tokenizer(content):
	tokens = [ tok for tok in content.split() ]
	
	return tokens


def cleaner(tokens, stopwords):
	clean_tokens = [tok for tok in tokens if len(tok.lower()) > 1 and tok.lower() not in stopwords ]
	
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


def main(url):
	stopwords = [ word.strip().lower() for word in open("./stopwords.txt") ]
	
	content = scraper(url)
	tokens = tokenizer(content)
	clean_tokens = cleaner(tokens, stopwords)

	results = freq_dist(clean_tokens) #most frequent

	return results


def test(url):
	print(f'{url} passed through quickprime!')
	return url


if __name__ == '__main__':
	main()
