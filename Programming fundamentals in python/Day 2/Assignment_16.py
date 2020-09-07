"""
You have x no. of 5 rupee coins and y no. of 1 rupee coins. You want to purchase an item for amount z. 
The shopkeeper wants you to provide exact change. You want to pay using minimum number of coins. 
How many 5 rupee coins and 1 rupee coins will you use? If exact change is not possible then display -1.

+-------------------------------------------------------------------+-----------------------------------------+
|                        Sample Input                               |             Expected Output             |
+-----------------------+-----------------------+-------------------+--------------------+--------------------+
| Available Rs. 1 coins | Available Rs. 5 notes | Amount to be made | Rs. 1 coins needed | Rs. 5 notes needed |
+-----------------------+-----------------------+-------------------+--------------------+--------------------+
|           2           |           4           |         21        |          1         |          4         |                                        
+-----------------------+-----------------------+-------------------+--------------------+--------------------+
|          11           |           2           |         11        |          1         |          2         |
+-----------------------+-----------------------+-------------------+--------------------+--------------------+
|           3           |           3           |         19        |                   -1                    |
+-----------------------+-----------------------+-------------------+--------------------+--------------------+


"""
#PF-Assgn-16
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0

    #Start writing your code here
    #Populate the variables: five_needed and one_needed
    five_needed = rupees_to_make//5
    one_needed = rupees_to_make-(5*five_needed)
    if five_needed <= no_of_five and one_needed <= no_of_one:
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    elif ((no_of_five - five_needed)*5) <= (no_of_one - one_needed):
        one_needed = one_needed + ((five_needed - no_of_five)*5)
        five_needed = no_of_five
        if five_needed <= no_of_five and one_needed <= no_of_one:
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed)
        else:
            print(-1)
    else:
            print(-1)


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work

    #print("No. of Five needed :", five_needed)
    #print("No. of One needed  :", one_needed)
    #print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(28,8,5)
