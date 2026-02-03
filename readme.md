# 📝 Flask Notes App

A simple yet scalable **Notes Management Web Application** built with Flask.  
It supports user authentication, note creation/deletion, and database migrations.  
Frontend is powered by Jinja2 templates with Bootstrap styling and JavaScript interactivity.

---

## 🚀 Features
- **User Authentication**: Secure login & signup using Flask‑Login.
- **Database**: SQLite with SQLAlchemy ORM.
- **Migrations**: Managed via Flask‑Migrate for smooth schema updates.
- **Dynamic Templates**: Jinja2 for rendering pages with server‑side logic.
- **Frontend Styling**: Bootstrap components with custom JavaScript for interactivity.
- **Notes Management**: Add, view, and delete notes tied to user accounts.

---

## 🛠️ Tech Stack
- **Backend**: Flask, Flask‑SQLAlchemy, Flask‑Login
- **Database**: SQLite
- **Migrations**: Flask‑Migrate
- **Frontend**: Jinja2, Bootstrap, JavaScript

---

## 📂 Project Structure
flask-notes-app/ │ └── instance/ ├── database.db |  ├── website/ │   ├── init.py        # App factory & DB setup │   ├── models.py          # SQLAlchemy models (User, Note) │   ├── views.py           # Routes for notes & homepage │   ├── auth.py            # Authentication routes │   └── templates/         # Jinja2 HTML templates │       ├── base.html │       ├── home.html │ └──sign_up.html       └── login.html │ ├── static/         # CSS, JS, Bootstrap assets │   └── index.js │  ├── migrations/         # Flask-Migrate migration files ├── main.py                # Entry point ├── Pipfile / requirements.txt └── README.md

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/SDsalima/flask-notes-app.git
   cd flask-notes-app

-----

## Initializing database
flask --app main db init
flask --app main db migrate -m "Initial migration"
flask --app main db upgrade