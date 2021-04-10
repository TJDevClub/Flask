import os
import smtplib
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")
	
@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    email = request.form.get("email")
    county = request.form.get("county")
    if not name or not county or not email:
        return render_template("failure.html")
    message = "You are registered!"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("coolcatvas@gmail.com", os.getenv("PASSWORD"))
    server.sendmail("coolcatvas@gmail.com", email, message)
    return render_template("success.html")