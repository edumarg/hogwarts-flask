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
        self._student = {"id": self._id, "first_name": self._first_name, "last_name": self._last_name,
                         "email": self._email, "password": self._password, "existing_skills": self._existing_skills,
                         "desire_skills": self._desire_skills}

    def __str__(self):
        """Print json string"""
        return json.dumps(self._student)

    def add_existing_skill(self, skill):
        self._existing_skills.append(skill)

    def add_desire_skill(self, skill):
        self._desire_skills.append(skill)

    @classmethod
    def from_json(cls, student):
        return cls(json.loads(student))
