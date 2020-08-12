import json
from datetime import datetime

from Classes.MongoDataLayer import MongoDataLayer
from Validators.Validators import ValidateEmail


class DataLayer:
    mongoDB = MongoDataLayer()

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
        now = datetime.now()
        created_at = now.strftime("%Y/%m/%d")
        student["createdOn"] = created_at
        student["lastEdit"] = created_at
        DataLayer.mongoDB.add_student(student)
        print("save student success\n")

    def set_admin(self, admin):
        """ add admin to mongoDB"""
        now = datetime.now()
        created_at = now.strftime("%Y/%m/%d")
        admin["createdOn"] = created_at
        admin["lastEdit"] = created_at
        DataLayer.mongoDB.add_admin(admin)
        print("save admin success\n")

    def get_student(self, email):
        """get student by email from the internal student dictionary"""
        return (DataLayer.mongoDB.get_student_by_email(email))

    def edit_student(self, student):
        now = datetime.now()
        edited_at = now.strftime("%Y/%m/%d")
        student["lastEdit"] = edited_at
        DataLayer.mongoDB.edit_student(student)

    def edit_admin(self, admin):
        now = datetime.now()
        edited_at = now.strftime("%Y/%m/%d")
        admin["lastEdit"] = edited_at
        DataLayer.mongoDB.edit_admin(admin)

    def delete_student(self, email):
        """deletes a user from the internal dictionary by its email"""
        DataLayer.mongoDB.delete_student_by_email(email)

    def get_all_admins(self):
        return DataLayer.mongoDB.get_all_admins()

    def get_all_students(self):
        return DataLayer.mongoDB.get_all_students()

    def get_student_count_by_creteated_date(self, date):
        return DataLayer.mongoDB.get_student_count_by_creteated_date(date)

    def get_students_by_current_skill(self, skill):
        pass

    def get_students_by_desier_skill(self, skill):
        pass

    def students_json(self):
        students_as_json = json.dumps(self.get_all_students())
        return students_as_json

    def shutdown(self):
        DataLayer.mongoDB.shutdown()

    def __str__(self):
        return str(self._students_dictionary)
