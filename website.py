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

@app.route("/python")
def python():
    return render_template("python.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/python-intro')
def python_intro():
    return render_template('python_intro.html')

@app.route('/variables')
def variables():
    return render_template('variables.html')

@app.route('/datatypes')
def datatypes():
    return render_template('datatypes.html')

@app.route('/operators')
def operators():
    return render_template('operators.html')

@app.route('/input-output')
def input_output():
    return render_template('input_output.html')

@app.route('/if-else')
def if_else():
    return render_template('if_else.html')

@app.route("/conditions")
def conditions():
    return render_template("conditions.html")

@app.route("/loops")
def loops():
    return render_template("loops.html")

@app.route("/functions")
def functions():
    return render_template("functions.html")

@app.route('/list')
def list_page():
    return render_template('list.html')

@app.route("/tuples")
def tuples():
    return render_template("tuples.html")

@app.route("/dictionary")
def dictionary():
    return render_template("dictionary.html")

@app.route("/sets")
def sets():
    return render_template("sets.html")

@app.route("/strings")
def strings():
    return render_template("strings.html")

@app.route("/modules")
def modules():
    return render_template("modules.html")

@app.route('/visitor-info', methods=['POST'])
def visitor_info():

    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    print(name,email,message)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)