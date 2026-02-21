import pickle
import os
import time
from police import *

def emulate_load():
            time.sleep(0.3)
            print("|")
            time.sleep(0.3)
            print("/")
            time.sleep(0.3)
            print("—")
            time.sleep(0.3)
            print("\\")
            time.sleep(0.3)
            print("|")
            time.sleep(0.3)
            print("/")
            time.sleep(0.3)
            print("—")
            time.sleep(0.3)
            print("\\")
            time.sleep(0.3)
            print("|")


def main():
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)

    data_files = {
        "police.pkl":       Police(),
        "applications.pkl": [], 
        "history.pkl":      [],
        "citizens.pkl":     [],
        "laws.pkl":         [],
        "security.pkl":     Security()
    }

    loaded = {}

    for filename, default in data_files.items():
        path = os.path.join(data_dir, filename)
        try:
            with open(path, "rb") as f:
                loaded[filename] = pickle.load(f)
            print(f"Loaded: {filename}")
        except (FileNotFoundError, EOFError, pickle.UnpicklingError) as e:
            print(f"Failed to load {filename}: {type(e).__name__}")
            loaded[filename] = default

    police          = loaded["police.pkl"]
    applications    = loaded["applications.pkl"]
    history         = loaded["history.pkl"]
    citizens        = loaded["citizens.pkl"]
    laws            = loaded["laws.pkl"]
    security        = loaded["security.pkl"]

    def write_statement():
            try:
                description = input("Write was happend: ")

                zone = input("What zone?: ")

                i = 0
                for citizen in citizens:
                    print(f"{i} - {citizen}")
                    i += 1
                
                selected_citizen = int(input("Choose accused"))
                suspect = citizens[selected_citizen]

                print("What law was broken?:")
                i = 0
                for law in laws:
                    print(f"{i} - {law}")
                    i += 1
                
                selected_law = int(input("Choose law"))
                law = laws[selected_law]
                
                application = Crime(suspect=suspect, description=description, zone=zone, law=law)
                applications.append(application)

                emulate_load()

                history.append(f"The police report about {application.suspect} was successfully filed")
                print(f"The police report about {application.suspect} was successfully filed")

            except Exception as e:
                    print(f"Error: {e}")

    def delete_statement():
        try:
            i = 0
            for application in applications:
                print(f"{i} - {application}")
                i += 1

            application_index = int(input("Choose application: "))
            applications.pop(application_index)
            
            history.append(f"Appliaction was successfully deleted")
        except Exception as e:
            print(f"Error: {e}")

    def show_statements():
        try:
            for application in applications:
                print(f"{application}\n")

        except Exception as e:
            print(f"Error: {e}")

    def add_citizen():
        try:
            name = input("Enter citizen's name: ")
            citizen = Citizen(name=name)
            citizens.append(citizen)

            history.append(f"Citizen was successfully added")
            print("Citizen was successfully added")
        
        except Exception as e:
            print(f"Error: {e}")

    def delete_citizen():
        try:
            i = 0
            for citizen in citizens:
                print(f"{i} - {citizen}")
                i += 1

            citizen_index = int(input("Choose citizen: "))
            citizens.pop(citizen_index)
            
            history.append(f"Citizen was successfully deleted")
        except Exception as e:
            print(f"Error: {e}") 

    def show_citizens():
        try:
            for citizen in citizens:
                print(f"{citizen}\n")

        except Exception as e:
            print(f"Error: {e}")

    def add_policeman():
        lastname = input("Enter policeman lastname: ")
        zone = input("Enter working zone: ")
        policeman = Policeman(lastname=lastname, zone=zone)
        police.hire(policeman=policeman, zone=zone)

        history.append(f"Policeman {policeman._lastname} hired to police")
        print(f"Policeman {policeman._lastname} hired to police")

    def add_zone():
        new_zone = input("Enter new zone: ")
        police.add_zone(new_zone=new_zone)

    def show_policemen():
        policemen = police.get_policemen()
        for policeman in policemen:
            print(policeman)

    def show_info():
        if not police._zones:
            print("No zones registered.")
            return

        for zone_id, data in sorted(police._zones.items(), key=lambda x: int(x[0]) if x[0].isdigit() else x[0]):
            print(f"\n{'='*40}")
            print(f"Zone {zone_id}")
            print(f"{'='*40}")
            print(f"  Policemen: {len(data['policemen'])}")
            for policeman in data["policemen"]:
                print(f"    - {policeman}")
            print(f"  Crimes: {len(data['crimes'])}")
            for crime in data["crimes"]:
                print(f"    - {crime}")
            print(f"  Security level: {data['security']}")

    def relocate_policemen():
        policemen = police.get_policemen()

        print("All policemen:")
        i = 0
        for policeman in policemen:
            print(f"{i} - {policeman}\n")
            i += 1

        indexes = input("Select policemen you want to relocate(example: <1 3 7>): ")
        try:
            relocated_policemen = [policemen[int(index)] for index in indexes.split()]
        except ValueError:
            print("Invalid input: all values must be integers")
            relocated_policemen = []

        new_zone = input("Enter new zone: ")
        police.relocate(relocated_policemen=relocated_policemen, target_zone=new_zone)
            
    while True:
        print(
            """ 
            Choice option:
            1 - Statement options
            2 - History settings
            3 - Police options
            4 - Civil options
            5 - Law options
            6 - Exit
            """)
        choice = int(input())


