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
                if history.empy():
                    print("History id empty")
                else:
                    for h in history:
                        print(f"{h}\n")

            elif choice == 2:
                history.clear()

            elif choice == 3:
                continue

            else:
                raise ValueError("Incorrect option")


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
            with open("data/police.pkl", "wb") as file:
                pickle.dump(police, file)
    
            with open("data/history.pkl", "wb") as file:
                pickle.dump(history, file)

            with open("data/citizens.pkl", "wb") as file:
                pickle.dump(citizens, file)

            with open("data/laws.pkl", "wb") as file:
                pickle.dump(laws, file)

            with open("data/security.pkl", "wb") as file:
                pickle.dump(security, file)

            break

        else:
            print("\nError: Incorrect option")


if __name__ == "__main__":
    main()