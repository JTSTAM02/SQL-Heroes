from database.connection import execute_query

def create_hero():
    name = input("Enter the hero's name: ")
    about_me = input("Enter a short description about the hero: ")
    biography = input("Enter the hero's biography: ")
    query = "INSERT INTO heroes (name, about_me, biography) VALUES (%s, %s, %s)"
    params = (name, about_me, biography) # creates tuple
    execute_query(query, params)
    print("Hero created successfully!")



def create_superpower():
    superpower = input("What superpower do you want your hero to have? Enter it here: ")
    ability_type_query = "INSERT INTO ability_types (name) VALUES (%s)"
    execute_query(ability_type_query, (superpower, ))

create_hero()
create_superpower()