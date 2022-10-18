"""
Matthew Hayden
M04 Lab
Creates an API for books.
Variables/Classes:
    class Book(): defines all the things that will be in the database.
        id: the id of the book, must be a primary key.
        book_name: the name of the book, must be unique.
        author: the author of the book.
        publisher: the publisher of the book.
    def get_books(): prints out the data for the different books.
    get get_book(): returns 404 if the id does not exist.
    def add_book(): allows for books to be added using POST.
    def delete_book(): allows for books to be deleted using DELETE.
"""
import tempfile
import os.path
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(tempfile.gettempdir(), 'test.db')
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True,nullable=False)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))

    def __repr__(self):
        return f"{self.book_name} - {self.author} - {self.publisher}"

@app.route('/')
def index():
    return 'Hello!'

@app.route('/books')
def get_books():
    books = Book.query.all()
    output = []
    for book in books:
        book_data={'book_name': book.book_name, 'author':book.author, 'publisher':book.publisher}
        output.append(book_data)
    return{"books": output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {"name":book.book_name,"author":book.author,'publisher':book.publisher}

@app.route('/books',methods=['POST'])
def add_book():
    book = Book(book_name=request.json['book_name'], author=request.json['author'],publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id':book.id}

@app.route('/books/<id>',methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error":"not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message":"Yeet!"}
