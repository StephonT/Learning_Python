# len() = counts the number of characters in a string

# course = 'Python for Beginners'
# print(len(course))

# There are also methods that can be used with the dot notation. Just be sure to not forget the parenthesis at the end of each method. 
# print(course.upper())

# print(course.lower())

# print(course)

# the find() method finds the character in which you are looking for and will print the index. Find method is sensitive! You can pass a series of strings also
# print(course.find('P'))
# This will print 0

# print(course.find('Beginners'))
#This will print 11 because it starts at the 11th index

#.replace replaces a word in which you indicate
# print(course.replace('Beginners', 'Absolute Beginners'))

# If you want to check the existence of a character or sequence of characters, use the 'in' operator
# print('Python' in course)
# This expression is a boolean expression.

facts = 'Stephon is the greatest!'
print(facts)
print(facts.find('!'))
print(len(facts))
print(facts.lower())
print(facts.upper())


