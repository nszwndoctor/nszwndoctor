# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan`s abbreviation is :", states['Michigan'])
print("Florida`s abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    
# now do both at the same time
print('-' * 10)
for abbrev, city in list(states.items()):
    print(f"{abbrev} has the city {city}")

# now do tboth at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")
    
print('-' * 10)
# safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas. ")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")

"""
字典是又一种数据结构，和列表一样，它是编程中最常用的数据结构之一。
字典的用处是把你要存储的东西和你的键映射 或者关联起来。
再强调一次，程序员说的“字典”和我们用来查字的字典差不多，
所以我们可以以实际的字典为例说明一下。

列表和字典有何不同？
列表是一些项的有序排列，而字典是将一些项（键）对应到另外一些项（值）的数据结构。
字典能用在哪里？
各种需要通过某个值去查看另一个值的场合。事实上，你也可以把字典叫“查找表”。
列表能用在哪里？
列表是专供需要有序排列的数据使用的。只要知道索引就能查到对应的值了。


"""    
    