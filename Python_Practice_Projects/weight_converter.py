# In this project, I built a weight converter from pounds to kilos and from kilos to pounds. This takes the user's input answer and convert their weight to either pounds or kilos. 

weight = int(input("Weight: "))

unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    converted = weight * .45
    print(f"You are {converted} kilos")
else: 
    converted = weight / 0.45
    print(f"You are {converted} pounds")


