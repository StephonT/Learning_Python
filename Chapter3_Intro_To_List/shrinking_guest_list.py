guest_list = ["jahhad", "robert", "shaq"]
print(guest_list)


# append() can be used
# guest_list.append('lebron')
# guest_list.append('evelyn')
# guest_list.append('denzel')
# print(guest_list)

# insert() can be used as well
guest_list.insert(0, 'lebron')
guest_list.insert(2, 'evelyn')
guest_list.append('denzel')
print(guest_list)
print("\nWow! Now you can only invite two people from your list.")

print(f'Sorry {guest_list.pop(0).title()}, I cannot invite you to dinner.')
print(f'Sorry {guest_list.pop(-1).title()}, I cannot invite you to dinner.')
print(f'Sorry {guest_list.pop(1).title()}, I cannot invite you to dinner.')
print(f'Sorry {guest_list.pop(1).title()}, I cannot invite you to dinner.')

print(f'\n{guest_list[0].title()}, you are still invited to dinner tonight.')
print(f'\n{guest_list[1].title()}, you are still invited to dinner tonight.')

# Use the del statement to empty the list
del guest_list[0]
del guest_list[0]
print(guest_list)
