print("===== Hotel Management System =====")

print("1. Book Room")
print("2. Exit")

choice = input("Enter your choice: ")

if choice == "1":
    name = input("Enter customer name: ")
    room = input("Enter room number: ")
    print("Room booked successfully!")
elif choice == "2":
    print("Thank you for using the system")
else:
    print("Invalid choice")
