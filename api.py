from flask import Flask, json, request
from Classes.Administrator import Administrator
from Classes.DataLayer import DataLayer
from Classes.Student import Student
from flask_cors import CORS
import atexit

app = Flask(__name__)
cors = CORS(app)


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
@app.route("/students/<email>")
def get_student_by_email(email):
    student = datalayer.get_student(email)
    response = app.response_class(response=json.dumps(student), status=200,
                                  mimetype="application/json")
    return response


# GET count of students with specific skills
@app.route("/skills/current")
def get_specific_skill():
    skill = request.args.get("skill")
    count = datalayer.get_students_by_current_skill(skill)
    response = app.response_class(response=json.dumps(count), status=200, mimetype="application/json")
    return response


# GET count of students with desired skill
@app.route("/skills/desire")
def get_desire_skills():
    skill = request.args.get("skill")
    count = datalayer.get_students_by_desire_skill(skill)
    response = app.response_class(response=json.dumps(count), status=200, mimetype="application/json")
    return response


# GET count students per day
@app.route("/students/createdOn")
def get_student_count_specific_day():
    date = request.args.get("date")
    new_date = date.replace("_", "/")
    count = datalayer.get_student_count_by_creteated_date(new_date)
    response = app.response_class(response=json.dumps(count), status=200, mimetype="application/json")
    return response


# POST new student
@app.route("/students/new", methods=["POST"])
def add_new_student():
    student = request.json
    new_student = Student(student["_id"], student["firstName"], student["lastName"], student["email"],
                          student["createdOn"], student["lastEdit"])
    if datalayer.set_student(student):
        response = app.response_class(response="students successfully added", status=200,
                                      mimetype='application/json')
    elif not datalayer.set_student(student):
        response = app.response_class(response="student already on database", status=405,
                                      mimetype='application/json')
    return response


# POST new admin
@app.route("/admins/new", methods=["POST"])
def add_new_admin():
    admin = request.json
    new_admin = Administrator(admin["id"], admin["firstName"], admin["lastName"], admin["email"], admin["password"])
    if datalayer.set_admin(admin):
        response = app.response_class(response=json.dumps(admin), status=200, mimetype='application/json')
    elif not datalayer.set_admin(admin):
        response = app.response_class(response="Admin already in data Base", status=405, mimetype='application/json')
    return response


# POST login admin
@app.route("/login", methods=["POST"])
def login_student():
    pass


# EDIT student
@app.route("/students/<email>", methods=["PUT"])
def edit_student(email):
    student = request.json
    if "_id" in student:
        del student["_id"]
    datalayer.edit_student(student)
    response = app.response_class(response="Student Edited successfully", status=200, mimetype='application/json')
    return response


# EDIT admin
@app.route("/admins/<email>", methods=["PUT"])
def edit_admin(email):
    admin = request.json
    if "_id" in admin:
        del admin["_id"]
    datalayer.edit_admin(admin)
    response = app.response_class(response="Admin Edited successfully", status=200, mimetype='application/json')
    return response


# DELETE student
@app.route("/students/<email>", methods=["DELETE"])
def delete_student(email):
    datalayer.delete_student(email)
    response = app.response_class(response="Student deleted successfully", status=200, mimetype='application/json')
    return response


# Persist dictionary on file:
@app.route("/students/persist")
def persist_students():
    datalayer.persist_students()
    response = app.response_class(response="Data Persisted", status=200,
                                  mimetype="application/json")
    return response


@app.route("/admins/persist")
def persist_admins():
    datalayer.persist_admins()
    response = app.response_class(response="Data Persisted", status=200,
                                  mimetype="application/json")
    return response


# Backup mongodb
@app.route("/backup")
def backup_db():
    datalayer.backup_mongodb()
    response = app.response_class(response=json.dumps("backup ok"), status=200, mimetype="application/json")
    return response


# Close connection with MongoDB at exit
@atexit.register
def close_connection():
    datalayer.shutdown()


if __name__ == "__main__":
    datalayer = DataLayer()
    # datalayer.load_students()
    # datalayer.load_admins()
    app.run()
