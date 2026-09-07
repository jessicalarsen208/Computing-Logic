Python 3.12.9 (tags/v3.12.9:fdb8142, Feb  4 2025, 15:27:58) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #initalization
... 
... 
... #constants
... #service charge and room rates
... INITIAL_SERVICE_CHARGE = 40
... SERVICE_CHARGE_PER_BATHROOM = 15
... SERVICE_CHARGE_PER_ROOM = 10
... 
... #calculated values
... 
... 
... 
... #declaration of user input variables
... 
... 
... 
... #get data
... customerName = input("Enter customer name: ")
... numOfBathrooms = int(input("Enter number of bathrooms: "))
... numOfRooms = int(input("Enter number of rooms: "))
... 
... #collecting the input from the user
... 
... 
... #process data
... #calculating costs
... totalCostOfRooms = SERVICE_CHARGE_PER_ROOM * numOfRooms
... totalCostOfBathroom = SERVICE_CHARGE_PER_BATHROOM * numOfBathrooms
... totalCostOfAllRooms = totalCostOfRooms + totalCostOfBathroom + INITIAL_SERVICE_CHARGE
... 
... #output information
... #displaying the information
... #print
... print ("--- Cleaning Service Summary ---")
... print ("Customer's Last Name:", customerName)
print ("Number of bathrooms to be cleaned:", numOfBathrooms)
print ("Cost to clean bathrooms: $" + str(totalCostOfBathroom))
print ("Number of other rooms to be cleaned:", numOfRooms)
print ("Total cost for cleaning other rooms: $" + str(totalCostOfRooms))
print ("Total cost for bathrooms and other rooms: $" + str(totalCostOfAllRooms))



#final message
print("\nProgram complete.")
