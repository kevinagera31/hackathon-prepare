from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Home Page"
@app.route("/about")
def about():
    return "About Page"
@app.route("/contact")
def contact():
    return "contact page"
@app.route("/user/<name>")
def user(name):
    return f"hello {name}!"
@app.route("/product/<id>")
def product():
    return f"product id is {id}!"
@app.route("/square/<int:num>")
def square():
    return f"square is{num*num}"

if __name__ == "__main__":
    app.run(debug=True)
