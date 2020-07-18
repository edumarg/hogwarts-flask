import json
import os
from datetime import datetime

from Validators.Validators import ValidateEmail


class DataLayer:
    def __init__(self):
        self._students_dictionary = {}

    def email_validation(self, email):
        """Validate that student email does not exists"""
        validate_email = ValidateEmail(email, self._students_dictionary)
        if validate_email.validate():
            return True
        else:
            return False

    def set_student(self, student):
        """appends student to the students internal  dictionary"""
        email = student["email"]
        self._students_dictionary[f'{email}'] = student
        now = datetime.now()
        created_at = now.strftime("%Y/%M/%d")
        self._students_dictionary[f'{email}']["created_at"] = created_at
        self._students_dictionary[f'{email}']["last_update"] = created_at
        print("save user success\n")

    def get_student(self, email):
        """get student by email from the internal student dictionary"""
        if email not in self._students_dictionary:
            print("student does not exist, please use a different email\n")
            return False
        else:
            return self._students_dictionary[f'{email}']

    def delete_student(self, email):
        """deletes a user from the internal dictionary by its email"""
        if email in self._students_dictionary:
            self._students_dictionary.pop(email, "email not found...")
            print("Student delete successful\n")
        else:
            print("email not found, student was not deleted\n")

    def load_students(self):
        """loads all the users in the json file into the internal dictionary"""
        if os.path.isfile(os.path.join("data", "students.json")):
            try:
                with open(os.path.join("data", "students.json"), "r") as file:
                    data = file.read()
                self._students_dictionary = json.loads(data)
                print("load successful\n")
                return self._students_dictionary
            except IOError:
                print("load failed\n")

        else:
            with open(os.path.join("data", "students.json"), "w+") as file:
                data = json.dumps(self._students_dictionary)
                file.write(data)
            print("load failed because students.json file did not exists and was created\n")

    def persists_students(self):
        """converts the internal dictionary to a json and stores it within the students.json file"""
        data = json.dumps(self._students_dictionary)
        try:
            with open(os.path.join("data", "students.json"), "w+") as file:
                file.write(data)
            print("persist command successful\n")
        except IOError:
            print("persist failed\n")

    def get_all_students(self):
        return self._students_dictionary

    def students_json(self):
        students_as_json = json.dumps(self.get_all_students())
        return students_as_json

    def __str__(self):
        return str(self._students_dictionary)