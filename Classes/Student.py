from Classes.Person import Person
import json


class Student(Person):
    def __init__(self, _id, firstName, lastName, email, currentSkills={},
                 desireSkills={}):
        super(Student, self).__init__(_id, firstName, lastName, email)
        self._id = _id
        self._firstName = firstName
        self._lastName = lastName
        self._email = email
        self._currentSkills = currentSkills
        self._desireSkills = desireSkills
        self._student = {"_id": self._id, "firstName": self._firstName, "lastName": self._lastName,
                         "email": self._email, "currentSkills": self._currentSkills,
                         "desireSkills": self._desireSkills}

    def __str__(self):
        """Print json string"""
        return json.dumps(self._student)

    # def add_existing_skill(self, skill):
    #     self._currentSkills.append(skill)
    #
    # def add_desire_skill(self, skill):
    #     self._desireSkills.append(skill)

    @classmethod
    def from_json(cls, student):
        return cls(json.loads(student))
