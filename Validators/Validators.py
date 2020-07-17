class ValidateNewStudent:
    def __init__(self, student):
        self._student = student

    def validate_compleate_info(self):
        if ("id" in self._student) and ("first_name" in self._student) and ("last_name" in self._student) \
                and ("email" in self._student) and ("password" in self._student) and "existing_skills" in self._student \
                and "desire_skills" in self._student:
            return True
        else:
            print("student missing information...")
            return False

    def validate_type_data(self):
        if type(self._student["id"]) == "int" and \
                type(self._student["first_name"]) == "string" and \
                type(self._student["last_name"]) == "string" and \
                type(self._student["email"]) == "string" and \
                type(self._student["password"]) == "string" and \
                type(self._student["existing_skills"]) == "list" and \
                type(self._student["desire_skills"]) == "list":
            return True
        else:
            print("some student data is incorrect, please try again..\n")
            return False


class ValidateEditStudent:
    def __init__(self, email, students):
        self._email = email
        self._students = students

    def validate_student_exists(self):
        if self._email in self._students:
            return True
        else:
            print("Student does not exist..\n")
            return False
   