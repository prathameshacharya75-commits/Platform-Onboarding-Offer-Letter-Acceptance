
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

employee = {
    "name": "",
    "designation": "",
    "salary": "",
    "joining_date": "",
    "status": "Pending",
    "onboarding": "Not Started"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/admin")
def admin():
    return render_template("admin.html", employee=employee)

@app.route("/add_employee", methods=["POST"])
def add_employee():

    employee["name"] = request.form["name"]
    employee["designation"] = request.form["designation"]
    employee["salary"] = request.form["salary"]
    employee["joining_date"] = request.form["joining_date"]
    employee["status"] = "Pending"
    employee["onboarding"] = "Not Started"

    return redirect("/offer")

@app.route("/offer")
def offer():
    return render_template("offer.html", employee=employee)

@app.route("/decision", methods=["POST"])
def decision():

    employee["status"] = request.form["decision"]

    if employee["status"] == "Accepted":
        return redirect("/onboarding")

    return redirect("/offer")

@app.route("/onboarding")
def onboarding():
    return render_template("onboarding.html", employee=employee)

@app.route("/complete", methods=["POST"])
def complete():

    employee["onboarding"] = "Completed"

    return redirect("/admin")

if __name__ == "__main__":
    app.run(debug=True)
