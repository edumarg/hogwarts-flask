import json
import os
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
        DataLayer.mongoDB.add_student(student)
        if DataLayer.mongoDB.add_student(student):
            return True
        elif not DataLayer.mongoDB.add_student(student):
            return False
        # """appends student to the students internal  dictionary"""
        # email = student["email"]
        # self._students_dictionary[f'{email}'] = student
        # now = datetime.now()
        # created_at = now.strftime("%Y/%M/%d")
        # self._students_dictionary[f'{email}']["created_at"] = created_at
        # self._students_dictionary[f'{email}']["last_update"] = created_at
        # print("save user success\n")

    def set_admin(self, admin):
        """appends student to the students internal  dictionary"""
        email = admin["email"]
        self._admins_dictionary[f'{email}'] = admin
        now = datetime.now()
        created_at = now.strftime("%Y/%M/%d")
        self._admins_dictionary[f'{email}']["created_at"] = created_at
        self._admins_dictionary[f'{email}']["last_update"] = created_at
        print("admin user success\n")

    def get_student(self, email):
        """get student by email from the internal student dictionary"""
        if email not in self._students_dictionary:
            print("student does not exist, please use a different email\n")
            return False
        else:
            return self._students_dictionary[f'{email}']

    def edit_student(self, student):
        self.get_student(student.email)
        pass

    def delete_student(self, email):
        """deletes a user from the internal dictionary by its email"""
        DataLayer.mongoDB.delete_student_by_email(email)
        
        # if email in self._students_dictionary:
        #     self._students_dictionary.pop(email, "email not found...")
        #     print("Student delete successful\n")
        # else:
        #     print("email not found, student was not deleted\n")

    # def load_admins(self):
    #     """loads all the users in the json file into the internal dictionary"""
    #     if os.path.isfile(os.path.join("data", "admins.json")):
    #         try:
    #             with open(os.path.join("data", "admins.json"), "r") as file:
    #                 data = file.read()
    #             self._admins_dictionary = json.loads(data)
    #             print("load successful\n")
    #             return self._admins_dictionary
    #         except IOError:
    #             print("load failed\n")
    #             return

    # def load_students(self):
    # """loads all the users in the json file into the internal dictionary"""
    # if os.path.isfile(os.path.join("data", "students.json")):
    #     try:
    #         with open(os.path.join("data", "students.json"), "r") as file:
    #             data = file.read()
    #         self._students_dictionary = json.loads(data)
    #         print("load successful\n")
    #         return self._students_dictionary
    #     except IOError:
    #         print("load failed\n")
    #         return
    #
    # else:
    #     with open(os.path.join("data", "students.json"), "w+") as file:
    #         data = json.dumps(self._students_dictionary)
    #         file.write(data)
    #     print("load failed because students.json file did not exists and was created\n")
    #     return

    def persist_students(self):

        """persist the local json file to mongoDB this will be delete after the data was created on mongoDB"""
        if os.path.isfile(os.path.join("data", "students.json")):
            try:
                with open(os.path.join("data", "students.json"), "r") as file:
                    data = file.read()
                self._students_dictionary = json.loads(data)
                print("load successful\n")
                for student in self._students_dictionary:
                    DataLayer.mongoDB.add_student(self._students_dictionary[student])
            except IOError:
                print("load failed\n")
                return

            # """converts the internal dictionary to a json and stores it within the students.json file"""
            # data = json.dumps(self._students_dictionary)
            # try:
            #     with open(os.path.join("data", "students.json"), "w+") as file:
            #         file.write(data)
            #     print("persist command successful\n")
            # except IOError:
            #     print("persist failed\n")

    def persist_admins(self):
        """persist the local json file to mongoDB this will be delete after the data was created on mongoDB"""
        if os.path.isfile(os.path.join("data", "admins.json")):
            try:
                with open(os.path.join("data", "admins.json"), "r") as file:
                    data = file.read()
                self._admins_dictionary = json.loads(data)
                print("load  admins successful\n")
                for admin in self._admins_dictionary:
                    DataLayer.mongoDB.add_admin(self._admins_dictionary[admin])
            except IOError:
                print("load failed\n")
                return

    def get_all_admins(self):
        admin_list = []
        for email in self._admins_dictionary:
            admin_list.append(self._admins_dictionary[email])
        return admin_list

    def get_all_students(self):
        students_list = []
        for email in self._students_dictionary:
            students_list.append(self._students_dictionary[email])
        return students_list

    def students_json(self):
        students_as_json = json.dumps(self.get_all_students())
        return students_as_json

    def shutdown(self):
        DataLayer.mongoDB.shutdown()

    def __str__(self):
        return str(self._students_dictionary)
