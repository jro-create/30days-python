# Notes App - Mini Project (Day 7)

def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved!")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            if not notes:
                print("No notes yet.")
                return
            print("\nYour Notes:")
            for line in notes:
                print("-", line.strip())
    except FileNotFoundError:
        print("No notes found. Try adding one first!")

def main():
    while True:
        print("\n1. Add Note")
        print("2. View Notes")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
# Notes App - Mini Project (Day 7)

def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved!")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
            if not notes:
                print("No notes yet.")
                return
            print("\nYour Notes:")
            for line in notes:
                print("-", line.strip())
    except FileNotFoundError:
        print("No notes found. Try adding one first!")

def main():
    while True:
        print("\n1. Add Note")
        print("2. View Notes")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

