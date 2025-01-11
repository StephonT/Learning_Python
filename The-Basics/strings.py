#This file will be about strings

course = 'Python Course for Beginners'
print(course)

# The following is how you create a string with multiple lengths
#Need to use triple quotes

course = '''
Hi John,

Here is our first email to you.

Thank you,
Stephon.
'''

print(course)

#How to index. In python, the first character starts with zero. A negative number can also be used to print the letters from the end of the word. You use the index by using square brackets []. You can extract multiple characters by using colon in the square brackets

example_1 = 'Stephon'
example_2 = 'Treadwell'

print(example_1[0])
print(example_2[-1])
print(example_1[0:5])
print(example_2[1:-1])
