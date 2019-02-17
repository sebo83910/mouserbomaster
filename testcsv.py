import csv
import mouserapi as mapi
from time import sleep


with open('test.csv', newline='') as csvfile:
    totalrows = 1
    spamreader = csv.DictReader(csvfile,fieldnames=('Id','Designator','Package','Quantity','Designation','Supplier','ref'),delimiter=';')
    #rowhhs = list(spamreader)
    #totalrows = len(rowhhs)
    #print(totalrows)
    for row in spamreader:
        totalrows+=1
    print(totalrows)
    csvfile.seek(0)
    spamreader = csv.DictReader(csvfile,fieldnames=('Id','Designator','Package','Quantity','Designation','Supplier','ref'),delimiter=';')
    for i,row in enumerate(spamreader):
        if(i>0):
            print(i+1,'/',totalrows)
            mapi.SearchShort(row['Designation'])
            sleep(2)


#print(row['Package'], row['Quantity'], row['Id'], row['Designation'])
