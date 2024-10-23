import os
import subprocess

def flask_db_menu():
    while True:
        print("\nFlask DB Commands Menu:")
        print("I - Initialize DB for migrations (only once)")
        print("M - Generate migration scripts (when models change)")
        print("U - Apply migration updates to database")
        print("Q - Quit")
        
        choice = input("\nChoose an option: ").lower()

        if choice == 'i':
            print("\nRunning: Initialize migration directory")
            run_flask_command("init")
        elif choice == 'm':
            print("\nRunning: Generate migration scripts")
            run_flask_command("migrate")
        elif choice == 'u':
            print("\nRunning: Apply migration updates to the database")
            run_flask_command("upgrade")
        elif choice == 'q':
            print("Quitting...")
            break
        else:
            print("Invalid choice. Please select I, M, U, or Q.")

def run_flask_command(command):
    try:
        # Ensure the FLASK_APP environment variable is set
        os.environ['FLASK_APP'] = "app.py"
        
        # Set the working directory to the project root where app.py is located
        os.chdir('/Users/bradyespey/Projects/GitHub/PoGO')  # <-- Change to your project root

        # Run the appropriate Flask command
        subprocess.run(["flask", "db", command], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    flask_db_menu()