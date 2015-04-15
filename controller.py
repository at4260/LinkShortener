import model

from flask import Flask, render_template, redirect, request, flash, g
from flask.ext.wtf import Form
from model import session as m_session
# from passlib.hash import pbkdf2_sha512
from random import randint


app = Flask(__name__)
app.secret_key = "key"


@app.route("/")
def home_page():
    return render_template("home.html")

@app.route("/create")
def create_link():
    input_link = request.args.get("input_link")
    
    link = m_session.query(model.Link).filter_by(original_link=input_link).first()

    # Checking if link is already in database
    if link is not None:
        shortened_link = link.shortened_link
    else:
        # shortened_link = pbkdf2_sha512.encrypt(
        #     link, salt=b'64', rounds=100000, salt_size=16)
        shortened_link = "http://www.google.com/" + str(randint(0,1000))

        # Checking if shortened link is already in database- possible encryption collisions
        check_shortened_link = m_session.query(model.Link).filter_by(shortened_link=shortened_link).first()
        while check_shortened_link is not None:
            shortened_link = "http://www.google.com/" + str(randint(0,1000))
            check_shortened_link = m_session.query(model.Link).filter_by(shortened_link=shortened_link).first()
        new_link = model.Link(original_link=input_link, shortened_link=shortened_link)
        m_session.add(new_link)
        m_session.commit()          
    return render_template("create.html", shortened_link=shortened_link)


if __name__ == "__main__":
    app.run(debug=True)
