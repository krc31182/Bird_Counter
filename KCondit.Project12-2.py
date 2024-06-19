# Kenneth Condit
# 6/13/2024

import pickle

def load_data():
    try:
        with open("bird_sightings.pickle", "rb") as f:
            bird_sightings = pickle.load(f)
    except FileNotFoundError:
        bird_sightings = {}
    return bird_sightings

def save_data(bird_sightings):
    with open("bird_sightings.pickle", "wb") as f:
        pickle.dump(bird_sightings, f)

def add_bird(bird_sightings):
    bird_name = input("Enter name of bird: ").strip().lower()
    if bird_name in bird_sightings:
        bird_sightings[bird_name] += 1
    else:
        bird_sightings[bird_name] = 1
    print(f"{bird_name.capitalize()} added to the list.")

def show_birds(bird_sightings):
    if not bird_sightings:
        print("No birds have been sighted yet.")
    else:
        sorted_birds = sorted(bird_sightings.items(), key=lambda x: x[0])
        print("Name:  Count")
        for bird, count in sorted_birds:
            print(f"{bird.capitalize()}:   {count}")

def main():
    bird_sightings = load_data()
    while True:
        print("The bird counter program by Ken Condit")
        print("")
        choice = input("Enter 'add' to add a bird, 'show' to show birds, or 'x' to exit: ").strip().lower()
        if choice == "add":
            add_bird(bird_sightings)
        elif choice == "show":
            show_birds(bird_sightings)
        elif choice == "x":
            save_data(bird_sightings)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
