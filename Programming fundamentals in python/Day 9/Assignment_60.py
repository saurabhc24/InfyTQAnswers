"""
Write a python function, remove_duplicates() which accepts a string and removes all duplicate characters from the given string and return it.


Also write the pytest test cases to test the program.

+-----------------------------+-----------------+
|         Sample Input        | Expected Output |
+-----------------------------+-----------------+
| 1122334455ababzzz@@@123#*#* |   12345abz@#*   |
+-----------------------------+-----------------+
"""

#PF-Assgn-60
def remove_duplicates(value):
    rmvdp = []
    list1=list(value)
    for i in list1:
        if i not in rmvdp:
            rmvdp.append(i)
    return "".join(rmvdp)
    
    #start writing your code here

print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))







