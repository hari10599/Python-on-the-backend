import psycopg2

def printAll(cursor):
    cursor.execute('select * from games')
    rows = cursor.fetchall()
    for row in rows :
        print(row)

#postgres is running a local container
connection = psycopg2.connect(
            host = 'Krishnas-MacBook-Pro.local',
            database = 'testDB',
            user = 'postgres',
            password = 'postgres',
            port = 5432
)

cursor = connection.cursor()
printAll(cursor)

cursor.execute("insert into games(name) values(%s)", ('God of war',))

printAll(cursor)

connection.commit()
cursor.close()
connection.close()

