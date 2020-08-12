import pymongo
import os

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
            student['_id'] = str(student['_id'])
            students_dict[student["_id"]] = student
        return students_dict

    def get_all_admins(self):
        admins_dict = {}
        admins = self.__db["administrators"].find()
        for admin in admins:
            admin['_id'] = str(admin['_id'])
            admins_dict[admin["_id"]] = admin
        return admins_dict

    def get_student_by_email(self, email):
        student = self.__db["students"].find_one({"email": email})
        student['_id'] = str(student['_id'])
        student_found = Student(student["_id"], student["firstName"], student["lastName"], student["email"],
                                student["createdOn"], student["lastEdit"])
        return student

    def get_admin_by_email(self, email):
        admin = self.__db["administrator"].find_one({"email": email})
        admin['_id'] = str(admin['_id'])
        admin_found = Administrator(admin["_id"], admin["firstName"], admin["lastName"], admin["email"],
                                    admin["createdOn"], admin["lastEdit"], admin["password"])
        return admin_found

    def get_student_count_by_creteated_date(self, date):
        pipeline = [{"$match": {"createdOn": {"$eq": date}}}, {"$count": "count"}];
        count = list(self.__db["students"].aggregate(pipeline))
        if len(count) > 0:
            return count[0]["count"]
        else:
            return 0

    def get_students_by_current_skill(self, skill):
        pipeline = self.__db["students"].aggregate([{"$project": {
            "current": {"$objectToArray": "$currentSkills"}}},
            {"$unwind": "$current"}])
        skill_list = list(pipeline)
        count = 0
        if len(skill_list) > 0:
            for index_id in skill_list:
                if index_id["current"]["k"] == skill:
                    if int(index_id["current"]["v"]) >= 2:
                        count += 1
        return count

    def get_students_by_desire_skill(self, skill):
        print("skill", skill)
        pipeline = self.__db["students"].aggregate([{"$project": {
            "desire": {"$objectToArray": "$desierSkills"}}},
            {"$unwind": "$desire"}])
        skill_list = list(pipeline)
        print("skill_list", skill_list)
        count = 0
        if len(skill_list) > 0:
            for index_id in skill_list:
                if index_id["desire"]["k"] == skill:
                    if int(index_id["desire"]["v"]) >= 2:
                        count += 1
        return count

    def add_student(self, student):
        student_add = self.__db["students"].find_one({"email": student["email"]})
        if not student_add:
            if "_id" in student:
                del student["_id"]
            self.__db["students"].insert(student)
            return True
        if student_add:
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

    def edit_student(self, student):
        return self.__db["students"].update({"email": student["email"]}, student)

    def edit_admin(self, admin):
        return self.__db["administrators"].update({"email": admin["email"]}, admin)

    def delete_student_by_email(self, email):
        student_delete = self.__db["students"].find_one({"email": email})
        if not student_delete:
            return False
        if student_delete:
            self.__db["students"].remove({"email": email})
            return True

    def backup_mongodb(self):
        command = "mongodump --host localhost --port 27017 --db hogwarts --out "
        local_folder = "db_backup"
        os.system(command + local_folder)

    def shutdown(self):
        self.__client.close()
