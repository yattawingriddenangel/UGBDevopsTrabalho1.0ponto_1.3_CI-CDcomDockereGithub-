import os
import pymysql
from flask import Flask, jsonify

app = Flask(__name__)


def conectar():
    return pymysql.connect(
        host=os.getenv("DB_HOST", "db"),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        database=os.getenv("DB_NAME", "app"),
        connect_timeout=3,
    )


@app.route("/")
def home():
    return jsonify(mensagem="API no ar!")


@app.route("/visitas")
def visitas():
    try:
        conn = conectar()
        with conn.cursor() as cur:
            cur.execute(
                "CREATE TABLE IF NOT EXISTS visitas ("
                "id INT AUTO_INCREMENT PRIMARY KEY, "
                "criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
            )
            cur.execute("INSERT INTO visitas () VALUES ()")
            conn.commit()
            cur.execute("SELECT COUNT(*) FROM visitas")
            total = cur.fetchone()[0]
        conn.close()
        return jsonify(visitas=total)
    except Exception as e:
        return jsonify(erro=str(e)), 500