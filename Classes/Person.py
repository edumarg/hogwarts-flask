class Person:
    def __init__(self, id, firstName, lastName, email):
        self._id = id
        self._firstName = firstName
        self._lasName = lastName
        self._email = email

    def get_email(self):
        return self._email
