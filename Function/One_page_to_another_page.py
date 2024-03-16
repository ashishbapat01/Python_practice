def homepage():
    print("Welcome to the homepage!")
    # Example: Display options for the user
    print("1. Go to Page 1")
    print("2. Go to Page 2")
    choice = input("Enter your choice: ")

    if choice == "1":
        page1()
    elif choice == "2":
        page2()
    else:
        print("Invalid choice. Please try again.")
        homepage()

def page1():
    print("You are on Page 1.")
    # Example: Display options for the user
    print("1. Go back to Homepage")
    print("2. Go to Page 2")
    choice = input("Enter your choice: ")

    if choice == "1":
        homepage()
    elif choice == "2":
        page2()
    else:
        print("Invalid choice. Please try again.")
        page1()

def page2():
    print("You are on Page 2.")
    # Example: Display options for the user
    print("1. Go back to Homepage")
    print("2. Go to Page 1")
    choice = input("Enter your choice: ")

    if choice == "1":
        homepage()
    elif choice == "2":
        page1()
    else:
        print("Invalid choice. Please try again.")
        page2()

# Start the program by calling the homepage function
homepage()
