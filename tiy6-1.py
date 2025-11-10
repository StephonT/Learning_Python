person = {
    "first_name": "stephon",
    "last_name": "treadwell",
    "age": 34,
    "city": "north brunswick"
}

fname = person['first_name']
lname = person['last_name']
age = person['age']
city = person['city']

print(fname.title())
print(lname.title())
print(age)
print(city.title())

# Favorite Numbers

favorite_numbers = {
    "jen": 55, "name": 'jen',
    "sarah": 15,
    "eric": 3, 
    "jason": 33
}

print(f"Jen's favorite number is {favorite_numbers['jen']}")
print(f"Sarah's favorite number is {favorite_numbers['sarah']}")
print(f"Erics's favorite number is {favorite_numbers['eric']}")
print(f"Jason's favorite number is {favorite_numbers['jason']}")

print("Sarah")
print(f"-Favorite Number: {favorite_numbers['sarah']}")
print(f"{favorite_numbers['name']}")

name_value = favorite_numbers.get("name", "Name does ot exist")

