from sqlalchemy import create_engine, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base = declarative_base()

def employees_details():
    query = text("SELECT name, departmentid, salary FROM employees")
    res = fetch_query("select", query)
    print(res)
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
                        'salary': row[2]
                    }
                    res.append(query_record)
            if type == 'select_one':
                print("test")
                row = result.fetchone()
                query_record = row[0]
                res.append(query_record)
    # data = session.query(cricket_players).all()
    if type == 'insert':
        with engine.connect() as connection:
            result = connection.execute(query)
            connection.commit()
            return True


    session.close()
    return res
