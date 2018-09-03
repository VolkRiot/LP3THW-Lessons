the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# simple for loop

for number in the_count:
    print(f'This is count {number}')

for fruit in fruits:
    print(f'The fruit is {fruit}')

for i in change:
    print(f'The change value is {i}')

elements = []

for i in range(0, 6):
    print(f'Adding element {i} to list')
    elements.append(i)

for i in elements:
    print(f'Element in list is {i}')
