from countpool import app
from flask import render_template, url_for


@app.route("/.html")
@app.route("/home.html")
def home():

    return render_template("home.html")
