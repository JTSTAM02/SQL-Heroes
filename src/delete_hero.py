import psycopg2
from database.connection import execute_query, create_connection

def deleteHero(hero_id):
    input("Type in which hero you would like to delete.")
    # look up ID of inputted hero
    query = "DELETE FROM Heroes WHERE id = '%s'"
    params = (hero_id, ) # converts to a tuple
    execute_query(query, params)
    print(f"Hero with ID {hero_id} deleted successfully.")

execute_query(deleteHero(hero_id))