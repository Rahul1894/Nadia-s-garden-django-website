Nadia's Garden Restaurant Website

A modern restaurant website built with Django, featuring online pizza ordering.

Features

- Dynamic pizza ordering system
- Editing order abilities
- Can order multiple pizza's at same time
- Admin dashboard for restaurant management

Prerequisites

- Python 3.8 or higher
- Django 4.2 or higher
- PostgreSQL (recommended) or SQLite

Installation

1. Clone the repository

git clone https://github.com/Rahul1894/Nadia-s-garden-django-website.git
cd Nadia-s-garden-django-website


2. Create and activate virtual environment

python -m venv venv
# For Windows
venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate


3. Run migrations

python manage.py makemigrations
python manage.py migrate


4. Create superuser

python manage.py createsuperuser


7. Run development server

python manage.py runserver


Visit http://localhost:8000 in your browser.

