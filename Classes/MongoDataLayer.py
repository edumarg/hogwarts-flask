import pymongo


class MongoDataLayer:
    def __create(self):
        self.__client = pymongo.MongoClient("http://localhost/", 27017)
        self.__students_db = self.__client["students"]
        self.__admins_db = self.__sclient["admins"]

    def __init__(self):
        self.__create()

    def get_all_students(self):
        pass

    def get_all_admins(self):
        pass

    def get_student_by_email(self, email):
        pass

    def get_admin_by_email(self, email):
        pass
