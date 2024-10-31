class Drivers:
    def __init__(self):
        self.drivers = []
        self.total_drivers = len(self.drivers)

    def viewDrivers(self):
        pass

    def addDriver(self, name):
        pass

    def checkSimilarDriver(self):
        pass

    def generateDriverID(self):
        pass
class Cities:
    def __init__(self):
        # self.graph_cities = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': []}
        self.graph_cities = {}

    def viewCities(self):
        pass

    def searchCity(self, city):
        pass

    def printNeighboringCities(self):
        pass

    def printDriversByCity(self):
        pass

    def checkCityAvailability(self, city_name):
        pass


def driversMenu():
    while True:
        print("1. View all Drivers")
        print("2. Add a driver")
        print("3. Check similar drivers")
        print("4. Go back to the main menu")

        user_input = input()

        if not user_input.isdigit():
            print("Please enter a number: 1, 2, 3, 4: ")
        else:
            if user_input == '1':
                d.viewDrivers()
            elif user_input == '2':
                name = input("Enter the Driver's name: ")
                d.addDriver(name)
            elif user_input == '3':
                d.checkSimilarDriver()
            elif user_input == '4':
                break
            else:
                print("Please choose 1, 2, 3, 4: ")

def citiesMenu():
    while True:
        print("1. View Cities")
        print("2. Search City")
        print("3. Print neighboring cities ")
        print("4. Print Drivers delivering to city ")
        print("5. Go back to the main menu")

        user_input = input()

        if not user_input.isdigit():
            print("Please enter a number: 1, 2, 3, 4, 5: ")
        else:
            if user_input == '1':
                c.viewCities()
            elif user_input == '2':
                c.searchCity('d')
            elif user_input == '3':
                c.printNeighboringCities()
            elif user_input == '4':
                c.printDriversByCity()
            elif user_input == '5':
                break
            else:
                print("Please choose 1, 2, 3, 4, 5: ")

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
                print("Enter: ")
                driversMenu()
            elif user_input == '2':
                print("Enter: ")
                citiesMenu()
            elif user_input == '3':
                print("Thank you. Exiting the system. Exit")
                break
            else:
                print("Please choose 1, 2, or 3: ")

d = Drivers()
c = Cities()

main()