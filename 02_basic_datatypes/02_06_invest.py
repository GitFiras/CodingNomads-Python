'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
# Interest over time formula: A = P ( 1 + rt)
# P = Principal amount (=invest)
# r = interest rate in % per period (=interest)
# t = amount of time periods (=years)

print("Welcome to your investment calculator!")
invest = input("Please enter the amount you would like to invest in EUR : ")
invest = int(invest)
years = input("Please enter the number of year you would like to invest : ")
years = int(years)
interest = float(0.021)
ROI = invest * ((int(1) + ( interest * years)))
print("The interest rate per year is : ", end='')
print(interest)

print("Your projected return on investment is : ", end='')
print(invest * (1 + (interest * years)))

print("Your projected return on investment after 1 year is : ", end='')
print(round(invest * (1 + (interest * 1)), 2))

print("Your projected return on investment after 2 years is : ", end='')
print(round(invest * (1 + (interest * 2)), 2))
