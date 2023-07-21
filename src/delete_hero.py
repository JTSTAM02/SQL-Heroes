from database.connection import execute_query

def delete_hero(hero_name):
    query = "SELECT id FROM heroes WHERE LOWER(name) = LOWER(%s)"
    params = (hero_name, )  # comma needed to convert to a tuple
    result = execute_query(query, params)

    if not result[1]:  # Checks the second element of tuple for boolean
        print("Error occurred while looking up the hero.")
        return

    rows = result[0]  # the first element of the tuple is the list of rows

    if rows:
        hero_id = rows[0][0] # Checks the fist elements of both the rows list and the row itself
        delete_query = "DELETE FROM heroes WHERE id = %s"
        delete_params = (hero_id, ) # shows ID of hero to be deleted
        execute_query(delete_query, delete_params)
        print(f"Hero with ID {hero_id} deleted successfully.")
    else:
        print(f"Hero '{hero_name}' not found.")

hero_name_input = input("Type in which hero you would like to delete: ")
delete_hero(hero_name_input)
