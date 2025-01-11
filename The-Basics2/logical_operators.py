# and = both needs to be true
# or = at least one needs to be true
# and not = both has to be true. 

has_high_income = False
has_good_credit = True

if has_high_income and has_good_credit:
    print("You are elgible for the loan!")


if has_good_credit and not has_high_income:
    print("You are elgible for some type of government help!")