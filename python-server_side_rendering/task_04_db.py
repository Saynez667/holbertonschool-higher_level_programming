from flask import Flask, render_template, request, jsonify
import json
import csv
import sqlite3

app = Flask(__name__)

# Function to fetch data from JSON
def get_data_from_json():
    try:
        with open('products.json', 'r') as file:
            data = json.load(file)
            return data.get("items", [])
    except FileNotFoundError:
        return []

# Function to fetch data from CSV
def get_data_from_csv():
    try:
        with open('products.csv', newline='') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []

# Function to fetch data from SQLite
def get_data_from_sqlite(product_id=None):
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        query = "SELECT id, name, category, price FROM Products"
        
        if product_id:
            query += " WHERE id = ?"
            cursor.execute(query, (product_id,))
        else:
            cursor.execute(query)
        
        products = [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in cursor.fetchall()]
        conn.close()
        return products
    except sqlite3.Error as e:
        return {"error": "Database error: " + str(e)}

# Route to display products
@app.route('/products')
def display_products():
    source = request.args.get('source', '').lower()
    product_id = request.args.get('id')

    if product_id:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template('product_display.html', error="Invalid product ID")

    if source == "json":
        data = get_data_from_json()
    elif source == "csv":
        data = get_data_from_csv()
    elif source == "sql":
        data = get_data_from_sqlite(product_id)
    else:
        return render_template('product_display.html', error="Wrong source")

    if isinstance(data, dict) and "error" in data:
        return render_template('product_display.html', error=data["error"])

    if product_id and not data:
        return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
