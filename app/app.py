import requests
import os
import json

from flask import Flask, render_template, request
from markdown import markdown

APP_DIR = os.path.dirname(os.path.realpath(__file__))
SITE_WIDTH = 800

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    search_query = request.args.get('search_query')
    request_url = "http://api.giphy.com/v1/gifs/search?q={}&api_key=dc6zaTOxFJmzC&limit=1".format(search_query)
    if search_query:
        response = requests.get(request_url)
        json_data = json.loads(response.content)
        embed_url = str([n['images']['fixed_height']['url'] for n in json_data['data']]).strip('[]\'').lstrip('u\'')
        return render_template('base.html', image=embed_url)
    else:
        return render_template('base.html')



def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()