# the dictopnary data structure is mutable
# a = {key : value}

mammad = {'age': 28,
          'cities': ['shz', 'teh'],
          'sport': 'mountaineering'}

gholi = {'age': 29,
         'cities': ['yzd', 'tbrz'],
         'sport': 'soccer'}

mammad['age']
mammad['cities']

mammad['food'] = 'kebab'



# --------------- methods ---------------------

a = mammad.get('age', 'not assigned')
print(a)


for key, value in mammad.items():
    print(f"{key} is {value}")


for key in mammad.keys():
    print(key)


for value in mammad.value():
    print(value)


# dictionary in list

# list in dictionary

# dictionary in dictionary

