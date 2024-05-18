# backend/app.py

from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    conn = mysql.connector.connect(
        host='db',
        user='root',
        password='example',
        database='testdb'
    )
    return conn

@app.route('/')
def hello():
    return "Welcome to the To-Do List API!"

@app.route('/todos', methods=['GET'])
def get_todos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, task FROM todos')
    todos = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def create_todo():
    new_task = request.json['task']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO todos (task) VALUES (%s)', (new_task,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'To-Do created!'}), 201

@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    new_task = request.json['task']
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE todos SET task = %s WHERE id = %s', (new_task, id))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'To-Do updated!'})

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM todos WHERE id = %s', (id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'To-Do deleted!'})

if __name__ == "__main__":
    app.run(host='0.0.0.0')