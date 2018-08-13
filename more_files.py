from sys import argv
from os.path import exists

script, from_file, to_file = argv

in_file = open(from_file)
in_data = in_file.read()

print(f'The input file is {len(in_data)} bytes long')

print(f'Does the output file exist? {exists(to_file)}')
print('Hit RETURN to continue....')

input()

out_file = open(to_file, 'w')
out_file.write(in_data)

print('Done')

out_file.close()
in_file.close()
