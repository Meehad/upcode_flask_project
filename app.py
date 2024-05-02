from flask import Flask, jsonify
import json

app = Flask(__name__)


def load_products_data():
    with open('products.json', 'r', encoding='utf-8') as file:
        return json.load(file)


@app.route('/', methods=['GET'])
def welcome():
    return '<h1>Welcome to our ecommerce website</h1>'


@app.route('/api', methods=['GET'])
def hello():
    return """<h1>This is my api</h1>
    <p>you can use GET /api/products to get details of all products<p>"""


@app.route('/api/products', methods=['GET'])
def get_products():
    data = load_products_data()
    return jsonify(data)

app.run(debug=True)
