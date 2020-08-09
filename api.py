from flask import Flask, json, escape, request
from Classes.DataLayer import DataLayer
from Classes.Skill import Skill
from Classes.Student import Student
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)


# GET before first request student.json file
# @app.before_first_request
# def before_first_request_func():
#     students = datalayer.load_students()
#     return students


# GET students
@app.route("/students")
def get_students():
    sudents = datalayer.get_all_students()
    response = app.response_class(response=json.dumps(sudents), status=200, mimetype="application/json")
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
    student = request.json
    print("students from react", student)
    # response = json.dumps(student,
    #                       status=200,
    #                       mimetype='application/json')

    # student_id = student["id"]
    # first_name = student["firstName"]
    # last_name = student["lastName"]
    # email = student["email"]
    # current_skills = student["currentSkills"]
    # desier_skills = student["desierSkills"]
    # student_dict = {"id": f"{student_id}", "firstName": f"{first_name}", "lastName": f"{last_name}",
    #                 "email": f"{email}", "currentSkills": f"{current_skills}",
    #                 "desierSkills": f"{desier_skills}"}
    new_student = Student(student["id"], student["firstName"], student["lastName"], tudent["email"])
    datalayer.set_student(student)
    print("data layer", datalayer)
    # response = app.response_class(response="Student added successfully", status=200, mimetype='application/json')
    response = "OK"


# POST login admin
@app.route("/login", methods=["POST"])
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
    datalayer.load_students()
    app.run()
