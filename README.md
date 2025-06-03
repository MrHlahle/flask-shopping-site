# Flask Shopping Site 🛒

A simple shopping website built using Python Flask.

## Features

- User registration and login
- View product listings and details
- Add to cart and view cart
- Checkout summary
- SQLite database integration
- Clean UI with external CSS

## Tech Stack

- Python (Flask)
- HTML/CSS (Jinja2 templating)
- SQLite (via SQLAlchemy)
- Bootstrap (optional for styling)

## Getting Started

### 🔧 Installation

1. Clone the repo:

   ```bash
   git clone https://github.com/MrHlahle/flask-shopping-site.git
   cd flask-shopping-site
2. Create and activate a virtual environment
   python -m venv venv
venv\Scripts\activate   # on Windows
3. Install dependencies:
   pip install -r requirements.txt
4. Run the app:
   flask run
Visit http://127.0.0.1:5000 in your browser to start shopping!

 Project Structure
 shopping_site/
├── static/
│   └── style.css
├── templates/
│   ├── index.html
│   ├── cart.html
│   ├── login.html
│   ├── register.html
│   ├── product_detail.html
│   └── checkout.html
├── app.py
├── models.py
├── database.db
└── README.md
📌 Author
Obakeng Hlahle
📧 obakenghlahle4a@gmail.com
🔗 GitHub
