from database.connection import execute_query

def read_table():
    query = "SELECT * FROM heroes;"
    result, cursor = execute_query(query)

    if result:
        for row in result:
            print(f"ID: {row[0]}, Name: {row[1]}, About Me: {row[2]}, Biography: {row[3]}")
    else:
        print("No records found in the table.")
        
    read_table()
