import time
import csv

start = time.time()

### Printing out 1 row in CSV file
with open('emailList.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
            print(f'\t{row[0]}')

end = time.time()

print("Time taken to execute " + str(end - start) + "s")


