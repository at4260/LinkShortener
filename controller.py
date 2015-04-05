from flask import Flask, render_template, redirect, request, flash, g
from flask import session as f_session
from flask.ext.wtf import Form


app = Flask(__name__)
app.secret_key = "key"


@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/create")
def home_page():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
