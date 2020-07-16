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

    # def validate_type_data(self):
    #     if type(self._student["id"]) == "int" and \
    #             type(self._student["first_name"]) == "str" and \
    #             type(self._student["last_name"]) == "str" and \
    #             type(self._student["email"]) == "str" and
