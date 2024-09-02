from flask import Flask, request, jsonify, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

GOOGLE_SEARCH_URL = "https://www.google.com/search?q="

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    search_url = GOOGLE_SEARCH_URL + query.replace(' ', '+')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(search_url, headers=headers)

    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for g in soup.find_all(class_='tF2Cxc'):
        title = g.find('h3').text
        link = g.find('a')['href']
        results.append({'title': title, 'link': link})

    return jsonify({'results': results})

if __name__ == '__main__':
    app.run(debug=True)
