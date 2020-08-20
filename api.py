from flask import Flask, json, request, escape
from Classes.Administrator import Administrator
from Classes.DataLayer import DataLayer
from Classes.Student import Student
from flask_cors import CORS
import atexit
from datetime import datetime

app = Flask(__name__)
cors = CORS(app)


def set_creatOn_lastEdid_dates(user):
    now = datetime.now().strftime("%Y/%m/%d")
    user["createdOn"] = now
    user["lastEdit"] = now
    return user


def set_id():
    user_id = datetime.now() - datetime(2019, 4, 13)
    user_id = int((user_id.total_seconds() * 10000 / 50) * 100000)
    return f"{user_id}"


# POST login
@app.route("/login", methods=["POST"])
def verify_login():
    user = request.json
    user["email"] = escape(user["email"].lower())
    user["password"] = escape(user["password"])
    if datalayer.verify_login(user):
        response = app.response_class(response=json.dumps(datalayer.verify_login(user)), status=200,
                                      mimetype="application/json")
    else:
        response = app.response_class(response="", status=200, mimetype="application/json")
    return response


# GET students
@app.route("/students")
def get_students():
    students = datalayer.get_all_students()
    response = app.response_class(response=json.dumps(students), status=200, mimetype="application/json")
    return response


# GET Admins
@app.route("/admins")
def get_admins():
    admins = datalayer.get_all_admins()
    response = app.response_class(response=json.dumps(admins), status=200, mimetype="application/json")
    return response


# GET student by email
@app.route("/students/<string:email>")
def get_student_by_email(email):
    student = datalayer.get_student_by_email(email)
    if student:
        response = app.response_class(response=json.dumps(student), status=200,
                                      mimetype="application/json")
    else:
        response = app.response_class(response="", status=200,
                                      mimetype="application/json")
    return response


# GET admin by email
@app.route("/admins/<string:email>")
def get_admin_by_email(email):
    admin = datalayer.get_admin_by_email(email)
    if admin:
        response = app.response_class(response=json.dumps(admin), status=200, mimetype="application/json")
    else:
        response = app.response_class(response="", status=200, mimetype="application/json")
    return response


# GET count of students with specific skills
@app.route("/skills/current")
def get_specific_skill():
    skill = escape(request.args.get("skill"))
    count = datalayer.get_students_by_current_skill(skill)
    response = app.response_class(response=json.dumps(count), status=200, mimetype="application/json")
    return response


# GET count of students with desired skill
@app.route("/skills/desire")
def get_desire_skills():
    skill = escape(request.args.get("skill"))
    count = datalayer.get_students_by_desire_skill(skill)
    response = app.response_class(response=json.dumps(count), status=200, mimetype="application/json")
    return response


# GET count students per day
@app.route("/students/createdOn")
def get_student_count_specific_day():
    date = escape(request.args.get("date"))
    new_date = date.replace("_", "/")
    count = datalayer.get_student_count_by_creteated_date(new_date)
    response = app.response_class(response=json.dumps(count), status=200, mimetype="application/json")
    return response


# POST new student
@app.route("/students/new", methods=["POST"])
def add_new_student():
    student = request.json
    student = set_creatOn_lastEdid_dates(student)
    id_string = "S-" + set_id()
    student["_id"] = id_string
    new_student = Student(student["_id"],
                          student["firstName"],
                          student["lastName"],
                          student["email"],
                          student["createdOn"],
                          student["lastEdit"],
                          student["currentSkills"],
                          student["desireSkills"])
    response = ""
    if datalayer.set_student(student):
        response = app.response_class(response="Student added to the database", status=200, mimetype='application/json')
    elif not datalayer.set_student(student):
        response = app.response_class(response="Email already exist on the database", status=200,
                                      mimetype='application/json')
    return response


# POST new admin
@app.route("/admins/new", methods=["POST"])
def add_new_admin():
    admin = request.json
    admin = set_creatOn_lastEdid_dates(admin)
    id_string = "A-" + set_id()
    admin["_id"] = id_string
    new_admin = Administrator(admin["_id"],
                              admin["firstName"],
                              admin["lastName"],
                              admin["email"],
                              admin["createdOn"],
                              admin["lastEdit"],
                              admin["password"])
    response = ""
    if datalayer.set_admin(admin):
        response = app.response_class(response="Admin added to the database", status=200, mimetype='application/json')
    elif not datalayer.set_admin(admin):
        response = app.response_class(response="Email already exist on the database", status=200,
                                      mimetype='application/json')
    return response


# EDIT student
@app.route("/students/<string:email>", methods=["PUT"])
def edit_student(email):
    student = request.json
    now = datetime.now().strftime("%Y/%m/%d")
    student["lastEdit"] = now
    if "_id" in student:
        del student["_id"]
    if datalayer.edit_student(student, email):
        response = app.response_class(response="Student Edited successfully", status=200, mimetype='application/json')
    else:
        response = app.response_class(response="Student NOT Edited", status=200, mimetype='application/json')
    return response


# EDIT admin
@app.route("/admins/<email>", methods=["PUT"])
def edit_admin(email):
    admin = request.json
    now = datetime.now().strftime("%Y/%m/%d")
    admin["lastEdit"] = now
    if "_id" in admin:
        del admin["_id"]
    if datalayer.edit_admin(admin, email):
        response = app.response_class(response="Admin Edited successfully", status=200, mimetype='application/json')
    else:
        response = app.response_class(response="Admin NOT Edited", status=200, mimetype='application/json')
    return response


# DELETE student
@app.route("/students/<email>", methods=["DELETE"])
def delete_student(email):
    datalayer.delete_student(email)
    response = app.response_class(response="Student deleted successfully", status=200, mimetype='application/json')
    return response


# Close connection with DB at exit
@atexit.register
def close_connection():
    datalayer.shutdown()


if __name__ == "__main__":
    datalayer = DataLayer()
    app.run()
