aliens = []

for alien in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print('...')

# Show the total number of aliens
print(f"The total number of aliens created are: {len(aliens)}")

for alien in aliens[:6]:
    if alien['color'] == 'green':
        alien['color'] = 'red'
        alien['points'] = 10
        alien['speed'] = 'medium'
print(f"\nRed Aliens: {aliens[:6]}")

for alien in aliens[0:3]:
    if alien['color'] == 'red':
        alien['color'] = 'yellow'
        alien['points'] = '15'
        alien['speed'] = 'fast'
print(f"\nYellow Aliens : {aliens[0:3]}")
