from app.scraper import scraper
from app.word_processor import tokenizer, cleaner, freq_dist


def csv_exporter(items):
	with open('output.csv', 'w') as f:
		writer = csv.writer(f, delimiter=',')
		for row in zip(items):
			writer.writerow(row)


def quick_prime(url):
	stopwords = [ word.strip().lower() for word in open("./stopwords.txt") ]
	
	content = scraper(url)
	tokens = tokenizer(content)
	clean_tokens = cleaner(tokens, stopwords)
	results, most_frequent_list = freq_dist(clean_tokens) #most frequent

	return results, most_frequent_list

def test(url):
	print(f'{url} passed through quick_prime!')
	return url


if __name__ == '__main__':
	quick_prime()
