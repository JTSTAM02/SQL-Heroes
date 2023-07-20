from database.connection import execute_query

def delete_hero(hero_name):
    # look up ID of inputted hero

    query = "SELECT id FROM heroes WHERE LOWER(name) = LOWER(%s)"
    params = (hero_name, ) # comma needed to convert to a tuple
    result = execute_query(query, params)
    hero_id = result.fetchone()
    if hero_id:
        hero_id = hero_id[0]
        delete_query = "DELETE FROM Heroes WHERE id = %s"
        delete_params = (hero_id, )
        execute_query(delete_query, delete_params)
        print(f"Hero with ID {hero_id} deleted successfully.")
    else:
        print(f"Hero '{hero_name}' not found.")

hero_name_input = input("Type in which hero you would like to delete: ")
delete_hero(hero_name_input)