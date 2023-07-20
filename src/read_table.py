from psycopg2 import errors # imported to help with catching errors
from database.connection import execute_query

def read_table():
    table_name = input("Enter the name of the table you want to view: ")
    query = f"SELECT * FROM {table_name};"

    try:
        result = execute_query(query)
        if result:
            columns = [desc[0] for desc in result.description]
            print(", ".join(columns))
            for row in result:
                # loops through each row as a tuple and converts data into a string and then joins it together
                print(", ".join(str(value) for value in row)) 
    except errors.UndefinedTable:
        print(f"The '{table_name}' table does not exist. Please try again.")

if __name__ == "__main__": # ensures run when called
    read_table()
