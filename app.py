#!usr/bin/python3
""" Starts a flask application."""


from flask import Flask, render_template, request, flash


app = Flask(__name__)
app.secret_key = "mynameis"

@app.route("/hello")
def index():
    flash("What's your name?")
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", the world is a better place with you in it!")
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)
