def city_details(city_name, country_name, population=''):
    if population:
        return ', '.join((city_name.title(), country_name.title() + ' ' + '-' + ' ' + 'population' + ' ' + '{}'.format(population)))
    else:
        return ', '.join((city_name.title(), country_name.title()))

print(city_details('Nairobi', 'kenya'))
