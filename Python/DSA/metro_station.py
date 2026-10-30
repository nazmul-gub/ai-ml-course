class Station: 
    def __init__(self, name):
        self.name = name
        self.next = None

class MetroLine:
    def __init__(self, head = None):
        self.head = head
        self.next = None

    def addStation(self, stationName):
        newStation = Station(stationName)
        

        if self.head is None:
            self.head = newStation
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = newStation

    
    def calculateFare(self, startStation, endStation):
        current = self.head
        index = 0

        start_index = None
        end_index = None

        while current is not None:
            if current.name == startStation:
                start_index = index

            if current.name == endStation:
                end_index = index

            current = current.next
            index += 1

        if start_index is None:
            print("Starting station not found!")
            return

        if end_index is None:
            print("Destination station not found!")
            return

        stations_travelled = abs(end_index - start_index)
        fare_per_station = 10

        fare = stations_travelled * fare_per_station

        print(f"Total Stations travelled: {stations_travelled}")
        print(f"Total fare: ৳{fare}")

    def displayStations(self):
        current = self.head

        if current is None:
            print("There is no stations in this line!!")
            return

        while current is not None:
            print(current.name, end=" -> ")
            current = current.next
        print("END")

    def searchStation(self, stationName):
        current = self.head

        while current is not None:
            if current.name == stationName:
                return f"✅ {current} is found!"
            current = current.next

        return f"❌ {stationName} is not found!!"

    def countStations(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next

        return count

    def insertAfter(self, targetStation, newStation):
        current = self.head

        temp = Station(newStation)

        while current is not None:
            if(current.name == targetStation):
                temp.next = current.next
                current.next = temp

            current = current.next

    def removeStation(self, stationName):
        # if metro line is empty
        if self.head is None:
            return

        #if we want to delete the first station
        if self.head.name == stationName:
            self.head = self.head.next

        #delete at any station

        prev = self.head
        current = self.head.next

        while current is not None:
            if current.name == stationName:
                prev.next = current.next
                return

            prev = current
            current = current.next


        
dmtcl = MetroLine()

dmtcl.addStation("Motijil")
dmtcl.addStation("Bangladesh Secretariate")
dmtcl.addStation("Dhaka University")
dmtcl.addStation("Shahbagh")
dmtcl.addStation("Karwan Bazar")
dmtcl.addStation("Farmgate")
dmtcl.addStation("Bijay Sarani")
dmtcl.addStation("Agargaon")
dmtcl.addStation("Shewrapara")
dmtcl.addStation("Kazipara")
dmtcl.addStation("Mirpur 10")
dmtcl.addStation("Mirpur 11")
dmtcl.addStation("Pallabi")
dmtcl.addStation("Uttara North")
dmtcl.addStation("Uttara Center")
dmtcl.addStation("Uttara South")

# dmtcl.displayStations()

# dmtcl.calculateFare("Pallabi", "Uttara")

# print(dmtcl.searchStation("Pallabi"))

# print(dmtcl.countStations())

# dmtcl.insertAfter("Shahbagh", "New Market")
# dmtcl.displayStations()

# dmtcl.removeStation("Shahbagh")
# dmtcl.displayStations()



def runMetroApp(metro):
    while True:
        print("\n===== DHAKA METRO LINE =====")
        print("1. Add station")
        print("2. Display all stations")
        print("3. Search station")
        print("4. Count stations")
        print("5. Calculate fare")
        print("6. Insert station after another station")
        print("7. Remove station")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter station name: ").strip()

            if name:
                metro.addStation(name)

        if choice == "2":
            metro.displayStations()

        if choice == "3":
            searchingStation = input("Enter the station that you want to search??").strip()
            result = metro.searchStation(searchingStation)

            if result is not None:
                print(f"Found station: {result.name}")
            else:
                print("Station not found!")

        if choice == "4":
            print(f"Total stations: {metro.countStations()}")

        if choice == "5":
            start = input("Enter starting station: ").strip()
            end = input("Enter ending station: ").strip()

            fare = metro.calculateFare(start, end)

            if fare is None:
                print("Invalid station name!")
            else:
                print(f"Total fare: ৳{fare}")


        elif choice == "6":
            target = input("Insert after which station? ").strip()
            new_name = input("New station name: ").strip()
            metro.insertAfter(target, new_name)

        elif choice == "7":
            name = input("Station to remove: ").strip()
            metro.removeStation(name)

        elif choice == "0":
            print("Leaving Metro Line System. Goodbye!")
            break
        else:
            print("Invalid choice! Please select an option from the menu.")


runMetroApp(dmtcl)









