from zeep import Client,xsd
from zeep import wsdl as test
from lxml import etree as ET

url = 'https://www.mouser.dk/service/searchapi.asmx'
wsdl = 'https://www.mouser.dk/service/searchapi.asmx?wsdl'
client = Client(wsdl=wsdl)


service = client.create_service('{http://api.mouser.com/service}SearchAPISoap12','http://api.mouser.com/service')

client.transport.session.headers.update({'PartnerID':'9c3c2752-29bb-4b9a-9679-e5fb6ade3a8c'})

#print(client.transport.session.headers.get('PartnerID'))
#client.transport.session.headers.update({'SOAPAction':'http://api.mouser.com/service/SearchByKeyword'})
#print(client.transport.session.headers.keys)





""" header = xsd.ComplexType([
        '{http://api.mouser.com/service}AccountInfo',
        xsd.ComplexType([
            xsd.Element(
                'PartnerID'
                ,xsd.String()),
        ]),
]) """

header = xsd.ComplexType(['{http://api.mouser.com/service}AccountInfo',xsd.Element('{http://api.mouser.com/service}PartnerID',xsd.String())])


#print(header)

header_value = header(PartnerID='9c3c2752-29bb-4b9a-9679-e5fb6ade3a8c')
print(header_value)

#node = client.create_message(client.service, 'SearchByKeyword', keyword='max4239',records=10,startingRecord=0,searchOptions='BeginsWith',_soapheaders=[header_value])




client.set_default_soapheaders([header_value])

print('Service Accessible: \t',client.service.ServiceStatus())



#_soapheaders=[header_value])
client.set_ns_prefix('ns0','http://api.mouser.com/service')
print(client.get_type('{http://api.mouser.com/service}AccountInfo'))
client.service.SearchByKeyword(keyword='max4239',records=10,startingRecord=0,searchOptions='BeginsWith',_soapheaders=[header_value])
#,_soapheaders=[header_value])


#print(client.service.SearchAPI.SearchByKeyword('max4239'))



#header = xsd.Element('{http://api.mouser.com/service}Pa')