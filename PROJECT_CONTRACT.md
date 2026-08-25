# Farmer Market Decision Assistant
## Project Contract

## 1. Technology Stack

Frontend:
- HTML5
- CSS3
- JavaScript

Backend:
- Python
- Flask

API:
- REST API

Communication:
- HTTP

Data Format:
- JSON

Database:
- MySQL

Database Language:
- SQL


## 2. Project Structure

farmer-market-decision-assistant/

├── app.py
├── database.py
├── requirements.txt
├── PROJECT_CONTRACT.md
├── README.md
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   └── results.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
├── database/
│   └── schema.sql
│
├── ml/
│   └── price_prediction.py
│
└── tests/


## 3. API Endpoints

POST /api/register
POST /api/login

GET /api/crops
GET /api/markets

POST /api/recommend

GET /api/history


## 4. Standard Function Names

### Authentication

register_user()
login_user()

### Database

get_user()
create_user()
get_crops()
get_markets()
get_market_prices()
save_recommendation()

### Calculation

calculate_gross_revenue()
calculate_transport_cost()
calculate_wastage_cost()
calculate_net_realization()

### Recommendation

rank_markets()
get_best_market()
generate_recommendation()


## 5. Standard Variables

crop
quantity
location
quality
market_price
distance
transport_cost
wastage_cost
gross_revenue
net_realization


## 6. Database Tables

users
crops
markets
market_prices
recommendations


## 7. Core Formula

Gross Revenue:

Quantity × Market Price

Transport Cost:

Distance × Cost Per Kilometer

Wastage Cost:

Gross Revenue × Wastage Percentage

Net Realization:

Gross Revenue
- Transport Cost
- Wastage Cost


## 8. JSON Request

POST /api/recommend

{
    "crop": "Tomato",
    "quantity": 500,
    "location": "Chennai",
    "quality": "A"
}


## 9. JSON Response

{
    "recommended_market": "Market B",
    "market_price": 28,
    "gross_revenue": 14000,
    "transport_cost": 1800,
    "wastage_cost": 280,
    "net_realization": 11920
}


## 10. Team Rules

1. Never push directly to main.
2. Work only on assigned branches.
3. Pull before starting work.
4. Do not create duplicate functions.
5. Do not rename agreed functions.
6. Do not rename agreed API endpoints.
7. Do not change database names without discussion.
8. Do not create duplicate files.
9. Commit meaningful changes.
10. Create a Pull Request before merging.
11. Test before pushing.
12. Do not commit passwords or API keys.
13. Changes to the project contract must be approved by the Project Architect.
