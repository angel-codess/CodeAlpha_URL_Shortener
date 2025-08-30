from datetime import datetime
import os, random, string
from urllib.parse import urlparse

from flask import Flask, jsonify, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

url_shortener = Flask(__name__)
url_shortener.config.from_object("config.Config")
db = SQLAlchemy(url_shortener)
migrate = Migrate(url_shortener, db)

class URL(db.Model):
    __tablename__ = "urls"
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10), unique=True, nullable=False, index=True)
    long_url = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

def is_valid_url(u: str) -> bool:
    try:
        parsed = urlparse(u)
        return parsed.scheme in ("http", "https") and bool(parsed.netloc)
    except Exception:
        return False

def generate_code(n: int = 7) -> str:
    alphabet = string.ascii_letters + string.digits
    while True:
        cand = "".join(random.choices(alphabet, k=n))
        if not URL.query.filter_by(code=cand).first():
            return cand

@url_shortener.get("/")
def home():
    return render_template("index.html")

@url_shortener.post("/api/shorten")
def api_shorten():
    data = request.get_json(silent=True) or request.form
    long_url = (data.get("url") or "").strip()

    if not long_url:
        return jsonify({"error": "Missing 'url'"}), 400
    if not is_valid_url(long_url):
        return jsonify({"error": "Please provide a valid http(s) URL"}), 400

    existing = URL.query.filter_by(long_url=long_url).first()
    if existing:
        code = existing.code
    else:
        code = generate_code()
        record = URL(code=code, long_url=long_url)
        db.session.add(record)
        db.session.commit()

    short_url = request.host_url.rstrip("/") + "/" + code
    return jsonify({"short_url": short_url, "code": code}), 201

@url_shortener.get("/<code>")
def follow(code: str):
    row = URL.query.filter_by(code=code).first()
    if not row:
        return render_template("index.html", not_found=True, code=code), 404
    return redirect(row.long_url, code=302)

@url_shortener.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    url_shortener.run(debug=True)
