import urllib, json
import cPickle as pickle

def dealsChecker(searchTerm, emailAddress):
    try:
        itemIds = pickle.load(open('itemIds.pkl','rb'))
    except:
        itemIds = []
    itemData = urllib.urlopen('http://deals.ebay.com/feeds/json').read()
    itemData = itemData.replace('ebaydailydeals', '"ebaydailydeals"')
    itemData = itemData.replace('(', '')
    itemData = itemData.replace(')', '')
    itemData = itemData.replace(';', '')
    itemData = json.loads(itemData)
    for i in itemData['ebaydailydeals']['items']:
        if searchTerm.lower() in i['title'].lower():
            if str(i['itemid']) in itemIds:
                pass
            else:
                itemIds.append(str(i['itemid']))
                print i['title'], i['convertedcurrentprice'], i['itemid']
    pickle.dump(itemIds, open('itemIds.pkl', 'wb'))
