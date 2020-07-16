from Classes.Person import Person
import json


class Student(Person):
    def __init__(self, id, first_name, last_name, email, password, existing_skills=[],
                 desire_skills=[]):
        super(Student, self).__init__(id, first_name, last_name, email, password)
        self._id = id
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._password = password
        self._existing_skills = existing_skills
        self._desire_skills = desire_skills
        self._student = {}

    def __str__(self):
        self._student["id"] = self._id
        self._student["first_name"] = self._first_name
        self._student["last_name"] = self._last_name
        self._student["email"] = self._email
        self._student["password"] = self._password
        self._student["existing_skills"] = self._existing_skills
        self._student["desire_skills"] = self._desire_skills
        return json.dumps(self._student)

    def add_existing_skill(self, skill):
        self._existing_skills.append(skill)

    def add_desire_skill(self, skill):
        self._desire_skills.append(skill)

    @classmethod
    def from_json(cls, data):
        return cls(json.loads(data))
