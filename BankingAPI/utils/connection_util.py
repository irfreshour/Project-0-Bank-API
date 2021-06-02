from psycopg2 import connect
from psycopg2._psycopg import OperationalError


def create_connection():
    try:
        conn = connect(
            host='database-1.cpwt7piygmnx.us-east-1.rds.amazonaws.com',
            database='postgres',
            user='postgres',
            password='password',
            port='5432'
        )
        return conn
    except OperationalError as e:
        print(e)


connection = create_connection()
print(connection)
