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

    def addCityNode(self, start_city):
        if start_city in self.graph_cities:
            print(start_city, "is already present in the cities graph.")
        else:
            self.graph_cities[start_city] = []
    
    def addEdge(self, city1, city2):
        if city1 not in self.graph_cities:
             print(city1, "is not present in the cities graph_cities")
        elif city2 not in self.graph_cities:
             print(city2, "is not present in the cities graph")
        else:
            self.graph_cities[city1].append(city2)
            self.graph_cities[city2].append(city1)


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

c.addCityNode("Beirut")
c.addCityNode("Tripoli")
c.addCityNode("Sidon")
c.addCityNode("Byblos")
c.addCityNode("Zahle")
c.addCityNode("Jounieh")
c.addCityNode("Baalbek")
c.addCityNode("Tyre")
c.addCityNode("Batroun")
c.addCityNode("Akkar")
c.addCityNode("Bshare")
c.addCityNode("Jbeil")

c.addEdge("Beirut", "Tripoli")
c.addEdge("Beirut", "Sidon")
c.addEdge("Beirut", "Byblos")
c.addEdge("Beirut", "Jounieh")
c.addEdge("Beirut", "Zahle")
c.addEdge("Tripoli", "Byblos")
c.addEdge("Tripoli", "Akkar")
c.addEdge("Tripoli", "Batroun")
c.addEdge("Akkar", "Bshare")
c.addEdge("Byblos", "Jounieh")
c.addEdge("Sidon", "Tyre")
c.addEdge("Zahle", "Baalbek")

print(c.graph_cities)
main()
