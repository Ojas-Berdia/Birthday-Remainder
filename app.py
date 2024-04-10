import datetime
from plyer import notification

# Function to add a birthday
def add_birthday(name, birthdate, birthdays):
    birthdays[name] = birthdate

# Function to remove a birthday
def remove_birthday(name, birthdays):
    if name in birthdays:
        del birthdays[name]
        print(f"{name}'s birthday has been removed from the list.")
    else:
        print(f"{name} is not found in the birthday list.")

# Function to display all birthdays
def display_birthdays(birthdays):
    print("\nBirthdays:")
    for name, birthdate in birthdays.items():
        print(f"{name}: {birthdate}")

# Function to check and display upcoming birthdays with remaining days
def check_upcoming_birthdays(birthdays):
    today = datetime.date.today()
    upcoming_birthdays = {}
    for name, birthdate in birthdays.items():
        birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d").date()
        birthdate_this_year = birthdate.replace(year=today.year)
        if birthdate_this_year < today:
            birthdate_this_year = birthdate_this_year.replace(year=today.year + 1)
        days_remaining = (birthdate_this_year - today).days
        upcoming_birthdays[name] = (birthdate_this_year.strftime("%Y-%m-%d"), days_remaining)
    if upcoming_birthdays:
        print("\nUpcoming Birthdays with Remaining Days:")
        for name, (birthdate, days_remaining) in upcoming_birthdays.items():
            print(f"{name}: {birthdate} (in {days_remaining} days)")
            if days_remaining == 0:
                notification_title = "Birthday Reminder"
                notification_message = f"Today is {name}'s birthday!"
                notification.notify(
                    title=notification_title,
                    message=notification_message,
                    app_name="Birthday Reminder",
                    timeout=10
                )
    else:
        print("\nNo upcoming birthdays.")

# Main function
def main():
    birthdays = {}
    while True:
        print("\n1. Add a birthday")
        print("2. Remove a birthday")
        print("3. Display all birthdays")
        print("4. Check upcoming birthdays")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter friend's name: ")
            birthdate = input("Enter friend's birthday (YYYY-MM-DD): ")
            add_birthday(name, birthdate, birthdays)
        elif choice == '2':
            name = input("Enter friend's name to remove: ")
            remove_birthday(name, birthdays)
        elif choice == '3':
            display_birthdays(birthdays)
        elif choice == '4':
            check_upcoming_birthdays(birthdays)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
