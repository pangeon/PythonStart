planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets, "\n")

print('1. The biggest planets in solar system are', planets[4], planets[5], sep=" | ")

print('2. Third planet in solar system is: ' + planets[2])

print('3. Planets after Earth: ', planets[3:])

print('4. Three planets before: ', planets[3], 'are', planets[:3])

print('5. Name', planets[4], 'has', len(planets[4]), 'letters')

print("6.I display planets with using \"loop for\" in:")
for planet in planets:
    print(planet, end=" ")

