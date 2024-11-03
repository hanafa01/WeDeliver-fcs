class Drivers:
    def __init__(self):
        self.drivers = [
            {"id": "ID001", "name": "User1", "start_city": "K"},
            {"id": "ID002", "name": "User2", "start_city": "B"},
            {"id": "ID003", "name": "User3", "start_city": "F"},
            {"id": "ID004", "name": "User4", "start_city": "W"},
            {"id": "ID005", "name": "User5", "start_city": "B"},
            {"id": "ID006", "name": "User6", "start_city": "G"},
            {"id": "ID007", "name": "User7", "start_city": "K"},
            {"id": "ID008", "name": "User8", "start_city": "O"},
            {"id": "ID009", "name": "User9", "start_city": "B"},
        ]
        
        # self.drivers = [
        #     {
        #         'id': 'ID001',
        #         'name': 'User1',
        #         'start_city': 'Beirut'
        #     },
        #     {
        #         'id': 'ID002',
        #         'name': 'User2',
        #         'start_city': 'Akkar'
        #     }
        # ]
        self.total_drivers = len(self.drivers)

    def viewDrivers(self):
        if self.drivers:
            print("\nDrivers: ")
            for d in self.drivers:
                print(f"{d["id"]}, {d["name"]}, {d["start_city"]}")
        else:
            print("\nNo drivers available")

    def addDriver(self, name):
        start_city = input("Enter the start city of the driver: ").strip().lower().capitalize()

        if not c.checkCityAvailability(start_city):
            while True:
                user_input = input(f"\n'{start_city}' is not present in the system. Would you like to add it ? (yes/no) ").strip().lower()
                if user_input not in ['yes', 'no']:
                    print("\nPlease enter yes or no")
                else:
                    break

            if user_input == 'no':
                #checknow \n                
                while True:
                    user_input = input("\nWould you like to add another start city name ? (yes/no) ").strip().lower()  
                    if user_input not in ['yes', 'no']:
                        print("\nPlease enter yes or no\n")
                    else:
                        break
                
                if user_input == 'yes':
                    print()
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
        print("Start City: ", start_city)

    def checkSimilarDriver(self):
        dic = {}
        for driver in self.drivers:
            if driver["start_city"] not in dic:
                dic[driver["start_city"]] = [] #city: [drivers]  
            dic[driver["start_city"]].append(driver["name"])

        print("\nSimilar Drivers: ")
        for start_city, drivers in dic.items():
            print(f"{start_city}: {', '.join(drivers)}")

    def generateDriverID(self):
        self.total_drivers += 1
        return f"ID{self.total_drivers:03}"
