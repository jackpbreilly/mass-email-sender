import time
import csv
input_file = "emailList.csv"
start_time = time.time()
data = csv.DictReader(open(input_file))
print("csv.DictReader took %s seconds" % (time.time() - start_time))
