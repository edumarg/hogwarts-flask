class BaseDBLayer:
    def __init__(self):
        pass

    def __connect(self):
        pass

    def shutdown(self):
        pass

    def get_all_students(self):
        pass

    def get_all_admins(self):
        pass

    def get_student_by_email(self, email):
        pass

    def get_admin_by_email(self, email):
        pass

    def add_student(self, student):
        pass

    def add_admin(self, admin):
        pass

    def edit_student(self, student):
        pass
    
    def edit_admin(self, admin):
        pass

    def delete_student_by_email(self, email):
        pass
