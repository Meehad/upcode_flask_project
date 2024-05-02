from flask import Flask, jsonify, request
import json

app = Flask(__name__)

def save_product(data):
    with open('products.json','w', encoding='utf-8') as file:
        json.dump(data,file,indent=4)

def load_products_data():
    with open('products.json', 'r', encoding='utf-8') as file:
        return json.load(file)

@app.route('/', methods=['GET'])
def welcome():
    return '<h1>Welcome to our ecommerce website</h1>'


@app.route('/api', methods=['GET'])
def hello():
    return """<h1>This is my api</h1>
    <p>you can use GET /api/products to get details of all products<p>
    <p>you can use GET /api/products/id to get details of a specific product using id<p>
    <p>you can use POST /api/products to add new product to products<p>
    """


@app.route('/api/products', methods=['GET'])
def get_products():
    data = load_products_data()
    return jsonify(data)

@app.route('/api/products/<int:id>', methods=['GET'])
def get_product(id):
    data = load_products_data()
    product = None
    for d in data:
        if d["id"] == id:
            product = d
            break
    if (product):
        return jsonify(product)
    else:
        (f'product with {id} not found', 404)

@app.route('/api/products',methods=['POST'])
def add_product():
    new_data = request.json
    data = load_products_data()
    data.append(new_data)
    save_product(data)
    return new_data

app.run(debug=True)
