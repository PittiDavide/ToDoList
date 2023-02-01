from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import sqlite3
from flask import request

app = Flask(__name__)
CORS(app)


@app.route('/tasks', methods=["GET"])
def task_list():
    con = sqlite3.connect("taskdb.db")
    cur = con.cursor()
    cur.execute("""
    SELECT * FROM tasks
    """)

    res = cur.fetchall()

    out = [
        {
            "id": task[0],
            "content": task[1],
            "done": bool(task[2]),
        }
        for task in res
    ]
    return jsonify(out)


@app.route('/tasks/<int:id>')
def task_details(id):
    con = sqlite3.connect("taskdb.db")
    cur = con.cursor()
    cur.execute("""
    SELECT * FROM tasks WHERE id = ?
    """, (id,))

    out = cur.fetchone()
    return {
        "data": out,
        "ok": True
    }

@app.route('/tasks/<int:id>', methods=["DELETE"])
def task_delete(id):
    con = sqlite3.connect("taskdb.db")
    cur = con.cursor()
    cur.execute("""
    DELETE FROM tasks WHERE id = ?
    """, (id,))
    con.commit()
    return {
        "ok": True
    }

@app.route('/tasks', methods=["POST"])
def task_create():
    con = sqlite3.connect("taskdb.db")
    cur = con.cursor()
    cur.execute("""
    INSERT INTO tasks(content,done) VALUES(?,false) returning id
    """, (request.json["content"],))
    out = cur.fetchone()
    con.commit()

    return {
        "id": out[0],
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
