import requests
from bs4 import BeautifulSoup
headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
           'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
#url = 'https://www.xvideos.com/?k=milf&p=2'

def hh_parse(headers):
        page=1
        url = 'https://www.xvideos.com/?k=milf&p=' + str(page)
        session = requests.Session()
        request = session.get(url, headers=headers)
        #############
        if request.status_code==200:
            #print('1')
            soup = BeautifulSoup(request.content, 'html.parser')
            div1 = soup.find('div', attrs={'id' : 'main'}).find('div', attrs={'id' : 'content'}).find('div', attrs={'class' : 'mozaique'})
            #print(div1)
            #print(video)
            for video in div1.find_all('div'):
                #clas_div = video.find('div')
                clas_p = video.find('p', attrs={'class' : 'title'})
                if(clas_p != None):
                    title = clas_p.find('a')
                    href = clas_p.find('a')['href']
                    url_2 = 'https://www.xvideos.com' + href
                    print(url_2)
                    #print(title.text)
                    #print(href)
                #print(clas_p)
        else:
            print('0')
hh_parse(headers)
