from flask import Flask, json, escape, request
from Classes.DataLayer import DataLayer
from Classes.Skill import Skill
from Classes.Student import Student

app = Flask(__name__)


# GET before first request student.json file
@app.before_first_request
def before_first_request_func():
    students = datalayer.load_students()
    return students


# GET students
@app.route("/students")
def get_students():
    data = students
    response = app.response_class(response=json.dumps(data), status=200, mimetype="application/json")
    return response


# GET student by email
@app.route("/students/<email>")
def get_student_by_email(email):
    student = datalayer.get_student(email)
    response = app.response_class(response=json.dumps(student), status=200, mimetype="application/json")
    return response


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
def get_student_specific_day():
    pass


# POST new student
@app.route("/students/new", methods=["POST"])
def add_new_student():
    student_id = escape(request.form.get("student_id"))
    first_name = escape(request.form.get("first_name"))
    last_name = escape(request.form.get("last_name"))
    email = escape(request.form.get("email"))
    password = escape(request.form.get("password"))
    magic_skill_name = escape(request.form.get("magic_skill_name"))
    magic_skill_level = escape(request.form.get("magic_skill_level"))
    magic_skill = Skill.from_sting(magic_skill_name, magic_skill_level)
    desire_skill_name = escape(request.form.get("desire_skill_name"))
    desire_skill_level = escape(request.form.get("desire_skill_level"))
    desire_skill = Skill.from_sting(desire_skill_name, desire_skill_level)
    student_dict = {"id": f"{student_id}", "first_name": f"{first_name}", "last_name": f"{last_name}",
                    "email": f"{email}", "password": f"{password}", "magic_skill": f"{magic_skill}",
                    "desire_skill": f"{desire_skill}"}
    new_student = Student(student_id, first_name, last_name, email, password)
    datalayer.set_student(student_dict)
    print(datalayer)
    response = app.response_class(response="Student added successfully", status=200, mimetype='application/json')
    return response


# POST login student
@app.route("/students/login", methods=["POST"])
def login_student():
    pass


# EDIT student
@app.route("/students/<student_id>", methods=["PUT"])
def edit_student(student_id):
    pass


# DELETE student
@app.route("/students/<email>", methods=["DELETE"])
def delete_student(email):
    datalayer.delete_student(email)
    print(datalayer)
    response = app.response_class(response="Student deleted successfully", status=200, mimetype='application/json')
    return response


# Persist dictiorany on file:
@app.route("/students/persist")
def persist_data():
    datalayer.persists_students()
    response = app.response_class(response="Data Persisted", status=200,
                                  mimetype="application/json")


if __name__ == "__main__":
    datalayer = DataLayer()
    students = {}
    app.run()
