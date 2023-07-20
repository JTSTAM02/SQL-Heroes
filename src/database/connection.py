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
    
def update_id_sequence():
    connection = create_connection("postgres", "postgres", "postgres")
    cursor = connection.cursor()

    try:
        # Step 1: Create a temporary table with the desired ID
        desired_id = 7  # Change this to the desired starting ID
        cursor.execute(f"CREATE TEMPORARY TABLE temp_heroes (id SERIAL PRIMARY KEY);")
        cursor.execute(f"INSERT INTO temp_heroes VALUES ({desired_id});")

        # Step 2: Reset the sequence to the temporary table's ID
        cursor.execute("SELECT setval('heroes_id_seq', (SELECT id FROM temp_heroes));")
        connection.commit()
        print(f"The sequence 'heroes_id_seq' has been reset to {desired_id}.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    update_id_sequence()








