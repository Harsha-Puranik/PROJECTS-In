def show_about_me():
    print("\n--- About Me ---")
    print("Hello! I'm Harsha Puranik, a BCA student passionate about Python, Web development, and building cool projects.")

def show_projects():
    print("\n--- Projects ---")
    print("1. Weather App - A Python app that shows weather using an API.")
    print("2. To-DO list - A command-line to-do manager.")
    print("3. Portfolio App - This console app showing my profile!")

def show_contact():
    print("\n--- Contact ---")
    print("Email: harshapuranik79@gmail.com")
    print("Phone: +91-7406078302")
    print("LinkedIn: https://www.linkedin.com/in/harsha-gopalkrishna-puranik-7a227b323/")

def main():
    while True:
        print("\n========= My Portfolio =========")
        print("1. About Me")
        print("2. Projects")
        print("3. Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
    
        if choice == "1":
            show_about_me()
        elif choice == "2":
            show_projects()
        elif choice == "3":
            show_contact()
        elif choice == "4":
            print("Thank you for visiting my Portfolio!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
