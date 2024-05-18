from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host='db',
        user='root',
        password='example',
        database='testdb'
    )
    cursor = conn.cursor()
    cursor.execute("SELECT 'Hello from MySQL!'")
    result = cursor.fetchone()

    return result[0]

if __name__ == "__main__":
    app.run(host='0.0.0.0')