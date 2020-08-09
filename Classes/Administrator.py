import json

from Classes.Person import Person


class Administrator(Person):
    def __init__(self, id, firstName, lastName, email, password, ):
        super(Administrator, self).__init__(id, id, firstName, lastName, email)
        self._id = id
        self._firstName = firstName
        self._lastName = lastName
        self._email = email
        self._password = password
        self._admin = {}

    def __str__(self):
        self._admin["id"] = self._id
        self._admin["first_name"] = self._firstName
        self._admin["last_name"] = self._lastName
        self._admin["email"] = self._email
        self._admin["password"] = self._password
        return json.dumps(self._admin)
