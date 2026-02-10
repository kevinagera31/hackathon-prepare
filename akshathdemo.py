from flask import Flask

app = Flask(__name__)
@app.route("/")
def about():
    return "about page"
@app.route("/contact")
def contact():
    return "contact page"
@app.route("/bottle")
def bottle():
    return "bottle page"
@app.route("/phone/<int:a>/<int:b>")
def phone(a,b):
	return f"value is {a*b}"
@app.route("/square/<int:a>")
def square(a):
    return f"the inputed no is {a} and square of the number is :{a*a}"
   

if __name__ == "__main__":
    app.run(debug=True)
