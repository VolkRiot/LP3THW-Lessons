import sys

script, filename = sys.argv

txt = open(filename)

print(f'Here is your file {filename}')
print(txt.read())

txt.close()
