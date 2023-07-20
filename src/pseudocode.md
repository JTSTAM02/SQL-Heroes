# SQL Heroes Pseudocode

## MoSCoW
    -Must-Haves: 
        * Connect to Database
        * View Datbase
        * Define functions needed for CRUD
        * Create command line interface for user to perform CRUD   Operations

    -Should-Haves:
        * Specific Python functions for each CRUD

    -Could-Haves:
        * Additional CRUD Operations (> 4)

    -Won't-Haves / Wish:
        * Frontend


## User Stories
    - As a user, I can create my own hero with a name and superpower.
    - As a user, I can read and display the table with all heroes and their info, including mine.
    - As a user, I can update my hero's superpower.
    - As a user, I can delete my hero altogether.



## Procedural

    1. Connect to Database using provided video instructions: https://www.youtube.com/watch?v=m9UWGCnJqm0&list=PLueGNSATcrZvkyb1QVkOvh6CMq4GiU-HA&index=40
    2. View database
    3. Define python functions for each letter of CRUD. (see User Stories and Python)
    4. Write SQL queries for each SQL query (see Python and SQL Results)

## Python (Functional and Object-Oriented)
    -CRUD
        *Create: 
            def create_hero():
                name = input("Enter your hero' name)
                superpower = input("Enter your hero's superpower")
                print("Your hero has been created")
        
        *Read:
             def read_table():
                query = """
                SELECT * FROM Heroes;
                """

                returned_items = execute_query(query).fetchAll
                for item in returned_items:
                    (item[1])
                return returned_items



        * Update:
            def update_my_hero():



        * Delete:
            def delete_hero(hero_id):
                query = "DELETE FROM Heroes WHERE id = %s"
                params = (hero_id)


## SQL (Results)

    CREATE for create_hero():
        - This should ultimately add the hero to the heroes table and include the about me and biography columns.

    READ for read_table() :
        - This should ultimately display all of the data from the table Heroes for my User.

    UPDATE for update_my_hero()
        - This should ultimately allow the user to input their hero's name and then allow them to type in a changed superpower, that will then be changed in the appropriate table.

    DELETE for delete_hero():
        - This should ultimately erase the chosen hero (chosen by ID) and completely rases their entire row of data from the table.

       



