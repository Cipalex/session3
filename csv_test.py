import csv


data = []

# Read file and print it
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)
        # Add data into a list
        data.append(row)


print(data)


# Modify data from list
for entry in data[1:]:
    entry[2] = str(int(entry[2]) + 10)


print(data)


# Modify file
with open('data.csv', mode='w') as csv_file:
    csv_write = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_write.writerows(data)
