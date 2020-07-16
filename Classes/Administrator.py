from Classes.Person import Person


class Administrator(Person):
    def __init__(self, id, first_name, last_name, email, password, ):
        super(Administrator, self).__init__(id, first_name, last_name, email, password)
