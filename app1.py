from flask import Flask,jsonify
app=Flask(__name__)
@app.route("/api/data")
def get_data():
    return jsonify({"name":"kevin","role":"backend developer","stack":"flask+mysql"})
if __name__=="__main__":
    app.run(debug=True)

