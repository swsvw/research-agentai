import json

from flask import Flask, render_template, request

from tasks.search_task import run_task

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summaries = []
    if request.method == 'POST':
        query = request.form['query']
        run_task(query) 
        with open("science_articles.json") as f:
            summaries = json.load(f)
    return render_template('index.html', summaries=summaries)

if __name__ == '__main__':
    app.run(debug=True)
