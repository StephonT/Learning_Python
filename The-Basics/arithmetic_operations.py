# In python, you are able to add, subtract, multiply and divide. There are 3 ways to divide. By using '/' and '//'. The '/' character will give you a float number while '//' will give you a whole number. The 3rd way is with the '%' sign. It prints the remainder

print(10 / 3 ) 
# This will print 3.333333333333335
print(10 // 3 )
# This will print 3
print(10 % 3)
# This will print the remainder

# EXPONENTS
print(10 ** 3)
# This reads 10 to the power of 3

# Augmented Assignment Operator (+=)
x = 10
x = x + 3
# Python will interperate this as x = 10 and will add 10 + 3. The sum will be the new variable x.
print(x)
#This is how you can increment a number

# The same can be done with the Augmented Assignment Operator
x += 3
print(x)

# Operator Precedence
x = 10 + 3 * 2 ** 2
print(x)
# Python knows to solve in order of operator Precedence
# parenthesis
# exponentation 2 ** 3 
# multiplication or division 
# addition or subtraction 