# If statements are statements that are executed when a condition is met

# if it's hot
#     It's a hot day
#     Drink plenty of water
# otherwise if it's cold
#     It's a cold day
#     Wear warm clothes
# otherwise
#     It's a lovely day

# Exercise 1

# is_hot = True
# is_cold = False

# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water!")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else:
#     print("It's a lovely day")

# Exercise 2
#Price of a house is $1M
# If buyer has good credit,
#     they need to put down 10%
# Otherwise
#     they need to put down 20%
# Print the down payment 

price = 1000000
good_credit = False
bad_credit = True

if good_credit:
    down_payment = .1 * price
    print(f"Down payment: ${down_payment}")
elif bad_credit:
    down_payment = .2 * price
    print(f"Down payment: ${down_payment}")
else:
    print("You might as well keep renting buddy!")

