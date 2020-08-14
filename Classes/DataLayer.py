import json
import os

from Classes.MysqlDataLayer import MysqlDataLayer
from Validators.Validators import ValidateEmail


class DataLayer:
    mySQL = MysqlDataLayer()

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

    def set_student(self, student):
        """ add student to mongoDB"""
        return DataLayer.mySQL.set_student(student)

    def set_admin(self, admin):
        """appends student to the students internal  dictionary"""
        return DataLayer.mySQL.set_admin(admin)

    def get_student(self, email):
        """get student by email from the internal student dictionary"""
        pass

    def edit_student(self, student):
        pass

    def edit_admin(self, admin):
        pass

    def delete_student(self, email):
        """deletes a user from the internal dictionary by its email"""
        pass

    def get_all_admins(self):
        pass

    def get_all_students(self):
        pass

    def students_json(self):
        students_as_json = json.dumps(self.get_all_students())
        return students_as_json

    def shutdown(self):
        DataLayer.mySQL.shutdown()

    def __str__(self):
        return str(self._students_dictionary)
