"""
Write a python program to guess the number in the user's mind.

randrange function of random module can be used to guess the number in user’s mind.

Note: User should think of a number which is in between 1 and 10 (both inclusive).

+---------------------+------------------------------+----------------+--------------------------+
| Random Range values | Sample number in user’s mind | Number guessed |      Expected Output     |
+---------------------+------------------------------+----------------+--------------------------+
|       1 to 10       |               5              |         3      |       Number is low      |
|                     |                              +----------------+--------------------------+
|                     |                              |         7      |        Number is high    |
|                     |                              +----------------+--------------------------+
|                     |                              |         5      | You have got it right!!! |
+---------------------+------------------------------+----------------+--------------------------+

"""

#PF-Tryout

def guess_number(number_in_mind):
    import random
    i=random.randrange(1,11)
    print(i)
    if i<number_in_mind:
        print ('Number is low')
    elif i>number_in_mind:
        print ('Number is high')
    else:
        print ('You have got it right!!!')

guess_number(4)
