# This is the Names assignment - Part I
students = [
{'first_name': 'Michael', 'last_name': 'Jordan'},
{'first_name': 'John', 'last_name': 'Rosales'},
{'first_name': 'Mark', 'last_name': 'Guillen'},
{'first_name': 'KB', 'last_name': 'Tonel'}
]
for element in range(1):
    for value in students:
        print value['first_name'], value['last_name']
