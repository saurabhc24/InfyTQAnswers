"""
Write a python program that displays a message as follows for a given number:

a. If it is a multiple of three, display "Zip"
b. If it is a multiple of five, display "Zap".
c. If it is a multiple of both three and five, display "Zoom".
d. If it does not satisfy any of the above given conditions, display "Invalid".
"""

#PF-Exer-11

def display(num):
    message=""
    #write your logic here
    if((num%3==0) and (num%5==0)):
        message = "Zoom"
    elif(num%3==0):
        message = "Zip"
    elif(num%5==0):
        message = "Zap"
    else:
      print("Invalid Number")
    return message

#Provide different values for num and test your program
message=display(9)
print(message)