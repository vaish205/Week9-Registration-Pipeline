
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def register():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def submit():
    name = request.form.get("name", "")
    rollno = request.form.get("rollno", "")
    year = request.form.get("year", "")
    branch = request.form.get("branch", "")

    return render_template(
        "success.html",
        name=name,
        rollno=rollno,
        year=year,
        branch=branch
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
