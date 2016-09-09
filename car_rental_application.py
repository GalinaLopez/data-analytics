# CA2 - DBS Car Rental Application
# Module - Programming for Big Data
# Student - Galina Lopez 10333429

from car import *
from car_rental import *

# constants
BOOKINGFEE = 14.00
DAILYRATE = 25.00
FIRST100 = 0.30
NEXT100 = 0.20
ABOVE200 = 0.10

# function definitions
# shows main menu
def showMainMenu():
    print "\n###########################################"
    print "\n\tDBS CAR RENTAL MAIN MENU"
    print "\n###########################################"
    print "\nSelect 1 to rent a car"
    print "Select 2 to return a car"    
    print "\n###########################################\n"
    return True

# shows next menu with car types  
def showNextMenu():
    print "\n###########################################"
    print "\nSelect 1 for petrol car"
    print "Select 2 for diesel car"
    print "Select 3 for electric car"
    print "Select 4 for hybrid car"    
    print "\n###########################################\n"
    return True
 
# takes user input and converts it to int and validates it to bigger than 0
def enterConvertValidate(msg):
    while True:
        sInput = raw_input(msg)
        try:
            input = int(sInput)      
            if input <= 0:           
                print "Out of range entry."
                continue
            else:
                break
        except:
            print "Invalid entry."
    return input

# calculates mileage surcharge based on miles travelled
# first 100 cost 0.30
# next 100 cost 0.20
# above 200 cost 0.10
def calculateMileageSurcharge(miles):
    if miles <= 100:
        result = miles * FIRST100
    elif miles <= 200:
        result = 100 * FIRST100
        result += (miles - 100) * NEXT100
    else:
        result = 100 * FIRST100
        result += 100 * NEXT100
        result += (miles - 200) * ABOVE200
    return result

# prints transaction details 
def printTransactionDetails(customer, car):
    print "\n###########################################"
    print "\n\tTRANSACTION DETAILS"
    print "\nCustomer Id:            \t", customer.getId()
    print "Customer Name:            \t", customer.getName()
    print "\nCar Registration Number:  \t", car.getReg()
    print "Car Make                  \t", car.getMake()
    print "Car Model                 \t", car.getModel()
    print "Car Colour                \t", car.getColour()
    print "\nBooking Fee paid:       \t", BOOKINGFEE
    print "\n###########################################"
    return True
    
# prints transaction receipt
def printTransactionReceipt(customer, dailyRental, mileageSurcharge):
    print "\n###########################################"
    print "\n\tTRANSACTION RECEIPT"
    print "\nCustomer Id:     \t", customer.getId()
    print "Customer Name:     \t", customer.getName()
    print "\nBooking Fee:     \t", BOOKINGFEE
    print "Daily Rate:       \t%.2f" %dailyRental
    print "Mileage Surcharge:\t%.2f" %mileageSurcharge
    print "Total paid:       \t%.2f" %(BOOKINGFEE + dailyRental + mileageSurcharge)
    print "\n###########################################"
    return True

# fills car with details about its reg, make, model, colour, mileage and type
def fillCarDetails(data, index, car):    
    details = data[index].split(',')
    car.reg = details[0].strip()
    car.make = details[1].strip()
    car.model = details[2].strip()
    car.colour = details[3].strip()
    car.mileage = int(details[4].strip())
    car.type = int(details[5].strip())
    return car

    
# read in the data from the cars.csv file    
data = [line.strip() for line in open('cars.csv', 'r')]
# print data

carRental=CarRental()

# populate the car pool
index = 1
petrol_cars = []
for x in range (24):     
    petrol_cars.append(fillCarDetails(data, index, PetrolCar()))
    index += 1    
carRental.cars[0] = petrol_cars

diesel_cars = []
for x in range (8):
    diesel_cars.append(fillCarDetails(data, index, DieselCar()))
    index += 1    
carRental.cars[1] = diesel_cars

electric_cars = []
for x in range (4):
    electric_cars.append(fillCarDetails(data, index, ElectricCar()))
    index += 1    
carRental.cars[2] = electric_cars  

hybrid_cars = []
for x in range (4):
    hybrid_cars.append(fillCarDetails(data, index, HybridCar()))
    index += 1    
