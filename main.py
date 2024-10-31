def main():
    print("Hello! Please enter: ")

    while True:
        print("1. Go to Drivers'Menu")
        print("2. Go to Cities' Menu")
        print("3. Exiting the system")

        user_input = input()

        if not user_input.isdigit():
            print("Please enter a number: 1, 2 or 3: ")
        else:
            if user_input == '1':
                #driversMenu()
                continue
            elif user_input == '2':
                #citiesMenu()
                continue
            elif user_input == '3':
                print("Thank you. Exiting the system. Exit")
                break
            else:
                print("Please choose 1, 2, or 3: ")

main()