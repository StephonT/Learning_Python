guest_list = ["jahhad", "jay-z", "shaq"]
print(f'{guest_list[0].title()}, you are invited to the dinner.')
print(f'{guest_list[1].title()}, you are invited to the dinner.')
print(f'{guest_list[2].title()}, you are invited to the dinner.')


# You can use pop() to remove a position from a list.
# print(guest_list.pop(1))

# You can remove an item from any list using the del statement. You'll no longer have access to the value
del guest_list[1]
print(guest_list)

# You can add to a list using the append()
guest_list.append('jay-z')
print(guest_list)
