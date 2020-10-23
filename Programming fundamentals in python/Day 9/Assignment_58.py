"""
Use Luhn algorithm to validate a credit card number.

A credit card number has 16 digits, the last digit being the check digit. A credit card number can be validated using Luhn algorithm as follows:

Step 1a: From the second last digit (inclusive), double the value of every second digit.
Suppose the credit card number is 1456734512345698.
Take the double of 9,5,3,1,4,7,5 and 1
i.e., 18, 10, 6, 2, 8, 14, 10 and 2

Note: If any number is greater than 9, then sum the digits of that number.
i.e., 9, 1, 6, 2, 8, 5 ,1 and 2

Step 1b: Sum the numbers obtained in Step 1a.
i.e., 34

Step 2: Sum the remaining digits in the credit card and add it with the sum from Step 1b.
i.e., 34 + (8+6+4+2+5+3+6+4) = 72

Step 3: If the total is divisible by 10 then the number is valid else it is not valid.

Write a function, validate_credit_card_number(), which accepts a 16 digit credit card number and returns true if it is valid as per Luhn’s algorithm or false, if it is invalid. Also write the pytest test cases to test the program.
"""


#PF-Assgn-58
def validate_credit_card_number(card_number):
    card=str(card_number)
    l=[]
    if len(card)==16:
        for i in card[-2::-2]:
            n=int(i)*2
            if n>9:
                n1=n%10+n//10
                l.append(n1)
            else:
                l.append(n)
        return (sum(l)+sum(list(map(int,card[-1::-2]))))%10==0
    else:
        return False
    

card_number= 4539869650133101 #4539869650133101  #1456734512345698 # #5239512608615007
result=validate_credit_card_number(card_number)
if(result):
    print("credit card number is valid")
else:
    print("credit card number is invalid")
