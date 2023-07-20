# from psycopg2 import connect, OperationalError

# def create_connection(db_name, db_user, db_password, db_host="localhost", db_port="5432"):
#     connection = None
#     try:
#         connection = connect(
#             dbname=db_name,
#             user=db_user,
#             password=db_password,
#             host=db_host,
#             port=db_port,
#         )
#         print("Connection to PostgreSQL DB successful")
#     except OperationalError as e:
#         print(f"The error '{e}' occurred")
#     return connection

# def execute_query(query, params=None):
#     connection = create_connection("postgres", "postgres", "postgres")
#     cursor = connection.cursor()
#     try:
#         if params is not None:
#             cursor.execute(query, params)
#         else:
#             cursor.execute(query)
#         connection.commit()
#         print("Query executed successfully")
#         return cursor.fetchall(), True
#     except Exception as e:
#         print(f"Error: {e}")
#         connection.close()
#         return None, False

from psycopg2 import connect, OperationalError, errors

def create_connection(db_name, db_user, db_password, db_host="localhost", db_port="5432"):
    connection = None
    try:
        connection = connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(query, params=None):
    connection = create_connection("postgres", "postgres", "postgres")
    cursor = connection.cursor()
    try:
        if params is not None:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        if cursor.description is not None: 
            result = cursor.fetchall()
        else:
            result = None

        connection.commit()
        print("Query executed successfully")
        connection.close()
        return result, True 
    except errors.UndefinedTable:
        print("There is not a table with that name. Please check your spelling and try again.")
        connection.close()
        return None, False  
    except Exception as e:
        print(f"Error: {e}")
        connection.close()
        return None, False 
    
