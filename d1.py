from flask import Flask

d1 = Flask(__name__)

@d1.route("/")
def home():
    return "Helooooooooo !!! and go to about if u want, and ur main job is to multiply two no. "
@d1.route("/about")
def about():
    return "Boss type commands and move to next slide ok go to contact"
@d1.route("/contact")
def contact():
    return "Fucker what are you doing, I think this is kevin whoever is delaying this, go do the multiplication first dumbass"
@d1.route("/multiplication/<int:a>/<int:b>")
def multiplication(a,b):
    return f"AT last broo i am multiplying it for you, now take = {a*b}"

if __name__ == "__main__":
    d1.run(debug=True)


    