#-----------------------------------------OPTION 1------------------------------------#
        

        if choice == 1:
                
            print(
                """
                1 - Write statement
                2 - Delete statement
                3 - Show statements
                4 - Back
                """)
            choice = int(input())

            if choice == 1:
                write_statement()

            elif choice == 2:
                delete_statement()

            elif choice == 3:
                show_statements()

            elif choice == 4:
                continue

            else:
                raise ValueError("Incorrect option")
                

#-----------------------------------------OPTION 2---------------------------------------#


        elif choice == 2:
            print(
                """
                1 - Show history
                2 - Clean history
                3 - Back
                """)

            choice = int(input())

            if choice == 1:
                if not history:
                    print("History is empty")
                else:
                    for h in history:
                        print(f"{h}\n")

            elif choice == 2:
                history.clear()

            elif choice == 3:
                continue

            else:
                raise ValueError("Incorrect option")


#------------------------------------------------------------------------------#


        elif choice == 3:
            print(
                """
                1 - Hire policeman
                2 - Fire policeman
                3 - Add zone
                4 - Show policemen
                5 - Show info
                6 - Relocate policemen(policeman)
                7 - Investigate offense
                8 - Arrest criminals
                """)
            choice = int(input("Choose option: "))

            if choice == 1:
                add_policeman()

            elif choice == 3:
                add_zone()

            elif choice == 4:
                show_policemen()

            elif choice == 5:
                show_info()

            elif choice == 6:
                relocate_policemen()


            


#--------------------------------OPTION 4---------------------------------------#


        elif choice == 4:
            print(
                """
                1 - Add citizen
                2 - Delete citizen
                3 - Show citizens
                4 - Back
                """)
            choice = int(input())

            if choice == 1:
                add_citizen()

            elif choice == 2:
                delete_citizen()

            elif choice == 3:
                show_citizens()

            elif choice == 4:
                continue

            else:
                raise ValueError("Incorrect option")

#-------------------------------------------------------------------------#


        elif choice == 6:
            data_to_save = {
                "data/police.pkl": police,
                "data/history.pkl": history,
                "data/citizens.pkl": citizens,
                "data/laws.pkl": laws,
                "data/applications.pkl": applications,
                "data/security.pkl": security,
            }

            for path, obj in data_to_save.items():
                with open(path, "wb") as file:
                    pickle.dump(obj, file)

            break

        else:
            print("\nError: Incorrect option")


if __name__ == "__main__":
    main()