staff_records = []

def add_staff():
    name = input("Enter staff name: ")
    position = input("Enter staff position: ")
    staff_records.append({"name": name, "position": position})
    print("Staff added successfully")

def view_staff():
    if not staff_records:
        print("No staff records found")
    else:
        for staff in staff_records:
            print(staff["name"], "-", staff["position"])

def main():
    while True:
        print("1. Add Staff")
        print("2. View Staff")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_staff()
        elif choice == "2":
            view_staff()
        elif choice == "3":
            break
        else:
            print("Invalid option")

main()
