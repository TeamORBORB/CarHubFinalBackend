from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/dealerships", methods=["GET"])
def get_dealerships():
    conn = sqlite3.connect('dealerships.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dealerships")
    rows = cursor.fetchall()
    conn.close()
    
    dealerships = []
    for row in rows:
        dealership = {
            "id": row[0],
            "name": row[1],
            "address": row[2],
            "latitude": row[3],
            "longitude": row[4]
        }
        dealerships.append(dealership)
    
    return jsonify(dealerships)

if __name__ == '__main__':
    app.run(debug=True)
