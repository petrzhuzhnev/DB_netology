
class DataBase:
    def delete_table_db(slef, conn):
        with conn.cursor() as cur:
            cur.execute("""
            DROP TABLE phone;
            DROP TABLE users;
            """)

    def create_db(self, conn):
        with conn.cursor() as cur:
            cur.execute("""create table if not exists users (
                            id serial primary key,
                            first_name varchar(30),
                            last_name varchar(30),
                            email varchar(30) unique); 

                            create table if not exists phone (
                            id serial primary key,
                            id_user int not null references users(id),
                            phone_number bigint);          
                            """)
            conn.commit()

    def add_client(self, conn):
        first_name, last_name, email = input("Введите имя пользователя: "), \
            input("Введите фамилию пользователя: "), \
            input("Введите почту пользователя: ")
        with conn.cursor() as cur:
            cur.execute("""insert into users(first_name, last_name, email)
                        values(%s, %s, %s) returning id""", (first_name, last_name, email))
            return int(cur.fetchone()[0])

    def add_phone(self, conn, client_id):
        phone = int(input('Введите номер телефона пользователя: '))
        with conn.cursor() as cur:
            cur.execute("""insert into phone(id_user, phone_number)
                            values(%s, %s);""", (client_id, phone))
            conn.commit()

    def change_client(self, conn, client_id, first_name=None, last_name=None, email=None, phones=None):
        with conn.cursor() as cur:
            cur.execute("""update users
                            set first_name = %s,
                                last_name = %s,
                                email = %s
                            where id = %s;""", (first_name, last_name, email, client_id))
            conn.commit()

    def change_client_phone(self, conn, client_id, phones=None):
        with conn.cursor() as cur:
            cur.execute("""update phone
                             set phone_number = %s
                             where id_user = %s;""", (phones, client_id))
            conn.commit()

    def delete_phone(self, conn, client_id, phone):
        with conn.cursor() as cur:
            cur.execute("""delete from phone
                            where id_user = %s and phone = %s;""", (client_id, phone))
            conn.commit()

    def delete_client(self, conn, client_id):
        with conn.cursor() as cur:
            cur.execute("""delete from users
                            where id_user = %s;""", (client_id,))
            conn.commit()

    def find_client(self, conn, client_id):
        with conn.cursor() as cur:
            cur.execute("""select first_name, last_name, email, phone_number 
                            from users join phone on phone.id_user = users.id
                            where users.id = %s""", (client_id,)
                        )
            return cur.fetchall()
