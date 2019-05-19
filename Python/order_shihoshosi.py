#coding UTF-8
from urllib import request
import urllib.parse
import bs4
from time import sleep
a = ['田中　太郎','松本　大介']

for i in a:
    name= urllib.parse.urlencode({'search_name':str(i)})
    sarch_word = urllib.parse.quote(i+"　司法書士")
    print(sarch_word)
#    print(i)
    url= 'http://kensaku.shiho-shoshi.or.jp/search/member.php?search_code=&'+name+'&search_address=&x=161&y=14'
    html = request.urlopen(url).read()
    soup = bs4.BeautifulSoup(html, 'lxml')
    office = soup.select('td:nth-child(6)')
    address = soup.select('td:nth-child(5)')
    #print(len(office))
    sarch_url = 'https://www.google.com/search?q=' + sarch_word
    headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/3,0.7",}
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)

    html_2 = request.urlopen(sarch_url).read()
    soup_2 = bs4.BeautifulSoup(html_2, 'lxml')
    title = soup_2.find_all('h3',class_="LC20lb")
    print(title)
    if len(office)>1:
        office_true = str(office[1])
        office_true = office_true.replace('<td>','')
        office_true = office_true.replace('<br/>','')
        office_true = office_true.lstrip()
        office_true = office_true.replace('</td>','')
        office_true = office_true.rstrip()
        pref = str(address[1])
        index_1 = pref.find('<br/>')
        index_2 = pref.find('<br/>',index_1+1)
        pref = pref[index_1+5:index_2]
        pref = pref.lstrip()
        print(i+":"+office_true+"("+pref[:3]+")")
    else:
        print(i)
#<table id = kojin>
#td[5]
#    sleep(1)
#１ページ毎に１秒休む