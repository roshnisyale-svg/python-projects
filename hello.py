import os

FILE = "notes.txt"

def add_note():
    note = input("Write your note: ")
    with open(FILE, "a") as f:
        f.write(note + "\n")
    print("Note saved.")

def view_notes():
    if not os.path.exists(FILE):
        print("No notes yet.")
        return
    
    with open(FILE, "r") as f:
        notes = f.readlines()
    
    print("\nYour Notes:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note.strip()}")

def delete_notes():
    open(FILE, "w").close()
    print("All notes deleted.")

while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Delete All Notes")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_note()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        delete_notes()
    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Invalid choice")