# Flask Shopping Site

A modern Flask-based shopping site featuring user authentication, a product catalog, shopping cart, and checkout system. Styled with a sleek Netflix/Takealot-inspired theme.  

**Live Demo:** [Flask Shopping Site on Render](https://flask-shopping-site.onrender.com/)

---

## Features

- User Registration and Login
- Product Listing and Details
- Add to Cart and View Cart
- Checkout System
- Session-based cart management
- Responsive and modern CSS styling

---

## Screenshots

![Home Page](screenshots/home.png)  
![Product Details](screenshots/product.png)  
![Cart](screenshots/cart.png)  
![Checkout](screenshots/checkout.png)  

---

## Technologies Used

- Python 3.x
- Flask 2.3.x
- SQLite3
- HTML / CSS / Jinja2 templates
- Render for deployment

---

## Installation (Local Development)

1. Clone the repository:

```bash
git clone https://github.com/MrHlahle/flask-shopping-site.git
cd flask-shopping-site

Create a virtual environment:
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

Install dependencies:
pip install -r requirements.txt

Initialize the database:
python init_db.py
python create_users_table.py

Run the app:
python app.py

Open http://127.0.0.1:5000
 in your browser.

Deployment

This project is deployed on Render: https://flask-shopping-site.onrender.com/

Future Improvements

Password hashing and security enhancements

Quantity selection in cart

Product images

Order history and user profile pages

Mobile-first responsive design improvements

License

This project is licensed under the MIT License.

👨‍💻 Developer

Obakeng Hlahle
🌐 GitHub Profile https://github.com/MrHlahle/flask-shopping-site/
email obakenghlahle4@gmail.com 
Render link https://flask-shopping-site.onrender.com/