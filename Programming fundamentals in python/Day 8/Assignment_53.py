"""
Assume that a poem is given. Write the regular expressions for the following:
Print how many times the letter 'v' appears in the poem.
Remove all the newlines from the poem and print the poem in a single line.
If a word has 'ch' or 'co', replace it with 'Ch' or 'Co'.
If the pattern has characters 'ai' or 'hi', replace the next three characters with *\*.
"""

#PF-Assgn-53
#This verification is based on string match.
import re
poem='''
It takes strength for being certain,
It takes courage to have doubt.
It takes strength for challenging alone,
It takes courage to lean on another.
It takes strength for loving other souls,
It takes courage to be loved.
It takes strength for hiding our own pain,
It takes courage to help if it is paining for someone.
'''
#Note: Triple quotes can be used to enclose Strings which has lines of text.

#Write your logic here for question 1

print(poem.count("v"))
print()
k=poem
k="\n"+k
print(k.replace("\n",""))
c=poem.replace("co","Co")
c=c.replace("ch","Ch")
print(c)
poem=re.sub(r"ai...",r"ai*\*",poem)
poem=re.sub(r"hi...",r"hi*\*",poem)
print(poem)

