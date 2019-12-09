import sys

old_file = open(sys.argv[1], 'r')
new_file = open(sys.argv[2], 'w+')
print("processing")
for line in old_file:
    if "----------------------------------------------------------------------" in line:
        continue
    else:
        new_file.write(line)

new_file.close()