class Cities:
    def __init__(self):
        # self.graph_cities = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': []}
        self.graph_cities = {}

    def viewCities(self): #Timesort algoithm by Python O(nlogn)
        print("\nView Cities:")
        sorted_cities = sorted(self.graph_cities.keys(), reverse=True)
        print(", ".join(sorted_cities))

    #checknow
    def searchCity(self, search_city):
        cities = self.graph_cities.keys()

        l = []
        for c in cities:
            if search_city.strip().lower() in c.lower():
                l.append(c.capitalize())
        print(f"\nSearch for city '{search_city}': ")
        if l:
            print(", ".join(l))
        else:
            print("No cities found.")

    def printNeighboringCities(self, city):
        city = city.strip().lower().capitalize()
        if not c.checkCityAvailability(city):
            print(f"\nCity '{city}' not available in the system.")
            return
        
        neighbors = self.graph_cities[city]
        if neighbors:
            print(f"\nNeighbors of the city '{city}': {", ".join(neighbors)}")
        else:
            print(f"\nNo neighbors found for the city '{city}'.")

    def printDriversReachedByCity(self, city_name):
        city_name = city_name.strip().lower().capitalize()
        
        if city_name in self.graph_cities:
            reachable_drivers = []
            for driver in d.drivers:
                if self.bfsCanReach(driver['start_city'],city_name):
                    if driver['name'] not in reachable_drivers:
                        reachable_drivers.append(driver['name'])
            
            if reachable_drivers:
                print(f"\nThe drivers that can be delivered to the city '{city_name}': ")
                print(", ".join(reachable_drivers))
            else:
                print("\nNo drivers found.")
        else:
            print(f"\n{city_name} is not present in the system.")

    
    def bfsCanReach(self, startCityNode, city_name_search):
        visited = []
        queue = []

        visited.append(startCityNode)
        queue.append(startCityNode)

        while queue:
            m = queue.pop(0)
            # print(m, end=" ")
            if city_name_search == m:
                return True
            
            for neighbour in self.graph_cities[m]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        
        return False

    def checkCityAvailability(self, city_name):
        if city_name in self.graph_cities:
            return True # available
        return False # not available

    def addCityNode(self, start_city):
        start_city = start_city.strip().lower().capitalize()
        if start_city in self.graph_cities:
            print(start_city, "is already present in the system.")
        else:
            self.graph_cities[start_city] = []
    
    def addEdge(self, city1, city2, printIfAdded = False):
        city1 = city1.strip().lower().capitalize()
        city2 = city2.strip().lower().capitalize()

        if city1 not in self.graph_cities:
            user_input = input(f"\n'{city1}' is not present in the system. Would you like to add it ? (yes/no) ").lower()
            if user_input == "yes":
                c.addCityNode(city1)
            else:
                print(f"\nCannot add an edge with a non-existing city: {city1}")
                return
        
        if city2 not in self.graph_cities:
            user_input = input(f"\n'{city2}' is not present in the system. Would you like to add it ? (yes/no) ").lower()
            if user_input == "yes":
                c.addCityNode(city2)
            else:
                print(f"\nCannot add an edge with a non-existing city: {city2}")
                return
        
        self.graph_cities[city1].append(city2)
        self.graph_cities[city2].append(city1)
        
        if printIfAdded:
            print(f"\nEdge between '{city1}' and '{city2}' has been added.")

    def printGraph(self):
        for city, neighbors in self.graph_cities.items():
            print(f"{city}", end=": ")
            if neighbors:
                # for n in neighbors:
                   print(", ".join(neighbors))
            else:
                print('----')

def driversMenu():
    while True:
        print("\nEnter: ")
        print("1. View all Drivers")
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
    while True:
        print("\nEnter: ")
        print("1. View Cities")
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
                c.viewCities()
            elif user_input == '2':
                key = input("\nEnter a key to search cities: ")
                c.searchCity(key)
            elif user_input == '3':
                city_name = input("\nEnter the city name to prints all cities that can be reached from: ")
                c.printNeighboringCities(city_name)
            elif user_input == '4':
                city_name = input("\nEnter the city name: ")
                c.printDriversReachedByCity(city_name)
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
    print("\nHello! Welcome to our program, ")

    while True:
        print("\nEnter: ")
        print("1. Go to Drivers'Menu")
        print("2. Go to Cities' Menu")
        print("3. Exiting the system\n")

        user_input = input()

        if not user_input.isdigit():
            print("\nPlease enter a number: 1, 2 or 3: ")
        else:
            if user_input == '1':
                driversMenu()
            elif user_input == '2':
                citiesMenu()
            elif user_input == '3':
                print("\nThank you. Exiting the system. Exit")
                break
            else:
                print("\nPlease choose 1, 2, or 3: ")

d = Drivers()
c = Cities()

c.addCityNode("B")
c.addCityNode("T")
c.addCityNode("S")
c.addCityNode("C")
c.addCityNode("Z")
c.addCityNode("J")
c.addCityNode("F")
c.addCityNode("H")
c.addCityNode("U")
c.addCityNode("A")
c.addCityNode("W")
c.addCityNode("V")
c.addCityNode("M")
c.addCityNode("I")
c.addCityNode("G")
c.addCityNode("K")
c.addCityNode("L")
c.addCityNode("O")
c.addCityNode("P")

c.addEdge("B", "T")
c.addEdge("B", "S")
c.addEdge("B", "C")
c.addEdge("B", "J")
c.addEdge("B", "Z")
c.addEdge("T", "C")
c.addEdge("T", "A")
c.addEdge("T", "U")
c.addEdge("A", "W")
c.addEdge("C", "J")
c.addEdge("S", "H")
c.addEdge("Z", "F")
c.addEdge("M", "I")
c.addEdge("I", "G")
c.addEdge("K", "L")

# print(c.graph_cities)
main()
