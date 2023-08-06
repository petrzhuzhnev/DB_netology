import os

import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import Publisher, Book, Shop, Stock, Sale, create_tables
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
DSN = os.getenv('DSN')
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

# сессия
Session = sessionmaker(bind=engine)#связь сесси с движком м сздание класса сессии
session = Session()

# # создание объектов
# js = Publisher(name="Пушкин")
# print(js.id)
# # hw1 = Homework(number=1, description="первое задание", course=js)
# # hw2 = Homework(number=2, description="второе задание (сложное)", course=js)
#
# session.add(js)
# print(js.id)
# session.commit()  # фиксируем изменения
# print(js.id)

def find_shops_by_publisher(publisher_name):
    sales = (
        session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)
        .join(Book.stock)
        .join(Stock.shop)
        .join(Sale.stock)
        .join(Publisher.books)
        .filter(Publisher.name == publisher_name)
        .all()
    )
    return sales


if __name__ == "__main__":
    publisher_name = input("Введите имя издателя: ")
    sales = find_shops_by_publisher(publisher_name)

    if sales:
        print("Название книги | Название магазина | Стоимость покупки | Дата покупки")
        for sale in sales:
            book_title, shop_name, price, date_sale = sale
            print(f"{book_title} | {shop_name} | {price} | {date_sale}")
    else:
        print(f"Покупки книг издателя {publisher_name} не найдены.")


# # запросы
# q = session.query(Course).join(Homework.course).filter(Homework.number == 1)
# print(q)
# for s in q.all():
#     print(s.id, s.name)
#     for hw in s.homeworks:
#         print("\t", hw.id, hw.number, hw.description)
#
# # вложенный запрос
# subq = session.query(Homework).filter(Homework.description.like("%сложн%")).subquery("simple_hw")
# q = session.query(Course).join(subq, Course.id == subq.c.course_id)
# print(q)
# for s in q.all():
#     print(s.id, s.name)
#     for hw in s.homeworks:
#         print("\t", hw.id, hw.number, hw.description)
#
#
# # обновление объектов
# session.query(Course).filter(Course.name == "JavaScript").update({"name": "NEW JavaScript"})
# session.commit()  # фиксируем изменения
#
#
# # удаление объектов
# session.query(Homework).filter(Homework.number > 1).delete()
# session.commit()  # фиксируем изменения
#




