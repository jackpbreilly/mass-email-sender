from multiprocessing import Pool
import time
import csv
import datetime

def callProcessRow(row):
    processRow(row)

def processRow(row):
    email = str(row)
    print(email+"\n")

class processCSV():

    def __init__(self, fileName):
        self.fileName = fileName

    def getRowCount(self):
        with open(self.fileName) as f:
            for i, l in enumerate(f):
                pass
        self.rowCount = i

    def selectChunkSize(self):
        if(self.rowCount>10000):
            self.chunkSize = 100
            return
        if(self.rowCount>5000):
            self.chunkSize = 500
            return
        self.chunkSize = 10
        return

    def processRows(self):
        listRows = []
        count = 0
        with open(self.fileName,mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                listRows.append(row)
                if(len(listRows) == self.chunkSize):
                    p.map(callProcessRow, listRows)
                    del listRows[:]

    def startProcess(self):
        self.getRowCount()
        self.selectChunkSize()
        self.processRows()


start = time.time()

p = Pool(4)
ob = processCSV("emailList.csv")
ob.startProcess()

end = time.time()

print("Time taken to execute " + str(end - start) + "s")





