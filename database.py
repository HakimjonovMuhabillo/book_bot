import sqlite3


def create_users_table():
    database = sqlite3.connect('bron.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,    
    chat_id INT,
    name TEXT,
    date TEXT,
    time INT,
    number_of_people INT
    )
    ''')


# create_users_table()

def tables():
    database = sqlite3.connect('bron.db')
    cursor = database.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tables(
    table_id INTEGER PRIMARY KEY AUTOINCREMENT,
    num_of_table TEXT,
    Is_available BOOL DEFAULT FALSE
    )
    ''')


# tables()


def insert_into_tables():
    database = sqlite3.connect('bron.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO tables(num_of_table) VALUES
    ('1'),
    ('2'),
    ('3'),
    ('4'),
    ('5'),
    ('6')
    ''')
    database.commit()
    database.close()


# insert_into_tables()


def insert_data(chat_id, name, date, time, number_of_people):
    database = sqlite3.connect('bron.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO users(chat_id, name, date, time, number_of_people)
    VALUES(?,?,?,?,?)
    ''', (chat_id, name, date, time, number_of_people))
    database.commit()
    database.close()


def cancel_table():
    database = sqlite3.connect('bron.db')
    cursor = database.cursor()
    cursor.execute('''
    DELETE FROM users
    ''')
    database.commit()
    database.close()


def get_booking(chat_id):
    database = sqlite3.connect('bron.db')
    cursor = database.cursor()
    cursor.execute('''
    SELECT * FROM users
    WHERE chat_id = ?
    ''', (chat_id,))
    users = cursor.fetchone()
    database.close()
    return users
