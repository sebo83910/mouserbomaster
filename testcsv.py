import csv
import mouserapi as mapi
from time import sleep
import xlsxwriter

workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet('BOM')
datasheet = workbook.add_worksheet('Prices')
# Start from the first cell. Rows and columns are zero indexed.
rowno = 2
colno = 2
bold = workbook.add_format({'bold': 1})
worksheet.write('A1','ID',bold)
worksheet.write('B1','Part#',bold)
worksheet.write('C1','Price',bold)
worksheet.write('D1',' @ ',bold)
worksheet.write('E1','Quantity',bold)
worksheet.write('F1','Total Price',bold)
worksheet.write('G1','Description',bold)

with open('test.csv', newline='') as csvfile:
    parts = []
    totalrows = 1
    spamreader = csv.DictReader(csvfile,fieldnames=('Id','Designator','Package','Quantity','Designation','Supplier','ref'),delimiter=';')
    #rowhhs = list(spamreader)
    #totalrows = len(rowhhs)
    #print(totalrows)
    for row in spamreader:
        totalrows+=1
    print('Found ',totalrows,' parts')
    csvfile.seek(0)
    spamreader = csv.DictReader(csvfile,fieldnames=('Id','Designator','Package','Quantity','Designation','Supplier','ref'),delimiter=';')
    for i,row in enumerate(spamreader):
        #print('%3.1f'%(i+1/totalrows*100),'%',end="\r")#,flush='true')
        if(i>0):
            print('Searched:',(i+1),'/',totalrows,' - Searching for: ',(row['Designation']),'                   ',end='\r',flush='true')
            worksheet.write('A%d'%(i+1),row['Designator'])
            worksheet.write('D%d'%(i+1),row['Designation'])
            worksheet.write('E%d'%(i+1),row['Quantity'])
            #if(i<4):
            parts.append(mapi.SearchShort(row['Designation']))
            sleep(2)
    print('')
    #print(parts[0])
    #print(parts[0][0].keys())



partnumber = []
prices = []
testtabel = []
b = 1
for part in (parts):
    for p in part:
        print(p['Part'],p['Price'])
        partnumber.append(p['Part'])
        prices.append(p['Price'])
        testtabel.append([p['Part'],p['Price']])
        datasheet.write('A%d'%b,p['Part'])
        datasheet.write('B%d'%b,p['Price'])
        datasheet.write('C%d'%b,p['Description'])
        datasheet.write('D%d'%b,p['Quantity'])
        b += 1

    worksheet.data_validation('B%d'%rowno,{'validate': 'list','source':partnumber})
    #print('=C%d*F%d'.format(rowno,rowno))
    worksheet.write_formula('C%d'%rowno,'=VLOOKUP(B%d,Prices!A1:Prices!D1000,2,FALSE)'%rowno) #PRICE
    worksheet.write_formula('G%d'%rowno,'=VLOOKUP(B%d,Prices!A1:Prices!D1000,3,FALSE)'%rowno) #DESCRIPTION
    worksheet.write_formula('D%d'%rowno,'=VLOOKUP(B%d,Prices!A1:Prices!D1000,4,FALSE)'%rowno) #QUANTITY FOR PRICE
    worksheet.write_formula('F%d'%rowno,'=IFERROR(C%d*D%d,0)'%(rowno,rowno)) #TOTAL PRICE

    #worksheet.data_validation('C%d'%rowno,{'validate': 'list','source':prices})
    partnumber = []
    prices = []
    #worksheet.write_string(row,col,part[0]['Part'])
    #worksheet.data_validation(firstrow=rowno,firstcol=colno,{'validate': 'list','source':[part[0]['Part']]})
    #worksheet.data_validation('A1',{'validate': 'list','source':[part[]['Part']]})
    #worksheet.write(rowno,colno,(part[0]['Part']+'-'+part[0]['Description']))
    rowno += 1
worksheet.write_string('E%d'%rowno,'TOTAL:')
worksheet.write_formula('F%d'%rowno,'=SUM(F2:F%d)'%(rowno-1))

workbook.close()
#print(testtabel)
#print(row['Package'], row['Quantity'], row['Id'], row['Designation'])
