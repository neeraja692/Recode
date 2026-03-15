from flask import Flask, request, render_template, redirect

app = Flask(__name__)

# Temporary in-memory storage
users = {}  # username -> {name,password,role}

# Admin logs
admin_logs = []

# ---------------- Pages ----------------

@app.route("/")
def home():
    return render_template("coverpage.html")

@app.route("/signup.html")
def signup_page():
    return render_template("signup.html")

@app.route("/login.html")
def login_page():
    return render_template("login.html")

@app.route("/follow.html")
def follow_page():
    return render_template("follow.html")

@app.route("/admin.html")
def admin_page():
    return render_template("admin.html", logs=admin_logs)

# ---------------- Signup ----------------

@app.route("/signup", methods=["POST"])
def signup():

    name = request.form.get("name")
    username = request.form.get("username")
    password = request.form.get("password")
    role = request.form.get("choose")

    if username in users:
        return f"User '{username}' already exists!"

    users[username] = {
        "name": name,
        "password": password,
        "role": role
    }

    # Role based redirect
    if role == "Admin":
        return redirect("/admin.html")

    elif role == "Moderator":
        return redirect("/moderator.html")

    else:
        return redirect("/follow.html")

# ---------------- Login ----------------

@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("name")
    password = request.form.get("password")
    role = request.form.get("choose")

    user = users.get(username)

    if user and user["password"] == password and user["role"] == role:

        if role == "Admin":
            return redirect("/admin.html")

        elif role == "Moderator":
            return redirect("/moderator.html")

        else:
            return redirect("/follow.html")

    else:
        return "Invalid credentials or role mismatch."

# ---------------- Admin Actions ----------------

@app.route("/admin_action", methods=["POST"])
def admin_action():

    action = request.form.get("action")
    admin_logs.append(action)

    return "success"

# ---------------------------------------
@app.route("/moderator.html")
def moderator_page():
    return render_template("moderator.html")

if __name__ == "__main__":
    app.run(debug=True)