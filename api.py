from flask import Flask

from Classes.DataLayer import DataLayer
from Classes.Student import Student

app = Flask(__name__)


@app.before_first_request("/students")
def populate_internal_student_dictionary():
    datalayer = DataLayer()
    datalayer.load_students()


# GET students
@app.route("/students")
def get_students():
    pass


# GET student by email
@app.route("/students/<email>")
def get_student_by_email(email):
    pass


# GET count desired skill
@app.route("/skills/desire")
def get_desire_skills():
    pass


# GET count of students with specific skills
@app.route("/skills/<skill>")
def get_specific_skill(skill):
    pass


# GET students per day
@app.route("/students/day")
def get_studetn_specific_day():
    pass


# POST new student
@app.route("/students/<student_id>", methods=["POST"])
def add_new_student(student_id):
    pass


# POST login student
@app.route("/students/login", methods=["POST"])
def login_student():
    pass


# EDIT student
@app.route("/students/<student_id>", methods=["PUT"])
def edit_student(student_id):
    pass


# DELETE student
@app.route("/students/<student_id>", methods=["DELETE"])
def delete_student(student_id):
    pass


if __name__ == "__main__":
    # app.run()
    add_new_student = Student(id=1, first_name="Edu", last_name="Marg", email="edu@mail.com", password="1234",
                              existing_skills={}, desire_skills={})
    print(add_new_student)
