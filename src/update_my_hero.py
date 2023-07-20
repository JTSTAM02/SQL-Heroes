from database.connection import execute_query

def update_my_hero():
    name = input("Enter the hero's name: ")
    about_me = input("Enter the updated short description about the hero: ")
    biography = input("Enter the updated hero's biography: ")

    query_check_hero = "SELECT id FROM heroes WHERE LOWER(name) = LOWER(%s)"
    params_check_hero = (name, )
    result, success = execute_query(query_check_hero, params_check_hero)

    if not success:
        print("Error occurred while checking the hero.")
        return

    hero_id = result[0][0] if result else None

    if hero_id:
        query_update_hero = "UPDATE heroes SET about_me = %s, biography = %s WHERE id = %s"
        params_update_hero = (about_me, biography, hero_id)
        execute_query(query_update_hero, params_update_hero)

        print(f"Hero with ID {hero_id} updated successfully!")
    else:
        print(f"Hero '{name}' not found.")

if __name__ == "__main__":
    update_my_hero()
