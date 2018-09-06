from app import app

from app.quick_prime import quick_prime
from flask import render_template, request, url_for

from wordcloud import WordCloud
import base64
from io import BytesIO
from PIL import Image


@app.route("/")
def index():
	return render_template('index.html')


# @app.route('/results', methods=['POST'])
@app.route('/results') # "if-the-internet-is-slow-so-local-items" tester
def results():
	# "if-the-internet-is-slow-so-local-items" tester
	word_freq = [ ('hawk',10), ('apple',3), ('spoon',2), ('red',1), ('mine',1) ]
	list_of_tokens = ['hawk','hawk','hawk','hawk','hawk','hawk','hawk','hawk','hawk','hawk','apple','apple','apple','spoon','spoon','red','mine']

	# url = request.form['url']
	# word_freq, list_of_tokens = quick_prime(url)

	text = " ".join(list_of_tokens)

	cloud_PIL = WordCloud(background_color='white').generate(text).to_image()

	# converts cloudPIL from PIL to bytes
	output = BytesIO()
	cloud_PIL.save(output, format='JPEG')

	# converts bytes to base64 encoding minus the "b'"" prexif and "'" suffix
	img = base64.b64encode(output.getvalue())
	img = str(img)[2:-1]

	return render_template('results.html', items=word_freq, img=img)


