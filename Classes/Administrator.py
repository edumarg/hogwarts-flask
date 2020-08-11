import json

from Classes.Person import Person


class Administrator(Person):
    def __init__(self, _id, firstName, lastName, email, password, ):
        super(Administrator, self).__init__(_id, firstName, lastName, email)
        self._id = _id
        self._firstName = firstName
        self._lastName = lastName
        self._email = email
        self._password = password
        self._admin = {"id": self._id, "firstName": self._firstName, "lastName": self._lastName,
                       "email": self._email, "password": self._password}

    def __str__(self):
        """Print json string"""
        return json.dumps(self._admin)

    @classmethod
    def from_json(cls, admin):
        return cls(json.loads(admin))
