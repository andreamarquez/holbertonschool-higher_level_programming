import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

# Function to read data from JSON file
def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to read data from CSV file
def read_csv(file_path):
    products = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert price to float and id to int
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def products():
    # Get query parameters
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    # Determine the source and read data
    if source == 'json':
        products_data = read_json('products.json')
    elif source == 'csv':
        products_data = read_csv('products.csv')
    else:
        # Invalid source
        return render_template('product_display.html', error="Wrong source")

    # Filter by id if provided
    if product_id:
        filtered_products = [product for product in products_data if product['id'] == product_id]
        if not filtered_products:
            # Product not found
            return render_template('product_display.html', error="Product not found")
        products_data = filtered_products

    # Pass data to the template
    return render_template('product_display.html', products=products_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
