import mysql.connector
from decouple import config
from Classes.BaseDBLayer import BaseDBLayer
from pprint import pprint


def check_skill(skill):
    if skill == "potionMaking":
        skill_id = 1
    elif skill == "spells":
        skill_id = 2
    elif skill == "quidditch":
        skill_id = 3
    elif skill == "animagus":
        skill_id = 4
    elif skill == "apparate":
        skill_id = 5
    elif skill == "metamorphmagi":
        skill_id = 6
    elif skill == "parseltongue":
        skill_id = 7
    else:
        skill_id = 0
    return skill_id


class MysqlDataLayer(BaseDBLayer):

    def __connect(self):
        self.__mydb = mysql.connector.connect(
            host="localhost",
            user=config('MYSQL_USER'),
            passwd=config('PASSWORD'),
            database=config('database')
        )

        # self.__mydb.autocommit = True

    def __init__(self):
        super().__init__()
        self.__connect()

    def get_all_students(self):
        cursor = self.__mydb.cursor()
        print("Get all students")
        try:
            sql = """SELECT 
            s.id,
            s.firstName,
            s.lastName,
            s.email,
            s.createdOn,
            s.lastEdit,
            sk.name,
            st.type,
            ms.skill_level
            FROM magic_skills ms
            INNER JOIN students s
            ON s.id = ms.student_id
            LEFT JOIN skills sk 
            ON sk.id = ms.skill_id
            LEFT JOIN skill_type st
            ON st.id = ms.skill_type_id"""""
            cursor.execute(sql)
            students = cursor.fetchall()
            pprint(students, )
            students = []


        except mysql.connector.Error as error:
            print("Failed to get Students", format(error))
            return False
        finally:
            cursor.close()

    def get_all_admins(self):
        cursor = self.__mydb.cursor()
        try:
            sql = "SELECT * from administrators"
            cursor.execute(sql)
            admins = cursor.fetchall()
            admins_list = []
            if len(admins) > 0:
                for admin in admins:
                    admin_dict = {"_id": admin[0], "firstName": admin[1], "lastName": admin[2], "email": admin[3],
                                  "password": admin[4], "createdOn": admin[5], "lastEdit": admin[6]}
                    admins_list.append(admin_dict)
            return admins_list
        except mysql.connector.Error as error:
            print("Failed to get admins", format(error))
            return False
        finally:
            cursor.close()

    def get_student_by_email(self, email):
        cursor = self.__mydb.cursor()
        try:
            sql = f"""SELECT s.id,
                    s.firstName,
                    s.lastName,
                    s.email,
                    s.createdOn,
                    s.lastEdit,
                    sk.name,
                    st.type,
                    ms.skill_level
                    FROM magic_skills ms
                    INNER JOIN students s
                    ON s.id = ms.student_id
                    LEFT JOIN skills sk 
                    ON sk.id = ms.skill_id
                    LEFT JOIN skill_type st
                    ON st.id = ms.skill_type_id
                    WHERE s.email = \"{email}\""""
            # value = email
            cursor.execute(sql)
            student = cursor.fetchall()
            pprint(student)

        except mysql.connector.Error as error:
            print("Fail to get student by email", format(error))
            return False
        finally:
            cursor.close()

    def get_admin_by_email(self, email):
        print("admin by email")
        cursor = self.__mydb.cursor()
        try:
            sql = f"SELECT * from administrators WHERE email = \"{email}\""
            cursor.execute(sql)
            admin = cursor.fetchone()
            admin_dict = {"_id": admin[0], "firstName": admin[1], "lastName": admin[2], "email": admin[3],
                          "password": admin[4], "createdOn": admin[5], "lastEdit": admin[6]}

            if admin:
                return admin_dict
            else:
                return False
        except mysql.connector.Error as error:
            print("Failed to get admin by mail", format(error))
            return False
        finally:
            cursor.close()

    def set_admin(self, admin):
        """appends admin to the MySQ: DB"""

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
            self.__mydb.commit()
            print(cursor.rowcount, "record inserted.")
            return True
        except mysql.connector.Error as error:
            print("Failed to update record to database rollback: {}".format(error))
            return False
        finally:
            cursor.close()

    def set_student(self, student):
        """appends student to the MySQ: DB"""

        cursor = self.__mydb.cursor()

        try:
            sql_student = "INSERT INTO students (id, firstName, lastName, email, createdOn, lastEdit) VALUES " \
                          "(%s,%s,%s,%s,%s,%s) "
            val_student = (student["_id"],
                           student["firstName"],
                           student["lastName"],
                           student["email"],
                           student["createdOn"],
                           student["lastEdit"])
            cursor.execute(sql_student, val_student)
            self.__mydb.commit()

            for (skill, level) in student["currentSkills"].items():
                sql_magic_skills = "INSERT INTO magic_skills (student_id,skill_id,skill_type_id, skill_level) VALUES " \
                                   "(%s, %s,%s,%s)"
                skill_id = check_skill(skill)
                skill_level = level

                val_magic_skills_current = (student["_id"],
                                            skill_id,
                                            1,
                                            skill_level
                                            )
                cursor.execute(sql_magic_skills, val_magic_skills_current)
                self.__mydb.commit()

            for (skill, level) in student["desireSkills"].items():
                sql_magic_skills = "INSERT INTO magic_skills (student_id,skill_id,skill_type_id, skill_level) VALUES " \
                                   "(%s, %s,%s,%s) "
                skill_id = check_skill(skill)
                skill_level = level

                val_magic_skills_desire = (student["_id"],
                                           skill_id,
                                           2,
                                           skill_level)
                cursor.execute(sql_magic_skills, val_magic_skills_desire)
                self.__mydb.commit()

            print(cursor.rowcount, "record inserted.")
            return True
        except mysql.connector.Error as error:
            print("Failed to update record to database rollback: {}".format(error))
            return False
        finally:
            cursor.close()

    def edit_student(self, student):
        pass

    def edit_admin(self, admin):
        pass

    def delete_student_by_email(self, email):
        cursor = self.__mydb.cursor()

        try:
            sql_select = f"SELECT id FROM students WHERE email =\"{email}\""
            cursor.execute(sql_select)
            student_id = cursor.fetchone()[0]
            print("student_id", student_id)
            sql_delete_student = f"DELETE FROM students WHERE email = \"{email}\""
            cursor.execute(sql_delete_student)
            sql_delete_magic_kill = f"DELETE FROM magic_skills WHERE student_id = \"{student_id}\""
            cursor.execute(sql_delete_magic_kill)

            self.__mydb.commit()
            print(cursor.rowcount, "record deleted.")
            return cursor.rowcount


        except mysql.connector.Error as error:
            print("Failed to delete record from database table: {}".format(error))
        finally:
            cursor.close()

    def get_student_count_by_creteated_date(self, date):
        pass

    def get_students_by_current_skill(self, skill):
        pass

    def get_students_by_desire_skill(self, skill):
        pass

    def delete_table(self, table):
        cursor = self.__mydb.cursor()

        try:
            sql_delete_table = f"TRUNCATE TABLE {table}"
            cursor.execute(sql_delete_table)
            self.__mydb.commit()
            print("Table deleted")
        except mysql.connector.Error as error:
            print("Failed to Delete all records from database table: {}".format(error))
        finally:
            cursor.close()

    def shutdown_db(self):
        self.__mydb.close()
