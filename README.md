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

## 📸 Screenshots

<img width="1906" height="1006" alt="Screenshot 2026-04-24 074506" src="https://github.com/user-attachments/assets/ba62bf5d-a242-4b21-b213-540a72da14e2" />
<img width="1919" height="1008" alt="Screenshot 2026-04-24 074703" src="https://github.com/user-attachments/assets/5fa6f112-8a53-49c1-8b52-72fdd374d27a" />
<img width="1919" height="1067" alt="Screenshot 2026-04-24 074813" src="https://github.com/user-attachments/assets/a069ad06-c6c9-4db8-85c4-ac4703801b86" />
<img width="1883" height="1028" alt="Screenshot 2026-04-24 074831" src="https://github.com/user-attachments/assets/62ddf2e3-285a-4cb4-bdf7-2bdcc5ee2eed" />

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
