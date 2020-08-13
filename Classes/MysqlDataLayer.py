import mysql.connector
from decouple import config


class MysqlDataLayer:

    def __connect(self):
        self.__mydb = mysql.connector.connect(
            host="localhost",
            user=config('MYSQL_USER'),
            passwd=config('PASSWORD'),
            database=config('DB')
        )

        self.__mydb.autocommit = True

    def __init__(self):
        super().__init__()
        self.__connect()

    def set_admin(self, admin):
        """appends student to the students internal  dictionary"""
        cursor = self.__mydb.cursor()
        try:
            # self.__mydb.start_transaction()
            sql = "INSERT INTO administrators (id, firstName, lastName, email, password, createdOn, lastEdit) VALUES " \
                  "(%s,%s, %s, %s, %s, %s, %s) "
            val = (admin["_id"],
                   admin["firstName"],
                   admin["lastName"],
                   admin["email"],
                   admin["password"],
                   admin["createdOn"],
                   admin["lastEdit"])
            cursor.execute(sql, val)
            print(cursor.rowcount, "record inserted.")
            return cursor.rowcount
        except mysql.connector.Error as error:
            print("Failed to update record to database rollback: {}".format(error))
        finally:
            cursor.close()

    def set_student(self, admin):
        """appends student to the students internal  dictionary"""
        pass

    def shutdown_db(self):
        self.__mydb.close()
