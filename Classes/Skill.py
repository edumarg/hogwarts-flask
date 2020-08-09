import json


class Skill:
    def __init__(self, name, level):
        self._name = name
        self._level = level
        self._skill = {}

    def __str__(self):
        self._skill[self._name] = self._level
        return json.dumps(self._skill)

    @classmethod
    def from_sting(cls, name, level):
        return cls(name=name, level=level)
