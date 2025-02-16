# EcoWaste - AI-Powered E-Waste Management Platform

EcoWaste is an AI-powered, end-to-end e-waste management platform that automates collection, tracking, recycling, and rewards to encourage sustainable disposal of electronic waste.


## 🛠 Project Structure

### Backend (Python/Flask)

├── app.py                         # Main Flask application file
├── GreenTalk.py                  # Chatbot implementation
├── data.py                       # Data handling utilities
├── setup_database.py             # Database initialization
├── check_database.py             # Database verification
├── recreate_db.py               # Database recreation utility
├── ReciptGenerate.py            # Receipt generation functionality
├── Expiary_Price_Prediction.py   # ML prediction implementation
├── requirements.txt              # Python dependencies


### Machine Learning Models

├── brand_encoder.pkl             # Brand encoding model
├── product_encoder.pkl           # Product type encoding model
├── usage_encoder.pkl            # Usage pattern encoding model
├── fixed_multi_output_model.pkl  # Main prediction model
├── expiry_price_data.csv        # Training data



```

## Setup Instructions

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up MySQL Database:
   - Install MySQL Server if not already installed
   - Create a new database:
     ```sql
     CREATE DATABASE ecowaste;
     ```
   - Update the `.env` file with your MySQL credentials:
     ```
     DATABASE_URL=mysql://username:password@localhost/ecowaste
     SECRET_KEY=your-secret-key
     ```

4. Run the application:
   ```bash
   python app.py
   ```

The server will start at `http://localhost:5000`

## API Endpoints

- `POST /api/register` - Register new user
- `POST /api/login` - Login user
- `GET /api/logout` - Logout user
- `POST /api/predict` - Get predictions for a product
- `GET /api/products` - Get user's product history

## Frontend

The frontend is currently a simple login page. To integrate with the backend:
1. Update the login form to submit to `/api/login`
2. Create additional pages for product prediction and history
3. Use fetch/axios for API calls

## Team Development

1. Always pull latest changes before starting work:
   ```bash
   git pull origin main
   ```

2. Create a new branch for your features:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. After making changes:
   ```bash
   git add .
   git commit -m "Description of changes"
   git push origin feature/your-feature-name
   ```

4. Create a Pull Request on GitHub for review

## Environment Variables

In production, set these environment variables:
- `SECRET_KEY` - Flask secret key
- `DATABASE_URL` - Database connection string (if not using SQLite)
