#мдель это спец класс наследующийся от базового класса
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base() #Инициализация

class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=40), unique=True)

class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(length=40), unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"), nullable=False)

    publisher = relationship(Publisher, backref="book")

class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=25), unique=True)

class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=True)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=True)
    count = sq.Column(sq.Integer)

    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="stock")

class Sale(Base):
    __tablename__= "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Integer, nullable=True)
    date_sale = sq.Column(sq.DATE, nullable=True)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=True)
    count = sq.Column(sq.Integer)

    stock = relationship(Stock, backref="stock")


def find_author():
    author = input("Введите фамилию автора: ")
    q = session.query(Publisher).join(Book.publisher).join(Stock.book).join(Stock.shop).join(Sale.stock).join(Shop)


def create_tables(engine):
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)







