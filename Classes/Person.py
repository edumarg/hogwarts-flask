class Person:
    def __init__(self, id, first_name, last_name, email, password):
        self._id = id
        self._first_name = first_name
        self._las_name = last_name
        self._email = email
        self._password = password

    def get_email(self):
        return self._email
