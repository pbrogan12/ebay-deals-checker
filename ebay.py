import urllib, json, smtplib
import cPickle as pickle
from email.mime.text import MIMEText
def dealsChecker(searchTerm, emailAddress, emailPass):

    try:
        itemIds = pickle.load(open('itemIds.pkl','rb'))
    except:
        itemIds = []

    msg = ""
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
                itemInfo = i['title'], i['convertedcurrentprice'], i['dealurl']
                msg =  msg + i['title'] + ' ' + i['convertedcurrentprice'] + ' ' + i['dealurl'] + "\n"
    pickle.dump(itemIds, open('itemIds.pkl', 'wb'))

    if msg:
        msg = MIMEText(msg)
        msg['Subject'] = 'Ebay daily deals for %s' % searchTerm
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(emailAddress,emailPass)
        s.sendmail(emailAddress, emailAddress, msg.as_string())
        s.quit()

