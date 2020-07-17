import json

from Classes.Person import Person


class Administrator(Person):
    def __init__(self, id, first_name, last_name, email, password, ):
        super(Administrator, self).__init__(id, first_name, last_name, email, password)
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._password = password
        self._admin = {}

    def __str__(self):
        self._admin["id"] = self._id
        self._admin["first_name"] = self._first_name
        self._admin["last_name"] = self._last_name
        self._admin["email"] = self._email
        self._admin["password"] = self._password
        return json.dumps(self._admin)
