from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

def read_json(file_path):
    with open(file_path) as file:
        return json.load(file)

def read_csv(file_path):
    with open(file_path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def products():
    source = request.agrs.get('source')
    product_id = request.agrs.get('id')
    products = []
    error_message = None
    
    if source == 'json':
        try:
            products = read_json('products.json')
        except FileNotFoundError:
            error_message = 'JSON File not found'
    elif source == 'csv':
        try:
            products = read_csv('products.csv')
        except FileNotFoundError:
            error_message = 'CSV File not found'
    else:
        error_message = 'Wrong source'

    if not error_message and product_id:
        try:
            product_id = int(product_id)
            products = [product for product in products if product['id'] == product_id]
            if not products:
                error_message = 'Product not found'
        except ValueError:
            error_message = 'Invalid product ID'
        
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
