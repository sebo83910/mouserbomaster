import csv
import mouserapi as mapi
from time import sleep


with open('test.csv', newline='') as csvfile:
    parts = []
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
        #print('%3.1f'%(i+1/totalrows*100),'%',end="\r")#,flush='true')
        print('Searched:',(i+1),'/',totalrows,' - Searching for: ',(row['Designation']),'                   ',end='\r',flush='true')
        if(i>65):
            parts.append(mapi.SearchShort(row['Designation']))
            sleep(2)
    print('')
    print(parts[0])
    print(parts[0][0].keys())



#print(row['Package'], row['Quantity'], row['Id'], row['Designation'])
