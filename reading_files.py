import sys

script, filename = sys.argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())


file_again = input("Enter the filename again>")
txt_again = open(filename)
print(txt_again.read())

txt_again.close()

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")
print("Opening the file")
target = open(filename, "w")

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I am going to ask you for three lines")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

target.write(line1 + "\n")
target.write(line2 + "\n")
target.write(line3 + "\n")

print("And finally we close it")
target.close()