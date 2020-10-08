"""
A traveler on a visit to India is in need of some Indian Rupees (INR) but he has money belonging to another currency. 
He wants to know how much money he should provide in the currency he has, to get the specified amount in INR.

Write a python program to implement a currency calculator which accepts the amount needed in INR and the name of the currency which the traveler has. 
The program should identify and display the amount the traveler should provide in the currency he has, to get the specified amount in INR.

Note: Use the forex information provided in the table below for the calculation. Consider that only the currency names mentioned in the table are valid. For any invalid currency name, display -1.

+-------------------+-------------------------+
|      Currency     |  Equivalent of 1.00 INR |
+-------------------+-------------------------+
|        Euro       |          0.01417        |
+-------------------+-------------------------+
|   British Pound   |          0.0100         |
+-------------------+-------------------------+
| Australian Dollar |          0.02140        |
+-------------------+-------------------------+
|  Canadian Dollar  |          0.02027        |
+-------------------+-------------------------+
"""
#PF-Tryout
#Assignment 18: Mandatory - Level 2

def convert_currency(amount_needed_inr,current_currency_name):
    converter = {
        'Euro': 0.01417,
        'British Pound': 0.0100,
        'Australian Dollar': 0.02140,
        'Canadian Dollar':0.02027
    }
    for Currency,Equivalent in converter.items():
        if Currency == current_currency_name:
            current_currency_amount = amount_needed_inr * Equivalent
            return current_currency_amount
    #write your logic here
    return -1

#currency_needed=convert_currency(2000,"Euro")
currency_needed=convert_currency(3500,"British Pound")
if(currency_needed!= -1):
    print(currency_needed )
else:
    print("Invalid currency name")
