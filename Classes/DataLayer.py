import json
from Classes.MongoDataLayer import MongoDataLayer
from Classes.MysqlDataLayer import MysqlDataLayer
from decouple import config

from Validators.Validators import ValidateEmail


class DataLayer:
    if config("DB") == "MySQL":
        db = MysqlDataLayer()
    else:
        db = MongoDataLayer()

    def __init__(self):
        self._students_dictionary = {}
        self._admins_dictionary = {}

    def email_validation(self, email):
        """Validate that student email does not exists"""
        validate_email = ValidateEmail(email, self._students_dictionary)
        if validate_email.validate():
            return True
        else:
            return False

    def get_all_students(self):
        return DataLayer.db.get_all_students()

    def get_all_admins(self):
        return DataLayer.db.get_all_admins()

    def get_student_by_email(self, email):
        """get student by email from the  students db"""
        return DataLayer.db.get_student_by_email(email)

    def get_admin_by_email(self, email):
        """get admin by email from the db"""
        print("email in data", email)
        return DataLayer.db.get_admin_by_email(email)

    def set_student(self, student):
        """ add student to db"""
        return DataLayer.db.set_student(student)

    def set_admin(self, admin):
        """appends admin to the administrators db"""
        return DataLayer.db.set_admin(admin)

    def edit_student(self, student):
        pass

    def edit_admin(self, admin):
        pass

    def delete_student(self, email):
        """deletes a user from the DB"""
        return DataLayer.db.delete_student_by_email(email)

    def get_student_count_by_creteated_date(self, date):
        pass

    def get_students_by_current_skill(self, skill):
        pass

    def get_students_by_desire_skill(self, skill):
        pass

    def students_json(self):
        students_as_json = json.dumps(self.get_all_students())
        return students_as_json

    def shutdown(self):
        DataLayer.db.shutdown()

    def __str__(self):
        return str(self._students_dictionary)
