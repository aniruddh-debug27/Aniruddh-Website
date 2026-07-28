#a = input("Enter Your Name:")
#b = int(input("Enter Your Age:"))
#c = input("Enter Your City:")
#d = input("Enter Your State:")
#e = input("Enter Your Country:")
#f = input("Enter Your Email:")
#g = input("Enter Your Phone Number:")
#h = input("Enter Your Gender:")
#i = input("Enter Your Occupation:")
#j = input("")
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hero")
def hero():
    return render_template("hero.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)