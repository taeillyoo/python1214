# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
import re 

#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

# <a href="/board/view.php?table=humordata&amp;no=1932391&amp;s_no=15238483&amp;kind=total&amp;page=1" target="_top">7년만의 재회</a>

#for n in range(0,10):
for n in range(1,11):
        #클리앙의 중고장터 주소 
        # data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        data = "http://www.todayhumor.co.kr/board/list.php?kind=total&table=total&page=" + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        data = urllib.request.urlopen(req).read()
        # 혹시 한글이 깨지는 경우?
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        # list = soup.findAll('a', attrs={'class':'list_subject'})
        # list = soup.find_all('span', attrs={'data-role':'list-title-text'})
        list = soup.find_all('td', attrs={'class':'subject'})

        for item in list:
                try:
                        #<a class='list_subject'><span>text</span><span>text</span>
                        # span = item.contents[1]
                        # span2 = span.nextSibling.nextSibling
                        # title = span2.text 
                        # title = item.text.strip()
                        item2 = item.find("a").text.strip()
                        # print(item2)
                        if (re.search('도박', item2)):
                                print(item2.strip())
                                # print('https://www.clien.net'  + item['href'])
                except:
                        pass
        
