# Mandatory to close the file after read
fh = open('module1.py', 'r')
print(fh.read())
fh.close()

# 'With' does the close automatically
with open('module1.py', 'r') as fh:
    print(fh.read())

with open('module1.py', 'r') as fh:
    for line in fh.readlines():
        print(line)


with open('c:\\tmp2\\asd2.txt', 'a') as fh:
    fh.write('Line1\n')
    fh.writelines(['Line2\n', 'Line3\n'])