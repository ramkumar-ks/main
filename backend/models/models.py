from sqlalchemy import create_engine, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base = declarative_base()

def employees_details():
    query = text("SELECT name, departmentid, salary, empid FROM employees")
    res = fetch_query("select", query)
    print(res)
    return res

def single_employee(id):
    query = f"SELECT name, departmentid, salary FROM employees where empid={id}"
    res = fetch_query("select_one_employee", text(query))
    print(res)
    return res

def update_employee_model(id, name=None, salary=None):
    query = ""
    if name and salary:
        query = f"update employees set name='{name}', salary={salary} where empid={id}"
    else:
        if name:
            query = f"update employees set name='{name}' where empid={id}"
        if salary:
            query = f"update employees set salary={salary} where empid={id}"
    res = fetch_query("update", text(query))
    return res

def add_player(id, name, department, salary):
    if department:
        department_id = f"SELECT departmentid FROM departments where deptname='{department}'"
        res = fetch_query("select_one", text(department_id))
        if res:            
            query = f"INSERT INTO employees (empid, name, departmentid, salary) VALUES ({id}, '{name}', {res[0]}, {salary})"
            res = fetch_query("insert", text(query))
            if res:
                return True
            else:
                return False

def delete_employee_by_id(id):
    query = f"DELETE FROM employees where empid={id}"
    res = fetch_query("delete", text(query))
    return res 

def fetch_query(type, query):
    engine = create_engine("postgresql+psycopg2://postgres:12345@localhost:5432/postgres", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    if 'select' in type:
        # Step 3: Execute the query
        print("tests")
        res = []
        with engine.connect() as connection:
            result = connection.execute(query)
            
            # Step 4: Fetch all results
            if type == 'select':
                rows = result.fetchall()
                
                # Step 5: Iterate and print results
                for row in rows:
                    query_record = {
                        'name': row[0],
                        'department_id': row[1],
                        'salary': row[2],
                        'empid': row[3]
                    }
                    res.append(query_record)
            if type == 'select_one':
                print("test")
                row = result.fetchone()
                query_record = row[0]
                res.append(query_record)
            
            if type == 'select_one_employee':
                row = result.fetchone()                
                query_res = {
                'name':row[0],
                'department_id':row[1],
                'salary':row[2]
                }
                return query_res
    # data = session.query(cricket_players).all()
    if type in ('insert', 'update', 'delete'):
        with engine.connect() as connection:
            result = connection.execute(query)
            connection.commit()
            return True

    session.close()
    return res
