import urllib, json

def dealsChecker(searchTerm, emailAddress):
    textfile = open('itemid.txt', 'a + r')
    itemData = urllib.urlopen('http://deals.ebay.com/feeds/json').read()
    itemData = itemData.replace('ebaydailydeals', '"ebaydailydeals"')
    itemData = itemData.replace('(', '')
    itemData = itemData.replace(')', '')
    itemData = itemData.replace(';', '')
    itemData = json.loads(itemData)
    for i in itemData['ebaydailydeals']['items']:
        if searchTerm.lower() in i['title'].lower():
            if str(i['itemid']) in textfile.read():
                    print "BOOYAH"
                    break
            else:
                textfile.write(i['itemid'] + "\n")
                print i['itemid']
                print i['title'], i['convertedcurrentprice'], i['itemid']
    textfile.close()
