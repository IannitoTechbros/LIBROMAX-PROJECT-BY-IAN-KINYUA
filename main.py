from cli.menu import main_menu
from database.setup import init_db

def main():
    init_db()
    main_menu()

if __name__ == "__main__":
    main()
