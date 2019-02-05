import requests
import xml.etree.ElementTree as ET
#import xml.dom.minidom


print('Hello World\n\n\n')

url = 'http://api.mouser.com/service/searchapi.asmx?wsdl'
#url = 'http://api.mouser.com/service/SearchByKeyword'

data = '<?xml version="1.0" encoding="utf-8"?>\
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">\
<soap:Header>\
<MouserHeader xmlns="http://api.mouser.com/service">\
<AccountInfo>\
<PartnerID>9c3c2752-29bb-4b9a-9679-e5fb6ade3a8c</PartnerID>\
</AccountInfo>\
</MouserHeader>\
</soap:Header>\
<soap:Body>\
<SearchByPartNumber xmlns="http://api.mouser.com/service">\
<mouserPartNumber>MAX423</mouserPartNumber>\
<partSearchOptions>BeginsWith</partSearchOptions>\
</SearchByPartNumber>\
</soap:Body>\
</soap:Envelope>'

#urldata = url+data   863-NTR3C21NZT1G
#print(urldata,'\n\n')

r = requests.post(url,data=data,headers={'Content-type':'text/xml'})
print('HTTP Response: \t',r.status_code,r.reason,'\n')
#e = xml.etree.ElementTree.parse(r).getroot()
tree = ET.ElementTree(ET.fromstring(r.text))
#print(tree.getroot())
root = tree.getroot()

body = root.getchildren()
#print(body[0].tag)
el1 = body[0].getchildren()
#print(el1)
el2 = el1[0].getchildren()
#print(el2)
el3 = el2[0].getchildren()


    
#print(el3[0].items)


#print(el3)
numOfParts = el2[0].find('{http://api.mouser.com/service}NumberOfResult').text
print('Number of parts found: \t',numOfParts)
parts = el3[1].getchildren()
#print('parts: ',parts)
part1 = parts[0]

parts = root.findall('{http://schemas.xmlsoap.org/soap/envelope/}Body/{http://api.mouser.com/service}SearchByPartNumberResponse/{http://api.mouser.com/service}SearchByPartNumberResult/{http://api.mouser.com/service}Parts/{http://api.mouser.com/service}MouserPart')

print('--------------------------')
for part in parts:
    if 'N/A' not in part.find('{http://api.mouser.com/service}MouserPartNumber').text and part.find('{http://api.mouser.com/service}Availability') is not None:
        print('\n')
        print('Mouser part #:\t',part.find('{http://api.mouser.com/service}MouserPartNumber').text)
        print('Availability: \t',part.find('{http://api.mouser.com/service}Availability').text)
        print('LeadTime: \t',part.find('{http://api.mouser.com/service}LeadTime').text)
        print('OnOrder: \t',part.find('{http://api.mouser.com/service}FactoryStock').text)
    else:
        print('\n')
        #print('Mouser part #:\t',part.find('{http://api.mouser.com/service}MouserPartNumber').text)
        print('Found N/A part')
print('--------------------------')



#print('Availability: ',part1.find('{http://api.mouser.com/service}Availability').text)
#print('LeadTime: ',part1.find('{http://api.mouser.com/service}LeadTime').text)
#print('OnOrder: ',part1.find('{http://api.mouser.com/service}FactoryStock').text)


#part1.attrib['{http://api.mouser.com/service}Availability'])
#p1root = part1.getchildren()
#print(part1.find('{http://api.mouser.com/service}Availability'))

#for part in parts[0].findall("./Availability"): #/SearchByPartNumberResult/Parts/MouserPart/[Availability!='0']
 #   print('wow')
    
    
#print(part.attrib)


#for avail in e.getroot().findall('SearchByPartNumberResult'):
    #print(avail.find('Availability').text)
    #print(len(avail))



#print(r.content)
#dom = xml.dom.minidom.parseString(r.content)
#print(dom.childNodes[0].firstChild.value)

