# > (greater than), < (less than), = (equal to), >= (greater than or equal to), <=(less than or equal to) , == , != (not equal)

# if temprature is greater than 30, its a hot day
# otherwise if it's less than 10, it's a cold day
# otherwise, it's neither hot nor cold

temperature = 30

if temperature >= 30:
    print("It's a hot day")
else: 
    print("It's not a hot day")


# if name is less than 3 characters long, name must be at least 3 characters
# otherwise, if it's more than 50 characters long, name can be a maximum of 50 characters
# otherwise, name looks good!

name = "Stephon"

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("You good big bruh!")