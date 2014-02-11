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
    itemHtml = """"""
    for i in itemData['ebaydailydeals']['items']:
        if searchTerm.lower() in i['title'].lower():
            if str(i['itemid']) in itemIds:
                pass
            else:
                itemIds.append(str(i['itemid']))
                itemInfo = i['title'], i['convertedcurrentprice'], i['dealurl']
                msg =  msg + i['title'] + ' ' + i['convertedcurrentprice'] + ' ' + i['dealurl'] + "\n"
                itemHtml = itemHtml + '<tr><td>' + i['title'] + '</td><td>' + i['dealurl'] + '</td></tr>'
    pickle.dump(itemIds, open('itemIds.pkl', 'wb'))

    if msg:
        count = 0
        html = """"""
        email = open('email.html','r')
        for i in email:
            if count == 187:
                html = html + itemHtml
                count += 1
            else:
                count += 1
                html = html + i
        email.close()
        part2 = MIMEText(html, 'html')
        msg.attach(part2)
        msg['Subject'] = 'Ebay daily deals for %s' % searchTerm
        s = smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        s.login(emailAddress,emailPass)
        s.sendmail(emailAddress, emailAddress, msg.as_string())
        s.quit()

