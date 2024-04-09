import datetime

def add_birthday():
    name = input("Enter friend's name: ")
    birthday = input("Enter friend's birthday (YYYY-MM-DD): ")
    with open("birthdays.txt", "a") as file:
        file.write(name + "," + birthday + "\n")

def check_birthdays():
    today = datetime.date.today()
    with open("birthdays.txt", "r") as file:
        for line in file:
            name, birthday = line.strip().split(",")
            birthday_date = datetime.datetime.strptime(birthday, "%Y-%m-%d").date()
            if birthday_date.month == today.month and birthday_date.day >= today.day:
                days_until_birthday = (birthday_date - today).days
                print(f"{name}'s birthday is in {days_until_birthday} days on {birthday_date.strftime('%B %d')}")
            elif birthday_date.month == today.month + 1 and today.day > birthday_date.day:
                days_until_birthday = (datetime.date(today.year, birthday_date.month, birthday_date.day) - today).days
                print(f"{name}'s birthday is in {days_until_birthday} days on {birthday_date.strftime('%B %d')}")
            elif birthday_date.month == 1 and today.month == 12 and today.day > birthday_date.day:
                days_until_birthday = (datetime.date(today.year + 1, birthday_date.month, birthday_date.day) - today).days
                print(f"{name}'s birthday is in {days_until_birthday} days on {birthday_date.strftime('%B %d')}")
            else:
                next_birthday_year = today.year + 1 if today.month > birthday_date.month else today.year
                days_until_birthday = (datetime.date(next_birthday_year, birthday_date.month, birthday_date.day) - today).days
                print(f"{name}'s birthday is in {days_until_birthday} days on {birthday_date.strftime('%B %d')}")

def main():
    while True:
        print("\n1. Add a birthday")
        print("2. Check birthdays")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_birthday()
        elif choice == "2":
            check_birthdays()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
