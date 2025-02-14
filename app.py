from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import joblib
import os
from datetime import datetime
import pandas as pd
from dotenv import load_dotenv
import urllib.parse

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key')
# MySQL configuration with URL-encoded password
password = urllib.parse.quote_plus('Mano@123')
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{password}@localhost/ecowaste'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

# Load ML models
try:
    print("Loading ML models...")
    model = joblib.load('clean_multi_output_model.pkl')
    product_encoder = joblib.load('product_encoder.pkl')
    brand_encoder = joblib.load('brand_encoder.pkl')
    usage_encoder = joblib.load('usage_encoder.pkl')
    print("ML models loaded successfully!")
except Exception as e:
    print(f"Error loading ML models: {str(e)}")

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_type = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    usage_pattern = db.Column(db.String(50), nullable=False)
    predicted_expiry = db.Column(db.Float, nullable=False)
    predicted_price = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def home():
    return "EcoWaste API is running!"

@app.route('/api/predict', methods=['POST'])
@login_required
def predict():
    try:
        data = request.json
        
        # Transform input data
        input_data = pd.DataFrame({
            'Product_Type': [product_encoder.transform([data['product_type']])[0]],
            'Brand': [brand_encoder.transform([data['brand']])[0]],
            'Usage_Pattern': [usage_encoder.transform([data['usage_pattern']])[0]]
        })
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Create new product record
        new_product = Product(
            product_type=data['product_type'],
            brand=data['brand'],
            usage_pattern=data['usage_pattern'],
            predicted_expiry=float(prediction[0][0]),
            predicted_price=float(prediction[0][1]),
            user_id=current_user.id
        )
        db.session.add(new_product)
        db.session.commit()
        
        return jsonify({
            'expiry_years': float(prediction[0][0]),
            'current_price': float(prediction[0][1])
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'error': 'Username already exists'}), 400
    
    new_user = User(
        username=data['username'],
        password=data['password'],  # In production, hash the password
        email=data['email']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.password == data['password']:  # In production, verify hashed password
        login_user(user)
        return jsonify({'message': 'Logged in successfully'})
    return jsonify({'error': 'Invalid username or password'}), 401

@app.route('/api/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'})

@app.route('/api/products', methods=['GET'])
@login_required
def get_products():
    products = Product.query.filter_by(user_id=current_user.id).all()
    return jsonify([{
        'id': p.id,
        'product_type': p.product_type,
        'brand': p.brand,
        'usage_pattern': p.usage_pattern,
        'predicted_expiry': p.predicted_expiry,
        'predicted_price': p.predicted_price,
        'created_at': p.created_at.isoformat()
    } for p in products])

if __name__ == '__main__':
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("Database tables created successfully!")
    
    print("\nStarting EcoWaste Server...")
    print("Available routes:")
    print("  - / (GET): Home")
    print("  - /api/predict (POST): Make predictions")
    print("  - /api/register (POST): Register new user")
    print("  - /api/login (POST): Login user")
    print("  - /api/logout (GET): Logout user")
    print("  - /api/products (GET): Get user's product history")
    print("\nServer is running on http://localhost:5000")
    
    app.run(debug=True, port=5000)
