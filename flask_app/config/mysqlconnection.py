import os
import pymysql.cursors
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class MySQLConnection:
    def __init__(self, db):
        connection = pymysql.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        self.connection = connection

    def query_db(self, query, data=None):
        with self.connection.cursor() as cursor:
            try:
                cursor.execute(query, data)
                print("Running Query:", cursor.mogrify(query, data))

                if query.lower().startswith("insert"):
                    self.connection.commit()
                    return cursor.lastrowid
                elif query.lower().startswith("select"):
                    return cursor.fetchall()
                else:
                    self.connection.commit()
            except Exception as e:
                print("Something went wrong", e)
                return False
            finally:
                self.connection.close()

def connectToMySQL(db):
    return MySQLConnection(db)
