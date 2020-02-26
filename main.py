import time
import csv
from multiprocessing import Process


# Building "mailing list"
def generate_csv():
    with open('list.csv', 'w') as f1:
        writer = csv.writer(f1, delimiter=',', lineterminator='\n')
        for i in range(1000000):
            row = "fakeemail" + str(i) + "@email.com"
            writer.writerow([row])

# generic function designed to be customisable to needs.
def x(file_name):
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            print("Emailing: " + str(row[0]))
            #time.sleep(0.5)


def split(filename, directory, perfile):
    with open(filename, "r") as csvfile:
        lines = csv.reader(csvfile)
        i = 0
        file_num = 0
        newfile = open(directory + "/" + "part_" + str(file_num) + ".csv", "w")
        for line in lines:
            i += 1
            newfile.write(','.join(line) + "\n")
            if i > perfile:
                newfile.close()
                i = 0
                file_num += 1
                newfile = open(directory + "/" + "part_" + str(file_num) + ".csv", "w")
        newfile.close()
        return file_num


if __name__ == '__main__':
    # generate_csv()
    # exit(0)
    file_num = split("list.csv", "split", 250000)
    start = time.time()
    processes = []
    for i in range(0, file_num + 1):
        func_args = 'split/part_' + str(i) + '.csv'
        process = Process(target=x, args=(func_args,))
        process.start()
        processes.append(process)


    for i in range(0, file_num + 1):
        processes[i].join()

    end = time.time()

    time_taken_processes = str(end - start)

    start = time.time()
    x("list.csv")
    end = time.time()

    time_taken_full_file = str(end - start)

    print("Time taken to execute using processes " + time_taken_processes + "s")
    print("Time taken to execute using full file " + time_taken_full_file + "s")
