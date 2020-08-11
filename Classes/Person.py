class Person:
    def __init__(self, _id, firstName, lastName, email, createdOn, lastEdit):
        self._id = _id
        self._firstName = firstName
        self._lasName = lastName
        self._email = email
        self._createdOn = createdOn
        self._lastEdit = lastEdit

    def get_email(self):
        return self._email
