from flask import Flask, request
# import requests
from flask_cors import CORS
from models.models import employees_details, add_player, single_employee, update_employee_model, delete_employee_by_id

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

@app.route('/update_employee/<int:id>', methods=['PATCH'])
def update_employee(id):
    res = single_employee(id)
    if res:
        data = request.get_json()
        new_name = ""        
        new_salary = None
        if data:
            if data.get('name'):
                new_name = data.get('name')            
            if data.get('salary'):
                new_salary = data.get('salary')
            if new_name and new_salary:
                print(new_name,new_salary)
                res = update_employee_model(id, name=new_name, salary=new_salary)
                return {'message:':res}
            else:
                if new_salary:
                    res= update_employee_model(id, "", salary=new_salary)
                    return {'message:':res}
                else:
                    res = update_employee_model(id, name=new_name, salary=None)
                    return {'message:':res}

@app.route('/delete_employee/<int:id>', methods=['DELETE'])
def delete_employee(id):
    res = delete_employee_by_id(id)
    return {'message':res}

    # data = request.get_json()
    # if data:
    #     name = data.get("name")
    #     department = data.get("department")
    #     salary = data.get("salary")
    # if name and department and salary:


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