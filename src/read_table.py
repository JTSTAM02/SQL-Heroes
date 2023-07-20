from psycopg2 import errors  # imported to help with catching errors
from database.connection import execute_query

def read_table():
    table_name = input("Enter the name of the table you want to view: ")
    query = f"SELECT * FROM {table_name};"
    result, success = execute_query(query)
    
    if success:
        if result is not None:
            for row in result:
                # loops through each row as a tuple and converts data into a string and then joins it together
                print(", ".join(str(value) for value in row))

if __name__ == "__main__":
    read_table()
