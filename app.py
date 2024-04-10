import datetime


def add_birthday():
    name = input("Enter friend's name: ")
    birthday = input("Enter friend's birthday (YYYY-MM-DD): ")
    with open("birthdays.txt", "a") as file:
        file.write(name + "," + birthday + "\n")


def delete_birthday():
    name_to_delete = input("Enter the name of the friend whose birthday you want to delete: ")
    with open("birthdays.txt", "r") as file:
        lines = file.readlines()
    with open("birthdays.txt", "w") as file:
        for line in lines:
            name, _ = line.strip().split(",")
            if name != name_to_delete:
                file.write(line)
    print(f"{name_to_delete}'s birthday has been deleted.")


def edit_birthday():
    name_to_edit = input("Enter the name of the friend whose birthday you want to edit: ")
    new_name = input("Enter the new name (leave blank to keep the same): ")
    new_birthday = input("Enter the new birthday (YYYY-MM-DD) (leave blank to keep the same): ")
    with open("birthdays.txt", "r") as file:
        lines = file.readlines()
    with open("birthdays.txt", "w") as file:
        for line in lines:
            name, birthday = line.strip().split(",")
            if name == name_to_edit:
                if new_name:
                    name = new_name
                if new_birthday:
                    birthday = new_birthday
                file.write(name + "," + birthday + "\n")
            else:
                file.write(line)
    print(f"{name_to_edit}'s birthday has been updated.")


def display_birthdays():
    print("\nBirthdays:")
    with open("birthdays.txt", "r") as file:
        for line in file:
            # Split the line into name and birthday using comma as the delimiter
            parts = line.strip().split(",")
            if len(parts) == 2:  # Check if the line contains both name and birthday
                name, birthday = parts
                print(f"{name}: {birthday}")


def main():
    while True:
        print("\n1. Add a birthday")
        print("2. Delete a birthday")
        print("3. Edit a birthday")
        print("4. Display all birthdays")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_birthday()
        elif choice == "2":
            delete_birthday()
        elif choice == "3":
            edit_birthday()
        elif choice == "4":
            display_birthdays()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
