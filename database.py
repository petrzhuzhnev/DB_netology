
class DataBase:
    def delete_table_db(slef, conn):
        with conn.cursor() as cur:
            cur.execute("""
            DROP TABLE phone;
            DROP TABLE users;
            """)

    def create_db(self, conn):
        with conn.cursor() as cur:
            cur.execute("""CREATE TABLE if not exists users (
                            id serial primary key,
                            first_name varchar(30),
                            last_name varchar(30),
                            email varchar(30) unique); 

                            CREATE TABLE if not exists phone (
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
            cur.execute("""INSERT INTO users(first_name, last_name, email)
                        VALUES(%s, %s, %s) returning id""", (first_name, last_name, email))

            return int(cur.fetchone()[0])

    def add_phone(self, conn, client_id):
        phone = int(input('Введите номер телефона пользователя: '))
        with conn.cursor() as cur:
            cur.execute("""INSERT INTO phone(id_user, phone_number)
                            VALUES(%s, %s)""", (client_id, phone))

            conn.commit()

    def change_client(self, conn, client_id, first_name=None, last_name=None, email=None):
        with conn.cursor() as cur:
            req = "UPDATE users SET "

            params = []

            if first_name:
                req += "first_name = %s, "
                params.append(first_name)

            if last_name:
                req += "last_name = %s, "
                params.append(last_name)

            if email:
                req += "email = %s, "
                params.append(email)

            req = req.rstrip(", ")

            req += " WHERE id = %s"
            params.append(client_id)

            cur.execute(req, params)

        conn.commit()

    def change_client_phone(self, conn, client_id, phones=None):
        with conn.cursor() as cur:
            cur.execute("""UPDATE phone
                             SET phone_number = %s
                             WHERE id_user = %s""", (phones, client_id))

            conn.commit()

    def delete_phone(self, conn, client_id, phone):
        with conn.cursor() as cur:
            cur.execute("""DELETE from phone
                            WHERE id_user = %s and phone = %s""", (client_id, phone))

            conn.commit()

    def delete_client(self, conn, client_id):
        with conn.cursor() as cur:
            cur.execute("""DELETE from users
                            where id_user = %s""", (client_id,))

            conn.commit()


    def find_client(self, conn, first_name=None, last_name=None, email=None, phone_number=None):
        with conn.cursor() as cur:
            req = """SELECT first_name, last_name, email, phone_number
                       FROM users JOIN phone ON phone.id_user = users.id
                       WHERE 1=1"""

            params = []

            if first_name: #Если значение None, то мы его не учитываем в конструкции IF
                req += " AND users.first_name = %s"
                params.append(first_name)

            if last_name:
                req += " AND users.last_name = %s"
                params.append(last_name)

            if email:
                req += " AND users.email = %s"
                params.append(email)

            if phone_number:
                req += " AND phone.phone_number = %s"
                params.append(phone_number)

            cur.execute(req, params)
            return cur.fetchall()




















