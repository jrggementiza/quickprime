from app import app

from app.quickprime import test
from flask import render_template, request, url_for, redirect


@app.route("/")
def index():
	return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
	url = request.form['url']
	item = test(url)
	return render_template('results.html', item=item)