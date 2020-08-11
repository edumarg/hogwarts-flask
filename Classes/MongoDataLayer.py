import pymongo

from Classes.Administrator import Administrator
from Classes.Student import Student


class MongoDataLayer:
    def __create(self):
        self.__client = pymongo.MongoClient("localhost", 27017)
        self.__db = self.__client["hogwarts"]

    def __init__(self):
        self.__create()

    def get_all_students(self):
        students_dict = {}
        students = self.__db["students"].find()
        for student in students:
            students_dict[student["_id"]] = student
        return students

    def get_all_admins(self):
        admins_dict = {}
        admins = self.__db["administrators"].find()
        for admin in admins:
            admins_dict[admin["_id"]] = admin
        return admin

    def get_student_by_email(self, email):
        student = self.__db["students"].find({"email": email})
        student_found = Student(student)
        return student_found

    def get_admin_by_email(self, email):
        admin = self.__db["administrator"].find({"email": email})
        admin_found = Administrator(admin)
        return admin_found

    def add_student(self, student):
        student_add = self.__db["students"].find_one({"email": student["email"]})
        if not student_add:
            if "_id" in student:
                del student["_id"]
            return self.__db["students"].insert(student)
        if student_add:
            print("student email already exist")
            return False

    def add_admin(self, admin):
        admin_add = self.__db["administrators"].find_one({"email": admin["email"]})
        if not admin_add:
            if "_id" in admin:
                del admin["_id"]
            return self.__db["administrators"].insert(admin)
        if admin_add:
            print("admin email already exist")
            return False

    def edit_student_by_email(self, student):
        return self.__db["students"].update({"email": student["email"]}, student)

    def edit_admin_by_email(self, admin):
        return self.__db["administrators"].update({"email": admin["email"]}, admin)

    def delete_student_by_email(self, email):
        return self.__db["students"].remove({"email": email})

    def shutdown(self):
        self.__client.close()
