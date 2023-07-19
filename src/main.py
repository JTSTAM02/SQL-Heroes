import psycopg2
from database.connection import execute_query, create_connection

execute_query("SELECT * FROM Heroes;")

def create_hero():
    # Prompt the user for hero details
    name = input("Enter the hero's name: ")
    about_me = input("Enter a short description about the hero: ")
    biography = input("Enter the hero's biography: ")
    query = "INSERT INTO heroes (name, about_me, biography) VALUES (%s, %s, %s)"
    params = (name, about_me, biography)
    execute_query(query, params)
    print("Hero created successfully!")


execute_query(create_hero())