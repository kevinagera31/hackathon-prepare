from flask import Flask,jsonify
import mysql.connector
app=Flask(__name__)
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="chickachickaslimshady",
        database="flask_test"
    )
@app.route("/api/data")
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(users)
if __name__=="__main__":
    app.run(debug=True)

