import urllib.request

def download_page(pageUrl):
    try:
        page = urllib.request.urlopen('http://www.urogay-smol.ru/')
        text = page.read().decode('utf-8')
        print(pageUrl, 'ok')
    except:
        print('Error at', pageUrl)
        return
    # do something with the downloaded text

commonUrl = 'http://www.urogay-smol.ru/?module=articles&action=view&id='
for i in range(135, 736):
    pageUrl = commonUrl + str(i)
    download_page(pageUrl)
 
