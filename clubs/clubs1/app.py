from flask import Flask, redirect, render_template, request

app = Flask(__name__)

# Registrants
students = []

@app.route("/")
def index():
	return render_template("index.html")
	
@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    county = request.form.get("county")
    if not name or not county:
        return render_template("failure.html")
    students.append(f"{name} from {county}")
    return redirect("/registrants")
    
@app.route("/registrants")
def registrants():
    return render_template("registrants.html", students=students)