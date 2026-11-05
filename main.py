import sqlite3 as sql
### use * or ** and like args/kwargs or whatever to have one universal add/delete function that changes to fit wherever its used

def init_sql(db_path, script_path):
    try:
        with open(script_path, "r") as file:
            script = file.read()

        with sql.connect(db_path) as conn:
            cu = conn.cursor()
            cu.executescript(script)
            print("SQL database created")
    except FileNotFoundError:
        print("Script not found")
    except sql.Error as e:
        print(f"an error occurred: {e}")

if __name__ == "__main__":
    init_sql(':memory:', 'setup.sql')

    test = [
        ("Cooper Hoffman", 11),
        ("Nikhil Konagurthu", 11)
    ]
    with sql.connect('choir.db') as conn:
        cu = conn.cursor()
        conn.commit()