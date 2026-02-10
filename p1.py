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
def product(id):
    return f"product id is {id}!"
@app.route("/square/<int:num>")
def square(num):
    return f"square is{num*num}"
@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    return f"add a and b = {a+b}"
@app.route("/work/<name>")
def work(name):
    return f"{name} You think your cute , now stop smilling and laughing and do your work !!!!!"

if __name__ == "__main__":
    app.run(debug=True)
