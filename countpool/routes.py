from countpool import app
from flask import render_template, url_for


@app.route("/", methods=['GET', 'POST'])
@app.route("/home", methods=['GET', 'POST'])
def home():

    return render_template("home.html")
