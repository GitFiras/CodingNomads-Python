'codingnomads'.capitalize()

'''
Receive the following arguments from the user:

kilometers to drive
liters-per-kilometer usage of the car
price per liter of fuel
Calculate the cost of the trip and display it to the user in the console.
'''

km = input("Please provide the number of kilometer that you expect to drive in Bali: ")
km = int(km)
car_usage = 0.5 # 0.5 L per KM car usage
Price_Liter = 1 # 1 USD per liter of fuel

Total_Costs_Trip = (int(km * car_usage * Price_Liter))

print("Your expected fuel costs for the entire trip are USD : ", end='')
print(Total_Costs_Trip)


'''
# assignment: print to column 70 of the display:'

s = 'monthy'
right_justify(s)
print(f"{s :>70}")
'''