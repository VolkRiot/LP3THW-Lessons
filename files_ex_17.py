import sys
import os

script, from_file, to_file = sys.argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line
indata = open(from_file).read()
print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {os.path.exists(to_file)}")
input("When ready. hit ENTER to proceed")
out_file = open(to_file, "w")
out_file.write(indata)

print("Alright all done")
out_file.close()
