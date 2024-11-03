class Drivers:
    def __init__(self):
        self.drivers = []
        # self.drivers = [
        #     {
        #         'id': 'ID001',
        #         'name': 'User1',
        #         'start_city': 'beirut'
        #     },
        #     {
        #         'id': 'ID002',
        #         'name': 'User2',
        #         'start_city': 'akkar'
        #     }
        # ]
        self.total_drivers = len(self.drivers)

    def viewDrivers(self):
        if self.drivers:
            print("\nDrivers :")
            for d in self.drivers:
                print(f"{d["id"]}, {d["name"]}, {d["start_city"].capitalize()}")
        else:
            print("\nNo drivers available")

    def addDriver(self, name):
        start_city = input("\nEnter the start city of the driver: ").strip().lower()

        if not c.checkCityAvailability(start_city):
            while True:
                user_input = input(f"\n'{start_city.capitalize()}' is not present in the system. Would you like to add it ? (yes/no) ").strip().lower()
                if user_input not in ['yes', 'no']:
                    print("\nPlease enter yes or no\n")
                else:
                    break

            if user_input == 'no':
                print("\nWould you like to add another start city name ? ")
                
                while True:
                    user_input = input().strip().lower()  
                    if user_input not in ['yes', 'no']:
                        print("\nPlease enter yes or no\n")
                    else:
                        break
                
                if user_input == 'yes':
                    self.addDriver(name)
                else:
                    print("\nNothing to add, back to the menu.")
                    return
            else:
                #yes add the city to the system
                c.graph_cities[start_city] = []
                print(f"\n{start_city} added, adding the driver..")
        
        #add a driver
        generatedId = self.generateDriverID()

        new_driver = { "id": generatedId, "name": name, "start_city": start_city }
        self.drivers.append(new_driver)

        print("\nNew Driver added: ")
        print("ID: ", generatedId)
        print("Name: ", name)
        print("Start City: ", start_city.capitalize())

    def checkSimilarDriver(self):
        dic = {}
        for driver in self.drivers:
            if driver["start_city"] not in dic:
                dic[driver["start_city"]] = [] #city: [drivers]  
            dic[driver["start_city"]].append(driver["name"])
        for start_city, drivers in dic.items():
            print(f"{start_city.capitalize()}: {', '.join(drivers)}")

    def generateDriverID(self):
        self.total_drivers += 1
        return f"ID{self.total_drivers:03}"
class Cities:
    def __init__(self):
        # self.graph_cities = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': []}
        self.graph_cities = {}

    def viewCities(self): #Timesort algoithm by Python O(nlogn)
        # cities = list(self.graph_cities.keys())
        # cities.sort(reverse=True)
        # print(", ".join(cities))
        #or
        sorted_cities = sorted(self.graph_cities.keys(), reverse=True)
        x = 0
        for c in sorted_cities:
            if x < len(sorted_cities) - 1:
                print(c.capitalize(), end=", ")
            else: 
                print(c.capitalize())
            x += 1
        # print(", ".join(capitalized_cities))

    def searchCity(self, search_city):
        cities = self.graph_cities.keys()

        l = []
        for c in cities:
            if search_city.lower() in c.lower():
                l.append(c.capitalize())
        if l:
            print(", ".join(l))
        else:
            print("No cities found.")

    def printNeighboringCities(self, city):
        city = city.lower()
        if not c.checkCityAvailability(city):
            print(f"\nCity '{city.capitalize()}' not available in the system.")
            return
        
        neighbors = self.graph_cities[city]
        if neighbors:
            # print(f"Neighbors of the city '{city.capitalize()}': {", ".join(neighbors)}")
            print(f"\nNeighbors of the city '{city.capitalize()}'", end=": ")
            x = 0
            for n in neighbors:
                if x < len(neighbors) - 1:
                    print(n.capitalize(), end=", ")
                else: 
                    print(n.capitalize())
                x += 1
        else:
            print(f"\nNo neighbors found for the city '{city}'.")

    def printDriversByCity(self):
        pass

    def checkCityAvailability(self, city_name):
        if city_name in self.graph_cities:
            return True # available
        return False # not available

    def addCityNode(self, start_city):
        start_city = start_city.lower()
        if start_city in self.graph_cities:
            print(start_city.capitalize(), "is already present in the cities graph.")
        else:
            self.graph_cities[start_city] = []
    
    def addEdge(self, city1, city2, printIfAdded = False):
        city1 = city1.lower()
        city2 = city2.lower()

        if city1 not in self.graph_cities:
            user_input = input(f"\n'{city1.capitalize()}' is not present in the system. Would you like to add it ? (yes/no) ").lower()
            if user_input == "yes":
                c.addCityNode(city1)
            else:
                print(f"\nCannot add an edge with a non-existing city: {city1.capitalize()}")
                return
        
        if city2 not in self.graph_cities:
            user_input = input(f"\n'{city2.capitalize()}' is not present in the system. Would you like to add it ? (yes/no) ").lower()
            if user_input == "yes":
                c.addCityNode(city2)
            else:
                print(f"\nCannot add an edge with a non-existing city: {city2.capitalize()}")
                return
        
        self.graph_cities[city1].append(city2)
        self.graph_cities[city2].append(city1)
        
        if printIfAdded:
            print(f"\nEdge between '{city1.capitalize()}' and '{city2.capitalize()}' has been added.")

    def printGraph(self):
        for city, neighbors in self.graph_cities.items():
            print(f"{city.capitalize()}", end=": ")
            if neighbors:
                for i in range(len(neighbors)):
                    if i < len(neighbors) - 1:
                        print(neighbors[i].capitalize(), end=", ")
                    else:
                        print(neighbors[i].capitalize())
            else:
                print('----')

