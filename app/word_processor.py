import nltk
import matplotlib

# word_processor.py -> accepts text, returns clean tokens
# tokenizer: returns tokens
# cleaner: returns clean_tokens

def tokenizer(content):
	tokens = [ tok for tok in content.split() ]
	
	return tokens


def cleaner(tokens, stopwords):
	clean_tokens = [tok for tok in tokens if len(tok.lower()) > 1 and tok.lower() not in stopwords ]
	
	print(f'total number of raw tokens: {len(tokens)}')
	print(f'total number of stop words: {len(tokens) - len(clean_tokens)}')
	print(f'total number of clean tokens: {len(clean_tokens)}')
	return clean_tokens


def stemmer(clean_tokens):
	return stemmed_tokens


def freq_dist(clean_tokens):
	freq_dist = nltk.FreqDist(clean_tokens)
	# freq_dist = freq_dist.most_common(50)

	# items = [ (v, k) for k, v in freq_dist.items() ]
	most_freq_list = freq_dist

	items = [ (v, k) for k, v in freq_dist.most_common(50) ]
	items.sort()
	items.reverse()
	items = [ (k, v) for v, k in items]

	return items, most_freq_list