carRental.cars[3] = hybrid_cars

# DBS car rental implementation    
id = 0
while True:
    showMainMenu()            
    try:
        # dealing with main menu choice
        choice = int(raw_input("Enter choice: > "))
        if choice < 1 or choice > 2:
            print "\nInvalid choice. Try again."            
            continue 
        # dealing with rents
        if choice == 1:
            showNextMenu() 
            #dealing with car type
            type = int(raw_input("Enter type of car: > "))
            if type < 1 or type > 4:
                print "\nInvalid type of car."
                if raw_input("\n  Q to quit or Enter to return to main menu ").lower() == 'q':
                    break                
                continue
            type -= 1 
            # checking car type is available
            if len(carRental.cars[type]) == 0:
                print "\nSorry no car of that type to rent. Try again."
                if raw_input("\n  Q to quit or Enter to return to main menu ").lower() == 'q':
                    break                
                continue    
            # renting a car
            print "Renting a car"  
            # dealing with returning customers
            if raw_input("Are you a returning customer? y/n > ").lower() == 'y':
                previousId = int(raw_input("Enter customer id: > "))
                customer = carRental.getCustomer(previousId)               
                print "\nCustomer name:", customer.getName()
                if customer.getCar() != None:
                    print "\nSorry you can't rent a car till you return the one you are still renting."
                    if raw_input("\n  Q to quit or Enter to return to main menu ").lower() == 'q':
                        break
                    continue
            else: 
                # dealing with new customers
                customer = Customer()
                customer.setName(raw_input("Enter customer name: > "))                
                customer.setId(str(id))
                print "\nFor customer:", customer.name, "\nCustomer id is:", customer.id, "\nNeeded when returning to DBS Car Rental to identify yourself."
                carRental.addCustomer(customer) 
                id += 1
            # renting transactions
            print "\nBooking fee of", BOOKINGFEE, "required."
            raw_input("Press Enter to continue with payment.")
            customer.makePayment(BOOKINGFEE)
            carRental.receivePayment(BOOKINGFEE)
            print "\nPayment received. \nThank you. \nCar is allocated."            
            car=carRental.rentCar(type)
            customer.rentCar(car)
            printTransactionDetails(customer, car)
            print "\nThank you for your business." 
        # dealing with returns
        elif choice == 2:
            print "Returning a car"
            try:
                # dealing with returning customers
                previousId = int(raw_input("Enter customer id: > "))                            
                customer = carRental.getCustomer(previousId)                               
                print "\nCustomer name:", customer.getName()
                # checking they have a car to return
                if customer.getCar() == None:
                    print "\nSorry you don't have a car to return. Try again."
                    if raw_input("\n  Q to quit or Enter to return to main menu ").lower() == 'q':
                        break
                    continue
                else:
                    # returning transactions
                    days = enterConvertValidate("Enter number of days of car rental: > ")
                    miles = enterConvertValidate("Enter number of miles travelled: > ")                    
                    customer.moveCar(customer.getCar(), miles)                    
                    car = customer.returnCar()                    
                    type = car.getType()
                    carRental.returnCar(type, car)
                    print "\nCar returned. \nInspection passed.\nInformation on days rented and miles travelled match our records and inspection. \nThank you."
                    dailyRate = days * DAILYRATE
                    mileageSurcharge = calculateMileageSurcharge(miles)
                    payment = dailyRate + mileageSurcharge
                    print "\nPayment of:", payment, "required based on days rented and miles travelled."
                    raw_input("Press Enter to continue with payment.")
                    customer.makePayment(payment)
                    carRental.receivePayment(payment)
                    print "\nPayment received. \nThank you for your business." 
                    printTransactionReceipt(customer, dailyRate, mileageSurcharge)                                      
            except:
                print "\nSorry invalid id. Try again."                  
        if raw_input("\n  Q to quit or Enter to return to main menu ").lower() == 'q':
            break
    except:
        print "\nInvalid entry. Try again."
        if raw_input("\n  Q to quit or Enter to return to main menu ").lower() == 'q':
            break
print "\nThank you. Have a nice day."
