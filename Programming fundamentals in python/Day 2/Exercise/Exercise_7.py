"""
The flight ticket rates for a round-trip (Mumbai->Dubai) were as follows:
Rate per Adult: Rs. 37550.0
Rate per Child: 1/3rd of the rate per adult
Service Tax: 7% of the ticket amount (including all passengers)
As it was a holiday season, the airline also offered 10% discount on the final ticket cost (after inclusion of the service tax).
Find and display the total ticket cost for a group which had adults and children.

Test the program with different input values for number of adults and children.

 __________________________________________________________________________
|           sample Inputs               |          Expected Output        | 
___________________________________________________________________________
| Number of adults | Number of children |                                 |
___________________________________________________________________________
|         5        |          2         |   Total Ticket Cost: 204910.35  |
___________________________________________________________________________
|         3        |          1         |   Total Ticket Cost: 120535.5   |
___________________________________________________________________________

"""
def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    intermediate_result=(no_of_adults*37550.0)+(no_of_children*(37550/3))
    service_tax=(7/100)*intermediate_result
    intermediate_result=intermediate_result+service_tax
    discount=(10/100)*intermediate_result
    total_ticket_cost=intermediate_result-discount
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(3,1)
print("Total Ticket Cost:",total_ticket_cost)
