import sqlite3
# A4
connect = sqlite3.connect("users.db")
# Рука с ручкой
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users(
    name VARCAHR (100) NOT NULL,
    age INTEGER NOT NULL,
    hobby TEXT
    )
''')
connect.commit()


# CRUD = Create - Read - Update - Delete

def add_user(name_1, age, hobby):
    # cursor.execute(f'INSERT INTO users(name, age, hobby) VALUES("{name}", "{age}", "{hobby}")')
    cursor.execute(
        "INSERT INTO users(name, age, hobby) VALUES (?,?,?)",
        (name_1, age, hobby)
    )
    connect.commit()
    print('Пользователь добавлен!!')

# add_user("Slava", 29, "Плавать!!")

def get_users():
    cursor.execute('SELECT name, age, hobby FROM users')
    # users = cursor.fetchone()
    users = cursor.fetchall()
    # users = cursor.fetchmany(2)
    for user in users:
        print(f'name: {user[0]}, age: {user[1]}, hobby: {user[2]}')

# get_users()

def update_user(row_id, name=None, age=None, hobby=None):
    if name:
        cursor.execute(
            'UPDATE users SET name = ? WHERE rowid = ?',
            (name, row_id)
        )
    elif age:
        cursor.execute(
            'UPDATE users SET age = ? WHERE rowid = ?',
            (age, row_id)
        )
    elif hobby:
        cursor.execute(
            'UPDATE users SET hobby = ? WHERE rowid = ?',
            (hobby, row_id)
        )
    else:
        print('ничего не передано!!!')

    connect.commit()
    print('Пользователь обнавлен!!!')

update_user(name="ROW2", row_id=3)
# get_users()

def delete_user(row_id):
    cursor.execute(f'DELETE FROM users WHERE rowid = "{row_id}"')
    connect.commit()
    print('Пользователь удален')

# delete_user(2)