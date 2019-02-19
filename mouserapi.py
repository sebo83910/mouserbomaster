class MouserPart:
    partnumber = 'not defined'
    availability = 0





def SearchByPartNumber(keyword):

    import requests
    import xml.etree.ElementTree as ET
    print('Searching for '+keyword+'...\n')

    url = 'http://api.mouser.com/service/searchapi.asmx?wsdl'

    data1 = '<?xml version="1.0" encoding="utf-8"?>\
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
    <mouserPartNumber>'

    data2 = '</mouserPartNumber>\
    <partSearchOptions>BeginsWith</partSearchOptions>\
    </SearchByPartNumber>\
    </soap:Body>\
    </soap:Envelope>'

    data = data1 + keyword + data2

    r = requests.post(url,data=data,headers={'Content-type':'text/xml'})
    print('HTTP Response: \t',r.status_code,r.reason,'\n')
    if(r.status_code == 200):
        tree = ET.ElementTree(ET.fromstring(r.text))
        root = tree.getroot()

        parts = root.findall('{http://schemas.xmlsoap.org/soap/envelope/}Body/{http://api.mouser.com/service}SearchByPartNumberResponse/{http://api.mouser.com/service}SearchByPartNumberResult/{http://api.mouser.com/service}Parts/{http://api.mouser.com/service}MouserPart')

        print('--------------------------')
        for part in parts:
            if 'N/A' not in part.find('{http://api.mouser.com/service}MouserPartNumber').text and part.find('{http://api.mouser.com/service}Availability') is not None:
                print('\n')
                print('Mouser part #:\t',part.find('{http://api.mouser.com/service}MouserPartNumber').text)
                print('Availability: \t',part.find('{http://api.mouser.com/service}Availability').text)
                print('LeadTime: \t',part.find('{http://api.mouser.com/service}LeadTime').text)
                print('OnOrder: \t',part.find('{http://api.mouser.com/service}FactoryStock').text)
                print('Price @',part.find('{http://api.mouser.com/service}PriceBreaks/{http://api.mouser.com/service}Pricebreaks/{http://api.mouser.com/service}Quantity').text,': \t',part.find('{http://api.mouser.com/service}PriceBreaks/{http://api.mouser.com/service}Pricebreaks/{http://api.mouser.com/service}Price').text)
                print('Description: \t',part.find('{http://api.mouser.com/service}Description').text)
            else:
                print('\n')
                #print('Mouser part #:\t',part.find('{http://api.mouser.com/service}MouserPartNumber').text)
                print('Found N/A part')
        print('--------------------------')
        d = dict()
        d['partnumber'] = 2
        return d
    else:
        raise Exception('Mouser API returned: {}'.format(r.status_code)+' - {}'.format(r.reason))
    


def SearchByKeyword(keyword,records):

    import requests
    import xml.etree.ElementTree as ET
    print('Searching for '+keyword+'...\n')

    url = 'http://api.mouser.com/service/searchapi.asmx?wsdl'

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
    <SearchByKeyword xmlns="http://api.mouser.com/service">\
    <keyword>'+keyword+'</keyword>\
    <records>'
    data += str(records)
    data += '</records>\
    <startingRecord>0</startingRecord>\
    <searchOptions>InStock</searchOptions>\
    </SearchByKeyword>\
    </soap:Body>\
    </soap:Envelope>'



    r = requests.post(url,data=data,headers={'Content-type':'text/xml'})
    print('HTTP Response: \t',r.status_code,r.reason,'\n')
    
    if(r.status_code == 200):
        tree = ET.ElementTree(ET.fromstring(r.text))
        root = tree.getroot()

        parts = root.findall('{http://schemas.xmlsoap.org/soap/envelope/}Body/{http://api.mouser.com/service}SearchByKeywordResponse/{http://api.mouser.com/service}SearchByKeywordResult/{http://api.mouser.com/service}Parts/{http://api.mouser.com/service}MouserPart')
        print('--------------------------')
        for part in parts:
            if 'N/A' not in part.find('{http://api.mouser.com/service}MouserPartNumber').text and part.find('{http://api.mouser.com/service}Availability') is not None:
                print('Description: \t',part.find('{http://api.mouser.com/service}Description').text)
                print('Price @',part.find('{http://api.mouser.com/service}PriceBreaks/{http://api.mouser.com/service}Pricebreaks/{http://api.mouser.com/service}Quantity').text,': \t',part.find('{http://api.mouser.com/service}PriceBreaks/{http://api.mouser.com/service}Pricebreaks/{http://api.mouser.com/service}Price').text)
                print('OnOrder: \t',part.find('{http://api.mouser.com/service}FactoryStock').text)
                print('LeadTime: \t',part.find('{http://api.mouser.com/service}LeadTime').text)
                print('Availability: \t',part.find('{http://api.mouser.com/service}Availability').text)
                print('Mouser part #:\t',part.find('{http://api.mouser.com/service}MouserPartNumber').text)
                print('\n')
            else:
                print('Found N/A part')
                #print('Mouser part #:\t',part.find('{http://api.mouser.com/service}MouserPartNumber').text)
                print('\n')
        print('--------------------------')
    else:
        raise Exception('Mouser API returned: {}'.format(r.status_code)+' - {}'.format(r.reason))
    return

