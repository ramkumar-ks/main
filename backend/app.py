from flask import Flask, request
# import requests
from flask_cors import CORS
from models.models import employees_details, add_player

app = Flask(__name__)
CORS(app)

@app.route('/')
def get_employees():
    res = employees_details()
    return res

@app.route('/add_employee', methods=['POST'])
def add_employee():
    data = request.get_json()
    if data:
        id = data.get("id")
        name = data.get("name")
        department = data.get("department")
        salary = data.get("salary")

        if name and department and salary:
            res = add_player(id, name, department, salary)            
            if res:
                return {'result':'Record inserted'}
            else:
                return {'result':'Insertion failed'}

# @app.route('/addUser', methods=['POST'])
# def add_users():
#     all_users = [
#         {
#         "Name": "Ramkumar K S",
#         "Age": 25,
#         "Role": "backend developer"
#         }
#     ]
#     user = request.get_json()
#     print(user)
#     if user:
#         user_name = user.get("Name")
#         age = user.get("Age")
#         role = user.get("Role")
#         if user_name and age and role:
#             all_users.append(user)        
#     return all_users

app.run(debug=True)