# Cab Service App

#1. Vehicle
#2. Driver
#3. Rider


class Zone:

    def __init__(self):

        self.drivers = []
        self.cars = []
        self.users = []

    def addDrivers(self, drivers_list):

        self.drivers.append(drivers_list)
        print('Drivers are added to the Zone')

    def addCars(self, cars_list):

        self.cars.append(cars_list)
        print('Drivers are added to the Zone')


    def addUsers(self, users_list):
            self.users.append(users_list)
            print('Drivers are added to the Zone')

    def getDrivers(self):
        return self.drivers


    # def getinfo(self):
    #     print([i.plate for i in self.cars])
    #     print('--------------------------')
    #     print([i.name for i in self.drivers])
    #     print('--------------------------')
    #     print([i.name for i in self.users])

class Car:

    def __init__(self, plate, make, model):

        self.plate = plate
        self.make = make
        self.model = model
        self.fuel_percent = 0.7
        self.capacity = 4


class User:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.history = []
        self.location = None


    def requestRide(self, dist, zone):


        #List down all the drives in the zone
        drivers_list = zone.getDrivers()[0]
        act_drivers_status = [(i.name, i.status) for i in zone.drivers[0]]
        print(act_drivers_status)

        # return self.id


class Driver:
    def __init__(self, id, name, vehicle=None):
        self.id = id
        self.name = name
        self.history = []
        self.location = None
        self.status = "Available"

    def getInfo(self):
        print(f'Name: {self.name}, Driver ID: {self.id} , Location: {self.location} , Status: {self.status}')


    def getDriverName(self):

        return self.name
    
    def setStatus(self, status):
        old_status = self.status
        self.status = status
        print(f'The Status of the Driver is changed from {old_status} --> {self.status}')


    def acceptRide(self, user, dist=20):

        if self.status != "Available":
            print("Cannot accept ride, diver is not available")
        else:
            print(f"Ride has been started with  {user.name}")
            self.setStatus('Busy')
            self.history.append([self.name, f'Rider: {user.name}', f'Distance: {dist}'])

    def getHistory(self):
        print(self.history)


    def completeRide(self):
        self.setStatus('Avaiable')



z1 =  Zone()

c1 = Car("HB 5967","Hyundai", "Aura")
c2 = Car("BV 8963", "Toyota", "Etios")

d1 = Driver(1, "John", vehicle=c1)
d2 = Driver(2, "Stephen", vehicle=c2)
d3 = Driver(3, "Rechen")
d4 = Driver(4, "Smith")

u1 = User(3, "Jennifer")
u2 = User(4, "Kryz")

z1.addCars([c1, c2])
z1.addDrivers([d1, d2, d3, d4])
z1.addUsers([u1, u2])
# z1.getinfo()

u1.requestRide(100, z1)

# d1.acceptRide(u1)
# d1.getInfo()
# d1.getHistory()
# d1.acceptRide(u2)



# drivers = [d1, d2, d3, d4]

# for div in drivers:
#     div.getInfo()

#     print("------------------------------------------------------")


# d1.setStatus('Lunch')
# d1.getInfo()
# d1.setStatus('Busy')
# d1.getInfo()

