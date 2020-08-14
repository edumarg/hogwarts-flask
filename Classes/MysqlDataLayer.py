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
            print(cursor.rowcount, "record inserted.")
            return cursor.rowcount
        except mysql.connector.Error as error:
            print("Failed to update record to database rollback: {}".format(error))
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

            skill_id = 0

            for (skill, level) in student["currentSkills"].items():
                sql_magic_skills = "INSERT INTO magic_skills (student_id,skill_id,skill_type_id, skill_level) VALUES " \
                                   "(%s, %s,%s,%s) "
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
                skill_level = level

                val_magic_skills_desire = (student["_id"],
                                           skill_id,
                                           2,
                                           skill_level)
                cursor.execute(sql_magic_skills, val_magic_skills_desire)

            # self.__mydb.commit()
            print(cursor.rowcount, "record inserted.")
            return cursor.rowcount

        except mysql.connector.Error as error:
            print("Failed to update record to database rollback: {}".format(error))

        finally:
            cursor.close()

    def shutdown_db(self):
        self.__mydb.close()
