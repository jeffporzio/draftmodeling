from getpass import getpass
from mysql.connector import connect, Error

insert = """
INSERT into test 
(name, number)
VALUES
    ("John Smith", 1),
    ("Jane Smith", 2)
"""

getAll = """
SELECT * FROM draft.test
"""

try:
    with connect(
        host="localhost",
        user="pythonUser",
        password="password",
        database="draft"
    ) as connection:
        print("Connected!")
        with connection.cursor() as cursor: 
            # cursor.execute(insert)
            # connection.commit()
            cursor.execute(getAll)
            result = cursor.fetchall()
            for row in result:
                print(row)
except Error as e:
    print(e)
