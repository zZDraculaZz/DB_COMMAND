import psycopg2

DB = 'shop'
DB_PASSWORD = '14774123dD'

# Присоединение к базе данных.
conn = psycopg2.connect(dbname=DB, user='postgres',
                        password=DB_PASSWORD, host='localhost')
# Создание переменной, которая позволяет взаимодействовать с базой данных.
cursor = conn.cursor()

# выбрать всё из таблицы.
cursor.execute("select * from customer;")

# Извлечение записи таблицы
record = cursor.fetchall()

print(record)

cursor.close()
conn.close()