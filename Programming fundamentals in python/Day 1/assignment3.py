# Question : ack and his three friends have decided to go for a trip by sharing the expenses of the fuel equally.
#Write a Python program to calculate the amount (in Rs) each of them need to put in for the complete (both to and fro) journey.
#The program should also display True, if the amount to be paid by each person is divisible by 5, otherwise it should display False. 
#(Hint: Use the relational operators in print statement.)



mileage=12
amount_per_litre=40
distance_one_way=190
per_head_cost=0
divisible_by_five=False

#Start writing your code from here
#Populate the variables: per_head_cost and divisible_by_five
total_distance=distance_one_way*2
petrol = (total_distance/mileage)*amount_per_litre
per_head_cost = petrol/4
if per_head_cost%5==0:
    divisible_by_five=True
#Do not modify the below print statements for verification to work
print(per_head_cost)
print(divisible_by_five)
