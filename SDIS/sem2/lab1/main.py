import pickle
import os
from police import Police
from police import Policeman
from police import Citizen
from police import Crime
from police import Investigation
from police import Law
from police import Security

def main():
    data_dir = "data"
    os.makedirs(data_dir, exist_ok=True)

    data_files = {
        "police.pkl":    Police(),
        "history.pkl":   [],
        "citizens.pkl":  [],
        "laws.pkl":      [],
        "security.pkl":  Security()
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

    police    = loaded["police.pkl"]
    history   = loaded["history.pkl"]
    citizens  = loaded["citizens.pkl"]
    laws      = loaded["laws.pkl"]
    security  = loaded["security.pkl"]

    while True:
        print(
            """ 
            Choice option:
            1 - Start investigation
            2 - History
            3 - Police settings
            4 - Civil settings
            5 - Law settings
            6 - Exit
            """)
        choice = int(input())

        if choice == 6:
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


if __name__ == "__main__":
    main()