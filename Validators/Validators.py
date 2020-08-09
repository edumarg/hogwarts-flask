import re


class ValidateEmail():
    def __init__(self, email, users):
        self._email = email
        self._users = users

    def validate(self):
        if self._email in self._users:
            print("student was already registered, please use a different email\n")
            return False
        else:
            return True


class ValidateNewStudent:
    def __init__(self, student):
        self._student = student

    def validate_compleate_info(self):
        if ("id" in self._student) and ("first_name" in self._student) and ("last_name" in self._student) \
                and ("email" in self._student) and "current_skills" in self._student \
                and "desier_skills" in self._student:
            return True
        else:
            print("student missing information...")
            return False

    # def validate_type_data(self):
    #     if type(self._student["id"]) == "int" and \
    #             type(self._student["first_name"]) == "string" and \
    #             type(self._student["last_name"]) == "string" and \
    #             type(self._student["email"]) == "string" and \
    #             type(self._student["password"]) == "string" and \
    #             type(self._student["existing_skills"]) == "list" and \
    #             type(self._student["desire_skills"]) == "list":
    #         return True
    #     else:
    #         print("some student data is incorrect, please try again..\n")
    #         return False


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


class ValidatePasswordLen():
    def __init__(self, password):
        super(ValidatePasswordLen, self).__init__()
        self._password = password

    def length_validation(self):
        special_characters = ["*", "<", ">", "!", "@", "#", "$", "%", "^", "&", "(", ")", "{", "}", ":", "|"]
        for character in special_characters:
            if self._password.find(character) >= 0:
                print(
                    f"Please make sure that in your password you use only alphanumerical characters and not special "
                    f"characters {special_characters}\n")
                return False
            else:
                if len(self._password) < 8:
                    print("Please make sure your password is at least 8 Characters long\n")
                    return False
                else:
                    return True


class ValidateEmailFormat():
    def __init__(self, email):
        super(ValidateEmailFormat, self).__init__()
        self._email = email

    def email_format_validation(self):
        test_email = re.fullmatch("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$", self._email)
        if test_email:
            return True

        else:
            print("Please enter a valid email address with the correct format -user@mail.com-\n")
            return False


class NameLastnameValidator():
    def __init__(self, first_name, last_name):
        super(NameLastnameValidator, self).__init__()
        self._first_name = first_name
        self._last_name = last_name

    def validte_first_last_name(self):
        special_characters = ["*", "<", ">", "!", "@", "#", "$", "%", "^", "&", "(", ")", "{", "}", ":", "|", ]
        test_name = re.search("[!@#$%^&()_+={};':\",.<>/?|]", self._first_name.lower())
        test_lastname = re.search("[!@#$%^&()_+={};':\",.<>/?|]", self._last_name.lower())
        if not test_name and not test_lastname:
            return True
        else:
            if test_name:
                print(f"Please make sure your name has no special characters {special_characters}\n")
            elif test_lastname:
                print(f"Please make sure your last name has no special characters {special_characters}\n")
        return False


class ValidateStudentDate():
    def __init__(self, students, date):
        pass