def SearchShort(keyword):

    import requests
    import xml.etree.ElementTree as ET
    from collections import OrderedDict
    from operator import itemgetter
    #print('Searching for '+keyword+'...\n')

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
    <SearchByKeyword xmlns="http://api.mouser.com/service">\
    <keyword>'+keyword+'</keyword>\
    <records>'
    data += str(3)
    data += '</records>\
    <startingRecord>0</startingRecord>\
    <searchOptions>InStock</searchOptions>\
    </SearchByKeyword>\
    </soap:Body>\
    </soap:Envelope>'


    #data = data1 + str + data2

    r = requests.post(url,data=data,headers={'Content-type':'text/xml'})
   #print('HTTP Response: \t',r.status_code,r.reason)
    tree = ET.ElementTree(ET.fromstring(r.text))
    root = tree.getroot()

    parts = root.findall('{http://schemas.xmlsoap.org/soap/envelope/}Body/{http://api.mouser.com/service}SearchByKeywordResponse/{http://api.mouser.com/service}SearchByKeywordResult/{http://api.mouser.com/service}Parts/{http://api.mouser.com/service}MouserPart')

    mouserparts = []
    keys = ['Part','Category','Availability','Quantity','Price','Description','FactoryStock','LeadTime']

    if(r.status_code == 200):
        #print('--------------------------')
        i = 0
        for part in parts:
            if 'N/A' not in part.find('{http://api.mouser.com/service}MouserPartNumber').text and part.find('{http://api.mouser.com/service}Availability') is not None:
                #print('\n')
                #print('Mouser part #:\t',part.find('{http://api.mouser.com/service}MouserPartNumber').text)
                #print('Category:\t',part.find('{http://api.mouser.com/service}Category').text)
                #print('Availability: \t',part.find('{http://api.mouser.com/service}Availability').text)
                #print('LeadTime: \t',part.find('{http://api.mouser.com/service}LeadTime').text)
                #print('OnOrder: \t',part.find('{http://api.mouser.com/service}FactoryStock').text)
                #print('Price @',part.find('{http://api.mouser.com/service}PriceBreaks/{http://api.mouser.com/service}Pricebreaks/{http://api.mouser.com/service}Quantity').text,': \t',part.find('{http://api.mouser.com/service}PriceBreaks/{http://api.mouser.com/service}Pricebreaks/{http://api.mouser.com/service}Price').text)
                #print('Description: \t',part.find('{http://api.mouser.com/service}Description').text)

                #partdict = {'Availability':part.find('{http://api.mouser.com/service}Availability').text,'Quantity':part.find('{http://api.mouser.com/service}PriceBreaks/{http://api.mouser.com/service}Pricebreaks/{http://api.mouser.com/service}Quantity').text,'Price':part.find('{http://api.mouser.com/service}PriceBreaks/{http://api.mouser.com/service}Pricebreaks/{http://api.mouser.com/service}Price').text}
                
                #partdict = [part.find('{http://api.mouser.com/service}Availability').text,part.find('{http://api.mouser.com/service}PriceBreaks/{http://api.mouser.com/service}Pricebreaks/{http://api.mouser.com/service}Quantity').text,part.find('{http://api.mouser.com/service}PriceBreaks/{http://api.mouser.com/service}Pricebreaks/{http://api.mouser.com/service}Price').text]
                #mouserparts.append(dict(zip(keys,partdict)))
                mouserparts.append({'Part':part.find('{http://api.mouser.com/service}MouserPartNumber').text,
                    'Category':part.find('{http://api.mouser.com/service}Category').text,
                    'Description':part.find('{http://api.mouser.com/service}Description').text,
                    'Availability':part.find('{http://api.mouser.com/service}Availability').text,
                    'FactoryStock':part.find('{http://api.mouser.com/service}FactoryStock').text,
                    'LeadTime':part.find('{http://api.mouser.com/service}LeadTime').text,
                    'Quantity':part.find('{http://api.mouser.com/service}PriceBreaks/{http://api.mouser.com/service}Pricebreaks/{http://api.mouser.com/service}Quantity').text,
                    'Price':part.find('{http://api.mouser.com/service}PriceBreaks/{http://api.mouser.com/service}Pricebreaks/{http://api.mouser.com/service}Price').text})
                i += 1
            else:
                #print('\n')
                #print('Mouser part #:\t',part.find('{http://api.mouser.com/service}MouserPartNumber').text)
                #print('Found N/A part')
                
                mouserparts.append({'Part':'N/A','Category':'N/A','Description':'N/A','Availability':'N/A','FactoryStock':'N/A','LeadTime':'N/A','Quantity':'N/A','Price':'N/A'})

        #print('--------------------------')
        #print(mouserparts[1:len(mouserparts)]['Part'])
        #print(mouserparts[1]['Price'])
        bob = []
        #for p in mouserparts:
            #print(p['Part']+' '+p['Price'])
            #print(p)
        newlist = sorted(mouserparts,key=itemgetter('Price'))
            #bob.append(newlist)
        #print(mouserparts)
        #print(newlist)
        return newlist
        
    else:
        raise Exception('Mouser API returned: {}'.format(r.status_code)+' - {}'.format(r.reason))
    return