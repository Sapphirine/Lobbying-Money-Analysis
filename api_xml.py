import urllib.request

maplight_api = '19525092ab4c20bbe5549e095d4ad379'
headers = {'User-Agent':'tyty/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

ss = ['109','110','111','112','113','114','115']
for i in ss:
    url = 'http://classic.maplight.org/services_open_api/map.bill_list_v1.xml?apikey=19525092ab4c20bbe5549e095d4ad379&jurisdiction=us&session='+i+'&include_organizations=1&has_organizations=1'
    req = urllib.request.Request(url, headers = headers)
    data = urllib.request.urlopen(req)

    xml = data.read()

    f =  open('map.bill_list_v1_'+i+'.xml', "wb")
    f.write(xml)
    f.close()