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
                return f"✅ {current.name} is found!"
            current = current.next

        return f"❌ {stationName} is not found!!"

    def countStations(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next

        return f"Total stations: {count}"

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

dmtcl.addStation("TSC")
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

# dmtcl.displayStations()

# dmtcl.calculateFare("TSC", "Agargaon")

# print(dmtcl.searchStation("Pallabi"))

# print(dmtcl.countStations())

dmtcl.insertAfter("Shahbagh", "New Market")
dmtcl.displayStations()

dmtcl.removeStation("Shahbagh")
dmtcl.displayStations()