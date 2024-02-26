favorite_places = {
    'Autumn': ['Florence', 'Wetland', 'Mountains'],
    'Serge': ['New Jersey', 'Cemetary'],
    'Steven': ['Weaverville', 'National Park', 'Farm']
}

for person, places in favorite_places.items():
    print(f"{person}'s favorite places are: {', '.join(places)}")