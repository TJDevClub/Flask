from flask import Flask, render_template, request, redirect
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
    return redirect("/registrants")
    
@app.route("/registrants")
def registrants():
    file = open("registrants.csv", "r")
    reader = csv.reader(file)
    children = []
    for row in reader:
        children.append(row)
    return render_template("registrants.html", students=children)