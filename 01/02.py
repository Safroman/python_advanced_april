countries_dict = {'Ukraine': 'Kiev', 'Canada': 'Ottava', 'Germany': 'Berlin'}

countries_list = ['Ukraine', 'Canada', 'Germany', 'USA']

for country in countries_list:
    if country in countries_dict.keys():
        print(countries_dict[country])
        # v.2
        print(countries_dict.get(country))
