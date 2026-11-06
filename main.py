import sqlite3 as sql
### use * or ** and like args/kwargs or whatever to have one universal add/delete function that changes to fit wherever its used

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

def main_menu():
    print(f"{HEADER}{BOLD}{FAIL}{"Main  Menu".center(16)}{RESET}")
    print(f"{BOLD}{UNDERLINE}{BLUE}Option        id{RESET}")
    print("Robes".ljust(14) + "1".ljust(2) + "\n" + "Students".ljust(14) + "2".ljust(2) + "\n" + "Songs".ljust(14) + "3".ljust(2) + "\n" + "Students".ljust(14) + "4".ljust(2)+ "\n" + "Quit".ljust(14) + "0".ljust(2) + "\n")

    while True:
        user_choice = input(f"Enter an option id:")
        match user_choice:
            case "1":
                robes_menu()
            case "2":
                students_menu()
            case "3":
                songs_menu()
            case "4":
                students_menu()
            case "0":
                sys.exit()
            case _:
                pass

def robes_menu():


def add_sample_data():
    pass

if __name__ == "__main__":
    init_sql(':memory:', 'setup.sql')
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