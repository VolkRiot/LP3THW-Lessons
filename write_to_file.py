from sys import argv

script, filename = argv

print(f'Were going to erase {filename}')
print('If you dont want that hit CTRl-C (^C)')
print('If you approve then hit RETURN')

input('?')

print('Opening the file...')
target = open(filename, 'w')

print('Truncating the file')
target.truncate()

print('Enter three new lines')
line1 = input('Line1: ')
line2 = input('Line2: ')
line3 = input('Line3: ')

print('Writing the lines to the file')
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print('Finally we close it')
target.close()
