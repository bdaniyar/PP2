import psycopg2

# Подключение к базе данных
def connect_to_db():
    return psycopg2.connect(
        dbname="snake_db",     # Убедись, что имя совпадает с тем, что ты создал в pgAdmin
        user="postgres",
        password="0507",
        host="localhost",
        port="5432"
    )

# Создание таблиц users и user_scores
def create_users_table():
    conn = connect_to_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(50) UNIQUE,
            level INT DEFAULT 1,
            score INT DEFAULT 0
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_scores (
            id SERIAL PRIMARY KEY,
            user_id INT,
            score INT,
            level INT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Таблицы для пользователей созданы!")

# Вставка нового пользователя
def insert_user(username):
    conn = connect_to_db()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    result = cur.fetchone()

    if result:
        print(f"Пользователь {username} уже существует!")
    else:
        cur.execute("INSERT INTO users (username, level, score) VALUES (%s, %s, %s)",
                    (username, 1, 0))
        conn.commit()
        print(f"Пользователь {username} успешно добавлен!")
    
    cur.close()
    conn.close()

# Получение данных пользователя
def get_user_data(username):
    conn = connect_to_db()
    cur = conn.cursor()

    cur.execute("SELECT id, level, score FROM users WHERE username = %s", (username,))
    result = cur.fetchone()

    if result:
        user_id, level, score = result
        return user_id, level, score
    else:
        return None, None, None

# Добавление записи в историю результатов
def insert_user_score(user_id, score, level):
    conn = connect_to_db()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO user_scores (user_id, score, level)
        VALUES (%s, %s, %s)
    """, (user_id, score, level))

    conn.commit()
    cur.close()
    conn.close()

# Обновление данных пользователя и добавление в историю
def update_user_score(username, score, level):
    conn = connect_to_db()
    cur = conn.cursor()

    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user_id = cur.fetchone()[0]

    cur.execute("""
        UPDATE users
        SET level = %s, score = %s
        WHERE id = %s
    """, (level, score, user_id))

    conn.commit()
    cur.close()
    conn.close()

    # Добавляем запись в user_scores
    insert_user_score(user_id, score, level)

    print(f"Данные пользователя {username} обновлены!")
