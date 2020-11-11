class BaseDBLayer:
    def __init__(self):
        pass

    def __connect(self):
        pass

    def shutdown(self):
        pass

    def verify_login(self, user):
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

    def edit_student(self, student, email):
        pass

    def edit_admin(self, admin, email):
        pass

    def delete_student_by_email(self, email):
        pass

    def get_student_count_by_creteated_date(self, date):
        pass

    def get_students_by_current_skill(self, skill):
        pass

    def get_students_by_desire_skill(self, skill):
        pass
