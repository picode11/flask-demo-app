# Flask MVC Demo Project

A professional-grade Flask application structure designed for teaching company-level development standards. This project demonstrates MVC architecture, strict separation of concerns, and best practices.

## 🚀 Features

- **MVC Architecture**: Models, Views (Templates), Controllers clearly separated.
- **Flattened Structure**: Modern, accessible project layout.
- **Role-Based Access Control (RBAC)**: Admin and User roles with specific permissions.
- **Blueprints**: Modular routing using Flask Blueprints.
- **Form Validation**: Secure forms using Flask-WTF.
- **Database**: SQLAlchemy ORM with support for SQLite (default) and MySQL.
- **Security**: Password hashing and session management.

## 🛠️ Prerequisites

- Python 3.8+
- MySQL Server (optional, for production/MySQL mode)

## 📦 Installation

1.  **Clone the repository** (if applicable) or navigate to the project folder.

2.  **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment**:
    - Windows:
        ```bash
        venv\Scripts\activate
        ```
    - Mac/Linux:
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## ⚙️ Configuration & Database Setup
Copy the `.env.example` file to create a `.env` file for your local configuration.

### 1. Default Setup (SQLite)
By default, the project is configured to use SQLite, which requires no extra setup.
The `.env` file should look like this:
```ini
SECRET_KEY=your-super-secret-key-change-in-production
DATABASE_URI=sqlite:///app.db
FLASK_ENV=development
```

### 2. MySQL Setup (Recommended for Prod/Learning)

To use MySQL instead of SQLite:

1.  **Install MySQL Server** (e.g., via XAMPP, WAMP, or standalone installer).
2.  **Create a Database**:
    Open your MySQL client (Workbench, phpMyAdmin, or CLI) and run:
    ```sql
    CREATE DATABASE flask_demo_db;
    ```
3.  **Update `.env` file**:
    Change the `DATABASE_URI` to point to your MySQL database.
    
    Format:
    `mysql+pymysql://<username>:<password>@<host>/<database_name>`
    
    Example:
    ```ini
    # .env
    SECRET_KEY=your-secure-secret-key
    
    # Example for local MySQL with root user and no password
    DATABASE_URI=mysql+pymysql://root:@localhost/flask_demo_db
    
    # Example with password 'password123'
    # DATABASE_URI=mysql+pymysql://root:password123@localhost/flask_demo_db
    ```

## ▶️ Running the Application

1.  **Initialize the Database**:
    The application checks for the database on startup and seeds it if empty. Just run the app!

2.  **Start the Server**:
    ```bash
    python run.py
    ```

3.  **Access the App**:
    Open your browser and go to: `http://localhost:5000`

## 🔑 Default Credentials

The application automatically creates these users if they don't exist:

| Role  | Username | Password  | Access Level |
|-------|----------|-----------|--------------|
| **Admin** | `admin`  | `admin123`| Full CRUD access to users |
| **User**  | `user`   | `user123` | View Profile only |

## 📂 Project Structure

```
flask-demo-prj/
├── controllers/      # Business logic (C in MVC)
├── models/           # Database Models (M in MVC)
├── routes/           # URL Routing
├── templates/        # HTML Files (V in MVC)
├── forms/            # Form classes & validation
├── extensions.py     # Flask extensions (DB, Login)
├── config.py         # Configuration loading
├── application.py    # App Factory
├── run.py            # Entry point
└── extensions.py     # Extensions setup
```

## 📝 Teaching Points
- Explain why **Env Variables** are used (Security).
- Show how **Blueprints** separate concerns in `routes/`.
- Discuss **SQLAlchemy** vs writing raw SQL.
- Demonstrate **Template Inheritance** in `templates/layouts/base.html`.
