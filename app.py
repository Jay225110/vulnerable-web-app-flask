from flask import Flask, request, render_template, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"

def get_db():
    return sqlite3.connect("users.db")

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        db = get_db()
        cursor = db.cursor()

        # ❌ SQL Injection Vulnerability
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        result = cursor.execute(query).fetchone()

        if result:
            session["user"] = username
            return redirect("/dashboard")
        else:
            return "Invalid credentials"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template("dashboard.html", user=session["user"])
    return redirect("/")


@app.route("/comment", methods=["GET", "POST"])
def comment():
    if request.method == "POST":
        comment = request.form["comment"]
        return f"User comment: {comment}"  # ❌ XSS vulnerability
    return render_template("comments.html")


if __name__ == "__main__":
    app.run(debug=True)