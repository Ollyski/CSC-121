rivers = {'piave': 'Italy', 'srepok': 'Vietnam', 'Amur': 'China'}

for river, country in rivers.items():
    print(f"The {river.capitalize()} runs through {country}.")

print("\nRivers:")
for river in rivers.keys():
    print(river.capitalize())

print("\nCountries:")
for country in rivers.values():
    print(country)
    