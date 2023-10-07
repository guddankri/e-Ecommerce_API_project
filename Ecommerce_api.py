from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for products (replace with a database in a real application)
products = [
    {"id": 1, "name": "Product 1", "price": 10.99},
    {"id": 2, "name": "Product 2", "price": 20.49},
]

# Create endpoint for retrieving all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Create endpoint for retrieving a specific product
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product is None:
        return jsonify({"error": "Product not found"}), 
    return jsonify(product)

# Create endpoint for creating a new product
@app.route('/products', methods=['POST'])
def create_product():
    new_product = request.json
    products.append(new_product)
    return jsonify(new_product), 201

# Create endpoint for updating an existing product
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    updated_product = request.json
    for i, product in enumerate(products):
        if product['id'] == product_id:
            products[i] = updated_product
            return jsonify(updated_product)
    return jsonify({"error": "Product not found"}), 

# Create endpoint for deleting a product
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    for i, product in enumerate(products):
        if product['id'] == product_id:
            del products[i]
            return jsonify({"message": "Product deleted"})
    return jsonify({"error": "Product not found"}), 

if __name__ == '__main__':
    app.run(port=5600)