"""
Description: Assignment 2
Author: Zalak Punjani 
Date: 26-05-2025
Usage: To display my understanding of module two

"""

import os

# SIMPLE DATA TYPES
# declaring a variable to store a name 
name = input("Enter your name")
os.system(f"echo Hello {name}")  

# The output of the value and the datatype of the variable declared above
print(f"name: {name} type: {type(name)}")

password = "pass12345"
print(password)

# Declaring a variable and assigning it a boolean value
has_license = False 

# the output of the value and datatype of the variable declared above
print(f"has license:{has_license} type: {type(has_license)}")

# Declaring a variable to store current yeah and its value
this_year = 2025

# Output of the year and its value 
print(f"this year: {this_year} type: {type(this_year)}")

# Increasing the value of the stored by this year variable by 1
next_year = this_year + 1

# Output of increase of this_year variable by 1
print(f"next year: {next_year} type: {type(name)}")


# MATHEMATICAL OPERATIONS
# Declaring a variable to store the current PST and GST and defining them as a constant
PST = 0.05     # Actual value: 5% = 0.05
GST = 0.07     # Actual Value: 7% = 0.07

# Declaring a variable to store purchase price of a vehicle and assigning it a value
purchase_price = 85000.00

# Calculating the PST and GST on sale of the vehicle 
federal_tax = purchase_price *GST
provincial_tax =purchase_price *PST  


# Final cost of the vehicle
final_cost = federal_tax + provincial_tax + purchase_price

# The results output showing Purchase Price, provincial tax, federal tax and total
print("Purchase price: {purchase_price} Provincial Tax: {provincial_tax} Federal Tax: {federal_tax} Total:{final_cost}")

#the results in all the values formated to 2 decimal palaces
print(f"Purchase Price: ${purchase_price:,.2f} Provincial Tax: ${provincial_tax:,.2f} Federal Tax: ${federal_tax:,.2f} Total: ${final_cost:,.2f}")


# LISTS
# Declares a variable a new list containing the literal values 1 through 10 inclusive. 
Values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Verifying that the list has been created by using print and showing its data type 

# Prints the list 
print(Values)

# Adding my first name "Zalak" in the list between 5 and 6
Values.insert(5, "Zalak")
print(Values)

# Removing number 9 from the list 
Values.remove(9)
print(Values)

# New list of characters A, B and C
Characters = ['A','B','C']

# Declaring both the lists above into one list without it containing lists
both_lists = Values + Characters

#Printing the output of both_lists
print(both_lists)


# TUPLES
# Declaring a variable to store a tuple that contains names of 4 Canadian provinces
provinces = ('Manitoba', 'British Columbia', 'Ontario', 'Alberta' )

# Showing the data type of the tuple created above and confirming if it was created
print(type(provinces))

# Output showing the tuples 
print(provinces)


# DICTIONARIES
# Declare and store dictionary that has keys 'nickel', 'dime', and 'quarter' with Canadian coin values
currency = { 
    "nickel" : 0.05,
    "dime" : 0.10, 
    "quarter" : 0.25
}

# Verifying that the dictionary was created 
print(type(currency))

# Output of the dictionary created above
print(currency)

# Showing the values of each currency in whole numbers
currency ['nickel'] = 5
currency ['dime'] = 10
currency ['quarter'] = 25

# Output of the values of the currency in whole numbers
print(currency)

# Adding Loonie and Toonie 
currency ['loonie'] = 100
currency ['toonie'] = 200

# printing the final output 
print(currency)

# SETS
# Declare and store set. Assigning it with even numbers between 2 and 20 
even_numbers = {2,4,6,8,10,12,14,16,18,20}

# Verifying that the set has been created
print(type(even_numbers))

#Showing the output of the set itself
print(even_numbers)

# Declare and store set. Assigning it with values representing multiples of 5 between 5 and 20 
multiple_of_5 = {5,10,15,20}

#Showing the output of the set itself
print(multiple_of_5)

# Declaring and store a set that would have unique numbers from both the sets mentioned above
unique_numbers = even_numbers.union(multiple_of_5)
print(unique_numbers)  #shows the output of the unique numbers

# Declaring and store a set that would have common numbers from both the sets mentioned above
common_numbers = even_numbers.intersection(multiple_of_5)
print(common_numbers) #shows the output of the common numbers 

# Declare and store a set that would only show the multiples of 2 in the 1st set and not from the 2nd set 
multiples_of_2 = even_numbers.difference(multiple_of_5)
print(multiples_of_2)  # shows only the multiples of 2 from the 1st set


# Declare and store a set that would only show the multiples of 5 in the 2nd set and not from the 1st set 
multiples_of_5_only = multiple_of_5.difference(even_numbers)
print(multiples_of_5_only)  # shows only the multiples of 2 from the 2nd set

