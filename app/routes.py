from app import app

from app.quick_prime import main
from flask import render_template, request, url_for, redirect


@app.route("/")
def index():
	return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
	url = request.form['url']
	items = main(url)
	# print(items)

	return render_template('results.html', items=items)