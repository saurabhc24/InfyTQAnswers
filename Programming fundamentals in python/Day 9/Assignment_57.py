"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

Write a python program to find and display the number of circular primes less than the given limit.
"""

#PF-Assgn-57
def check_prime(number):
    return number > 1 and all(number % i != 0 for i in range(2, number))
    
def rotations(num):
    rotated = []
    m = str(num)
    for i in m:
        rotated.append(int(m))
        m = m[1:] + m[0]
    return rotated

def get_circular_prime_count(limit):
    counter = 0 

    for number in range(1, limit):
        if all(check_prime(number) for number in rotations(number)): 
            counter += 1 
    return counter
#Provide different values for limit and test your program
print(get_circular_prime_count(1000))