def driversMenu():
    print("\nEnter: ")
    while True:
        print("\n1. View all Drivers")
        print("2. Add a driver")
        print("3. Check similar drivers")
        print("4. Go back to the main menu\n")

        user_input = input()

        if not user_input.isdigit():
            print("\nPlease enter a number: 1, 2, 3, 4: ")
        else:
            if user_input == '1':
                d.viewDrivers()
            elif user_input == '2':
                name = input("\nEnter the Driver's name: ")
                d.addDriver(name)
            elif user_input == '3':
                print()
                d.checkSimilarDriver()
            elif user_input == '4':
                break
            else:
                print("\nPlease choose 1, 2, 3, 4: ")

def citiesMenu():
    print("\nEnter: ")
    while True:
        print("\n1. View Cities")
        print("2. Search City")
        print("3. Print neighboring cities ")
        print("4. Print Drivers delivering to city ")
        print("5. Add an edge between cities")
        print("6. Print a graph for cities")
        print("7. Go back to the main menu\n")

        user_input = input()

        if not user_input.isdigit():
            print("\nPlease enter a number: 1, 2, 3, 4, 5: ")
        else:
            if user_input == '1':
                print()
                c.viewCities()
            elif user_input == '2':
                key = input("\nEnter a key to search cities: ")
                print()
                c.searchCity(key)
            elif user_input == '3':
                city_name = input("\nEnter the city name to prints all cities that can be reached from: ")
                c.printNeighboringCities(city_name)
            elif user_input == '4':
                c.printDriversByCity()
            elif user_input == '5':
                city1 = input("\nEnter the first city: ")
                city2 = input("Enter the second city: ")
                c.addEdge(city1, city2, True)
            elif user_input == '6':
                print()
                c.printGraph()
            elif user_input == '7':
                break
            else:
                print("\nPlease choose 1, 2, 3, 4, 5: ")

def main():
    print("Hello! Welcome to our program. \nPlease enter: ")

    while True:
        print("\n1. Go to Drivers'Menu")
        print("2. Go to Cities' Menu")
        print("3. Exiting the system\n")

        user_input = input()

        if not user_input.isdigit():
            print("Please enter a number: 1, 2 or 3: ")
        else:
            if user_input == '1':
                driversMenu()
            elif user_input == '2':
                citiesMenu()
            elif user_input == '3':
                print("Thank you. Exiting the system. Exit")
                break
            else:
                print("Please choose 1, 2, or 3: ")

d = Drivers()
c = Cities()

c.addCityNode("beirut")
c.addCityNode("tripoli")
c.addCityNode("sidon")
c.addCityNode("byblos")
c.addCityNode("zahle")
c.addCityNode("jounieh")
c.addCityNode("baalbek")
c.addCityNode("tyre")
c.addCityNode("batroun")
c.addCityNode("akkar")
c.addCityNode("bshare")
c.addCityNode("jbeil")

c.addEdge("beirut", "tripoli")
c.addEdge("beirut", "sidon")
c.addEdge("beirut", "byblos")
c.addEdge("beirut", "jounieh")
c.addEdge("beirut", "zahle")
c.addEdge("tripoli", "byblos")
c.addEdge("tripoli", "akkar")
c.addEdge("tripoli", "batroun")
c.addEdge("akkar", "bshare")
c.addEdge("byblos", "jounieh")
c.addEdge("sidon", "tyre")
c.addEdge("zahle", "baalbek")

# print(c.graph_cities)
main()
