from database.connection import execute_query

def create_hero():
    name = input("Enter the hero's name: ")
    about_me = input("Enter a short description about the hero: ")
    biography = input("Enter the hero's biography: ")
    query = "INSERT INTO heroes (name, about_me, biography) VALUES (%s, %s, %s)"
    params = (name, about_me, biography) # creates tuple
    execute_query(query, params)
    print("Hero created successfully!")

execute_query(create_hero())