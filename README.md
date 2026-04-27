# 🔐 Vulnerable Web App (Flask)

A simple Flask-based web application intentionally designed with common web vulnerabilities like **SQL Injection** and **Cross-Site Scripting (XSS)** for learning and demonstration purposes.

---

## 🚀 Features

* User Login System
* SQLite Database Integration
* Demonstrates:

  * ❌ SQL Injection Vulnerability
  * ❌ XSS Vulnerability
* Simple Flask backend
* HTML templates for UI

---

## 🛠️ Tech Stack

* Python (Flask)
* SQLite
* HTML/CSS

---

## 📂 Project Structure

```
vulnerable-web-app-flask/
│
├── app.py              # Main Flask application
├── init_db.py          # Database initialization
├── users.db            # SQLite database
├── requirements.txt    # Dependencies
│
├── templates/          # HTML files
│   ├── login.html
│   ├── dashboard.html
│   └── comments.html
│
└── screenshots/        # Project screenshots
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Jay225110/vulnerable-web-app-flask.git
cd vulnerable-web-app-flask
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python app.py
```

---

## 🔑 Default Credentials

```
Username: admin
Password: admin
```

---

## ⚠️ Disclaimer

> This project is created **for educational purposes only**.
> Do NOT use this code in production environments.

---

## 📌 Future Improvements

* Add secure version (fix vulnerabilities)
* Implement authentication best practices
* Use ORM (like SQLAlchemy)
* Add input validation & sanitization

---

## 👤 Author

* GitHub: https://github.com/Jay225110

---

⭐ If you found this useful, consider giving a star!
