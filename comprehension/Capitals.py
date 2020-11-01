countries = input().split(', ')
capitals = input().split(', ')
result = {country: capital for country, capital in zip(countries, capitals)}
[print(f'{key} -> {value}') for key, value in result.items()]
