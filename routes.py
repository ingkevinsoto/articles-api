from flask import jsonify, request
from app import app
from database import get_db

def dict_from_row(row, columns):
    return dict(zip(columns, row))

@app.route('/articles', methods=['GET'])
def get_articles():
    db = get_db()
    cursor = db.execute("SELECT id, title, content, image_url, autor FROM articles")
    columns = [column[0] for column in cursor.description]
    articles = [dict_from_row(article, columns) for article in cursor.fetchall()]
    return jsonify({'articles': articles})

@app.route('/articles/<int:article_id>', methods=['GET'])
def get_article(article_id):
    db = get_db()
    cursor = db.execute("SELECT id, title, content, image_url, autor FROM articles WHERE id=?", (article_id,))
    columns = [column[0] for column in cursor.description]
    article = cursor.fetchone()
    return jsonify({'article': dict_from_row(article, columns)})

@app.route('/contacts', methods=['POST'])
def add_contact():
    data = request.get_json()
    name = data['name']
    email = data['email']
    phone = data['phone']
    message = data['message']

    db = get_db()
    db.execute("INSERT INTO contacts (name, email, phone, message) VALUES (?, ?, ?, ?)", (name, email, phone, message))
    db.commit()

    return jsonify({'message': 'Contact added successfully'}), 201
