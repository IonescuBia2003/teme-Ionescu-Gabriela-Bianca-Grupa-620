from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

def init_data():
    with app.app_context():
        
        if not Product.query.first():
            product1 = Product(name='Pix', price=10.99)
            product2 = Product(name='Stilou', price=20.99)
            product3 = Product(name='Carte', price=25.99)
            product4 = Product(name='Penar', price=50.99)
            product5 = Product(name='Ghiozdan', price=99.99)

            db.session.add_all([product1, product2, product3, product4, product5])
            db.session.commit()


with app.app_context():
    db.create_all()
    init_data()

@app.route('/products', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    product_list = [f"{product.name}: {product.price} RON" for product in products]
    return '<br>'.join(product_list)


if __name__ == '__main__':
    
    app.run(debug=True)
