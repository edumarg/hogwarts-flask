import json
import os
from datetime import datetime


class DataLayer:
    def __init__(self):
        self._students_dictionary = {}

    def set_student(self, student):
        """appends student to the students dictionary"""
        email = student["email"]
        self._students_dictionary[f'{email}'] = student
        now = datetime.now()
        created_at = now.strftime("%Y/%M/%d")
        self._students_dictionary[f'{email}']["created_at"] = created_at
        self._students_dictionary[f'{email}']["last_update"] = created_at
        print("save user success\n")

    def get_student(self, email):
        """get student by email"""
        if email not in self._students_dictionary:
            print("student does not exist, please use a different email\n")
            return False
        else:
            return self._students_dictionary[f'{email}']

    def delete_student(self, email):
        """deletes a user from the dictionary by its email"""
        if email in self._students_dictionary:
            self._students_dictionary.pop(email, "email not found...")
            print("Student delete successful\n")
        else:
            print("email not found, student was not deleted\n")

    def persists_students(self):
        """converts the dictionary to a json and stores it within the data directory as file"""
        data = json.dumps(self._users_dictionary)
        try:
            with open("students.json", "w+") as file:
                file.write(data)
            print("persist command successful\n")
        except IOError:
            print("persist failed\n")
