class Drivers:
    def __init__(self):
        self.drivers = []
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
            print("Drivers :")
            for d in self.drivers:
                print(f"{d["id"]}, {d["name"]}, {d["start_city"]}")
        else:
            print("No drivers available")

    def addDriver(self, name):
        start_city = input("Enter the start city of the driver: ")

        if not c.checkCityAvailability(start_city):
            print(f"Would you like to add the city '{start_city}' to our system? ")

            while True:
                user_input = input().strip().lower()
                if user_input not in ['yes', 'no']:
                    print("Please enter yes or no")
                else:
                    break

            if user_input == 'no':
                print("Would you like to add another start city name ? ")
                
                while True:
                    user_input = input().strip().lower()  
                    if user_input not in ['yes', 'no']:
                        print("Please enter yes or no")
                    else:
                        break
                
                if user_input == 'yes':
                    self.addDriver(name)
                else:
                    print("Nothing to add, back to the menu.")
                    return
            else:
                #yes add the city to the system
                c.graph_cities[start_city] = []
                print(f"{start_city} added, adding the driver..")
        
        #add a driver
        generatedId = self.generateDriverID()

        new_driver = { "id": generatedId, "name": name, "start_city": start_city }
        self.drivers.append(new_driver)

        print("New Driver added: ")
        print("ID: ", generatedId)
        print("Name: ", name)
        print("Start City: ", start_city)

    def checkSimilarDriver(self):
        dic = {}
        for driver in self.drivers:
            if driver["start_city"] not in dic:
                dic[driver["start_city"]] = [] #city: [drivers]  
            dic[driver["start_city"]].append(driver["name"])

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
        cities = list(self.graph_cities.keys())

        cities.sort()
        for c in cities:
            print(c)

    #another way
    def viewCities2(self): #MergeSort O(nlogn)
        print(mergeSort(list(self.graph_cities.keys()), 0, len(self.graph_cities) - 1))

    def searchCity(self, city):
        pass

    def printNeighboringCities(self):
        pass

    def printDriversByCity(self):
        pass

    def checkCityAvailability(self, city_name):
        if city_name in self.graph_cities:
            return True #available
        return False #not available

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

def mergeSort(list1, start, end):
    if start == end:
        return 
    mid = (start + end) // 2

    mergeSort(list1, start, mid)
    mergeSort(list1, mid+1, end)

    merge(list1, start, end)
    return list1

def merge(l, start, end):
    mid = (start + end) // 2
    i = start
    j = mid+1
    temp = []
    while i<= mid and j <= end:
        if l[i] < l[j]:
            temp.append(l[i])
            i += 1
        else:
            temp.append(l[j])
            j += 1

    while i<= mid:
        temp.append(l[i])
        i += 1

    while j <= end:
        temp.append(l[j])
        j += 1

    l[start:end+1] = temp

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

# print(c.graph_cities)
main()
