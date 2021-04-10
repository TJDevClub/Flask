from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")
	
@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    county = request.form.get("county")
    if not name or not county:
        return render_template("failure.html")
    file = open("registrants.csv", "a", newline="")
    writer = csv.writer(file)
    writer.writerow((name, county))
    file.close()
    return render_template("success.html")