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

        self.__mydb.autocommit = False

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
            st.type,
            sk.name,
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
            students_list = []
            if len(students) > 0:
                student_dict = {"_id": "",
                                "firstName": "",
                                "lastName": "",
                                "email": "",
                                "createdOn": "",
                                "lastEdit": "",
                                "currentSkills": {},
                                "desireSkills": {}}

                for student in students:
                    if student[0] != student_dict["_id"]:
                        count = 0
                        student_dict = {"_id": student[0],
                                        "firstName": student[1],
                                        "lastName": student[2],
                                        "email": student[3],
                                        "createdOn": student[4],
                                        "lastEdit": student[5],
                                        "currentSkills": {},
                                        "desireSkills": {}}
                        if student[6] == "Current":
                            student_dict["currentSkills"][student[7]] = student[8]
                        elif student[6] == "Desire":
                            student_dict["desireSkills"][student[7]] = student[8]
                        count += 1
                    elif student[0] == student_dict["_id"]:
                        if student[6] == "Current":
                            student_dict["currentSkills"][student[7]] = student[8]
                        elif student[6] == "Desire":
                            student_dict["desireSkills"][student[7]] = student[8]
                        count += 1
                    if count == 7:
                        students_list.append(student_dict)
            return students_list
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
            self.__mydb.commit()
            admins = cursor.fetchall()
            admins_list = []
            if len(admins) > 0:
                for admin in admins:
                    admin_dict = {"_id": admin[0],
                                  "firstName": admin[1],
                                  "lastName": admin[2],
                                  "email": admin[3],
                                  "password": admin[4],
                                  "createdOn": admin[5],
                                  "lastEdit": admin[6]}
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
                    st.type,
                    sk.name,
                    ms.skill_level
                    FROM magic_skills ms
                    INNER JOIN students s
                    ON s.id = ms.student_id
                    LEFT JOIN skills sk 
                    ON sk.id = ms.skill_id
                    LEFT JOIN skill_type st
                    ON st.id = ms.skill_type_id
                    WHERE email = %s"""
            email = (email,)
            cursor.execute(sql, email)

            student = cursor.fetchall()
            if len(student) > 0:
                student_dict = {"_id": "",
                                "firstName": "",
                                "lastName": "",
                                "email": "",
                                "createdOn": "",
                                "lastEdit": "",
                                "currentSkills": {},
                                "desireSkills": {}}

            for s in student:
                if s[0] != student_dict["_id"]:
                    count = 0
                    student_dict = {"_id": s[0],
                                    "firstName": s[1],
                                    "lastName": s[2],
                                    "email": s[3],
                                    "createdOn": s[4],
                                    "lastEdit": s[5],
                                    "currentSkills": {},
                                    "desireSkills": {}}
                    if s[6] == "Current":
                        student_dict["currentSkills"][s[7]] = s[8]
                    elif s[6] == "Desire":
                        student_dict["desireSkills"][s[7]] = s[8]
                    count += 1
                elif s[0] == student_dict["_id"]:
                    if s[6] == "Current":
                        student_dict["currentSkills"][s[7]] = s[8]
                    elif s[6] == "Desire":
                        student_dict["desireSkills"][s[7]] = s[8]
                    count += 1
                if count == 7:
                    pprint(student_dict)

            return student_dict
        except mysql.connector.Error as error:
            print("Fail to get student by email", format(error))
            self.__mydb.rollback()
            return False
        finally:
            cursor.close()

    def get_admin_by_email(self, email):
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
        """appends admin to the MySQL: DB"""

        cursor = self.__mydb.cursor()
        try:

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
            self.__mydb.start_transaction()
            sql_student = "INSERT INTO students (id, firstName, lastName, email, createdOn, lastEdit) VALUES " \
                          "(%s,%s,%s,%s,%s,%s) "
            val_student = (student["_id"],
                           student["firstName"],
                           student["lastName"],
                           student["email"],
                           student["createdOn"],
                           student["lastEdit"])
            cursor.execute(sql_student, val_student)

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
            self.__mydb.rollback()
            return False
        finally:
            cursor.close()

    def edit_student(self, student, email):
        cursor = self.__mydb.cursor()
        try:
            self.__mydb.start_transaction()
            sql_select = "SELECT id FROM students WHERE email = %s "
            cursor.execute(sql_select, (email,))
            student_id = cursor.fetchone()
            print(student_id[0])

            sql_update_student = "UPDATE students SET firstName = %s, lastName = %s, email = %s, lastEdit= %s" \
                                 " WHERE email= %s"
            values_update_student = (student["firstName"],
                                     student["lastName"],
                                     student["email"],
                                     student["lastEdit"],
                                     email)
            cursor.execute(sql_update_student, values_update_student)

            for (skill, level) in student["currentSkills"].items():
                sql_update_magic_skill_current = "UPDATE magic_skills SET skill_level=%s" \
                                                 " WHERE student_id = %s AND skill_type_id = %s AND skill_id = %s"
                skill_id = check_skill(skill)
                skill_level = level

                values_update_magic_skills_current = (
                    skill_level,
                    student_id[0],
                    1,
                    skill_id
                )
                cursor.execute(sql_update_magic_skill_current, values_update_magic_skills_current)

            for (skill, level) in student["desireSkills"].items():
                sql_update_magic_skill_desire = "UPDATE magic_skills SET skill_level=%s" \
                                                " WHERE student_id = %s AND skill_type_id = %s AND skill_id = %s"
                skill_id = check_skill(skill)
                skill_level = level
                values_update_magic_skills_desire = (
                    skill_level,
                    student_id[0],
                    2,
                    skill_id
                )
                cursor.execute(sql_update_magic_skill_desire, values_update_magic_skills_desire)

            self.__mydb.commit()
            return True
        except mysql.connector.Error as error:
            print("Failed to update record to database rollback: {}".format(error))
            self.__mydb.rollback()
            return False
        finally:
            cursor.close()

    def edit_admin(self, admin, email):
        cursor = self.__mydb.cursor()
        try:
            sql = "UPDATE administrators SET firstName = %s, lastName = %s, email=%s , lastEdit = %s, password = %s " \
                  "WHERE email = %s "
            values = (admin["firstName"],
                      admin["lastName"],
                      admin["email"],
                      admin["lastEdit"],
                      admin["password"],
                      email)
            cursor.execute(sql, values)
            self.__mydb.commit()
            print(cursor.rowcount, "record inserted.")
            return True
        except mysql.connector.Error as error:
            print("Failed to update record to database rollback: {}".format(error))
            self.__mydb.rollback()
            return False
        finally:
            cursor.close()

    def delete_student_by_email(self, email):
        cursor = self.__mydb.cursor()
        try:
            self.__mydb.start_transaction()
            sql_select = f"SELECT id FROM students WHERE email = %s"
            cursor.execute(sql_select, (email,))
            student_id = cursor.fetchone()[0]
            print("student_id", student_id)
            sql_delete_student = f"DELETE FROM students WHERE email = %s"
            cursor.execute(sql_delete_student, (email,))
            sql_delete_magic_kill = f"DELETE FROM magic_skills WHERE student_id = %s"
            cursor.execute(sql_delete_magic_kill, student_id)
            self.__mydb.commit()
            print(cursor.rowcount, "record deleted.")
            return cursor.rowcount
        except mysql.connector.Error as error:
            print("Failed to delete record from database table: {}".format(error))
            self.__mydb.rollback()
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
