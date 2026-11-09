import sqlite3 as sql
import sys
### use * or ** and like args/kwargs or whatever to have one universal add/delete function that changes to fit wherever its used

DATABASE_PATH = 'choir.db'

#style shortcuts
HEADER = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
RESET = '\033[0m'
CARRIAGE_RETURN = '\033[F'
CLEAR_LINE = '\033[2K'

def init_sql(script_path):
    try:
        with open(script_path, "r") as file:
            script = file.read()

        with conn:
            cu.executescript(script)
            print("SQL database created")

    except FileNotFoundError:
        print("Script not found")
    except sql.Error as e:
        print(f"an error occurred: {e}")

def search(table, search_col, search_val):
    # Courtesy of shane:
    cu.execute("SELECT * FROM ? LIMIT 0", (table,)) #selects everything from the table but returns 0 rows (limit 0)
    columns = [desc[0] for desc in cu.description]
    columns.remove(search_col)
    query = f"""
    SELECT *
    FROM ?
    WHERE ? 
    """
#where search_col = search val
    pass
def robes_menu():
    while True:
        all_robes = cu.execute(f"""
        SELECT
            robes.id, students.name FROM robes
            LEFT JOIN students ON robes.student_id = students.id
            WHERE robes.student_id IS NOT 0;             
        """).fetchall()
        print(f"{HEADER}{BOLD}{FAIL}Robes{RESET}".center(17))
        print(f"{BOLD}{UNDERLINE}{BLUE}Robe Id    ".ljust(12) + f"Owner             {RESET}".ljust(17))
        for i in all_robes:
            print(f"{i[0]}".ljust(12) + f"{i[1]}".ljust(17))

        print(f"\n{BOLD}{UNDERLINE}{BLUE}Option        id{RESET}")
        print("Change Owners".ljust(14) + "1".ljust(2) + "\n" + "Search Robes".ljust(14) + "2".ljust(2) + "\n" + "Quit".ljust(14) + "0".ljust(2) + "\n")
        user_choice = input(f"Enter an option id >>> ")
        match user_choice:
            case "1":
                assign_robes()
            case "2":
                search()
            case "0":
                break
            case _:
                pass

def main_menu():
    while True:

        print(f"\n{HEADER}{BOLD}{FAIL}Main  Menu{RESET}".center(16))
        print(f"{BOLD}{UNDERLINE}{BLUE}Option        id{RESET}")
        print("Robes".ljust(14) + "1".ljust(2) + "\n" + "Students".ljust(14) + "2".ljust(2) + "\n" + "Songs".ljust(14) + "3".ljust(2) + "\n" + "Sheets".ljust(14) + "4".ljust(2)+ "\n" + "Quit".ljust(14) + "0".ljust(2) + "\n")

        user_choice = input(f"Enter an option id >>> ")
        match user_choice:
            case "1":
                robes_menu()
            case "2":
                students_menu()
            case "3":
                songs_menu()
            case "4":
                sheets_menu()
            case "0":
                sys.exit()
            case _:
                pass

def add_sample_data():
    pass

if __name__ == "__main__":
    conn = sql.connect(DATABASE_PATH)
    cu = conn.cursor()

    init_sql('setup.sql')
    main_menu()


""" query for sheets:
SELECT
    sheets.id as Sheet_ID,
    pieces.title as Piece_ID,
    students.name as Owner
FROM sheets
LEFT JOIN pieces ON sheets.piece_id = pieces.id
LEFT JOIN students ON sheets.student_id = students.id
ORDER BY (whatever you want);
"""