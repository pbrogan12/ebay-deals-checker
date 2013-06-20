import urllib, json

def dealsChecker(searchTerm, emailAddress):
    itemData = urllib.urlopen('http://deals.ebay.com/feeds/json').read()
    itemData = itemData.replace('ebaydailydeals', '"ebaydailydeals"')
    itemData = itemData.replace('(', '')
    itemData = itemData.replace(')', '')
    itemData = itemData.replace(';', '')
    itemData = json.loads(itemData)
    for i in itemData['ebaydailydeals']['items']:
        if searchTerm.lower() in i['title'].lower():
            print i['title'], i['convertedcurrentprice']

