import xml.etree.ElementTree as ET
import requests
import csv

#bill number
n = ['109','110','111']
for i in n:
    tree = ET.parse('map.bill_list_v1_'+i+'.xml')
    #tree = ET.parse('map.bill_list_v1_109.xml')
    root = tree.getroot()

    for child in root:
        try:
            a = (child.find('url').text)
            topic = child.find('topic').text
            topic=topic[:63]
            
            topic = topic.replace('/','-')
            print(topic)
            a = a + '/download.csv'
            b = requests.get(a)
            print('URL Get!')
            if topic[-1] == '.':
                with open(topic+'csv','w') as f:
                    writer = csv.writer(f)
                    reader = csv.reader(b.text.splitlines())

                    for row in reader:
                        writer.writerow(row)
            else:    
                with open(topic+'.csv','w') as f:
                    writer = csv.writer(f)
                    reader = csv.reader(b.text.splitlines())

                    for row in reader:
                        writer.writerow(row)
        
        except:
            pass