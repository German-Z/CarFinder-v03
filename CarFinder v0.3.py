AllowedVehiclesList = [
  'Ford F-150', 
  'Chevrolet Silverado', 
  'Tesla CyberTruck', 
  'Toyota Tundra', 
  'Nissan Titan'
]

#function used to search for vehicles and see if they are authorized.
def truckSearch(AllowedVehiclesList):
  autoSearch = str(input('Please Enter full Vehicle name: '))
  if autoSearch in AllowedVehiclesList:
    print(f'{autoSearch} is an authorized vehicle')
  else:
    print(f'{autoSearch} is not an authorized vehicle, if you received this in error please check the spelling and try again')
    
#function used to add authorized vehicles
def truckAdd(AllowedVehiclesList):
  addTruck = str(input('Please Enter the full Vehicle name you would like to add: '))
  if addTruck:
    print(f' You added "{addTruck}" as an authorized vehicle')
  AllowedVehiclesList.append(addTruck)

#OnLoad menu when program is executed.
menu = '''********************************
AutoCountry Vehicle Finder v0.1
********************************
Please Enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. ADD Authorized Vehicle
4. Exit'''
#if statements for AutoCountry.
while (True):
  print(menu)
  autoInput = int(input('-> '))
  if autoInput == 1:
    print('The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:')
    for vehicle in AllowedVehiclesList:
      print(vehicle)
  if autoInput == 3:
     truckAdd(AllowedVehiclesList)
    
  if autoInput == 2:
     truckSearch(AllowedVehiclesList)

  elif autoInput == 4:
    print('Thank you for using the AutoCountry Vehicle Finder, good-bye!')
    exit()
