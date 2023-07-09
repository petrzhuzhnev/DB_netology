import os
import psycopg2
from dotenv import load_dotenv
from database import DataBase

if __name__ == "__main__":
    load_dotenv()
    db = os.getenv('DB')
    user = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    database = DataBase()
    with psycopg2.connect(database=db, user=user, password=password) as conn:
        database.delete_table_db(conn)
        database.create_db(conn)
        user = database.add_client(conn)
        database.add_phone(conn, user)
        users = database.find_client(conn, 1)
        print(users)

