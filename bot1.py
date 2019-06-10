from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime
import random
import time
import requests
from bs4 import BeautifulSoup
ya=289841871
#alar - 179666336;
#galva - 50230213;
#Oxxi - 61705242; Magos data operus
login, password = "79064374132", "pak228322A"
vk_session = vk_api.VkApi(token ="4eeb6adf5a015676d3ec1da94de6559dbb7ad8782e6f80c9ef7a97c9a196204f828a870c089c83c63f4fe")
#vk_session.auth()

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
##################################################
headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
           'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
#url = 'https://www.xvideos.com/?k=milf&p=2'

def hh_parse(headers):
        kol_vo_porno=0
        copy_url_2=''
        url_2=''
        page=random.randint(0, 10)
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
                clas_div = video.find('div')
                clas_p = video.find('p', attrs={'class' : 'title'})
                if(clas_p != None and clas_div!= None):
                    title = clas_p.find('a')
                    #print(title)
                    href = clas_p.find('a')['href']
                    img = clas_div.find('img')['data-src']
                    copy_url_2=url_2
                    url_2 = 'https://www.xvideos.com' + href
                    if(copy_url_2!=url_2):
                        porn_title=title.text
                        porn_url = url_2
                        porn_img = img
                        vk_session.method('messages.send', {'user_id': event.user_id, 'message': '{0}\n{1}'.format(porn_title,porn_url), 'random_id': random.randint(-2147483648,+2147483648), "attachment": porn_img})
                        time.sleep(3)
                        kol_vo_porno+=1
                        if(kol_vo_porno==4):break
                        #print(title.text)
                        #print(href)
                    #print(clas_p)
        else:
            print('0')
######################################################
#galva
molitva1 =  {'Возлюби Императора,\n'
            'Ибо Он есть избавление Человечества.\n'
            'Повинуйся словам Его,\n'
            'Ибо ведет Он тебя к светлому будущему.\n'
            'Внемли мудрости Его,\n'
            'Ибо хранит Он тебя от зла.\n'
            'Пусть шепот твоих молитв напоен будет любовью,\n'
            'Ибо спасут они твою душу.\n'
            'Почитай слуг Его,\n'
            'Ибо от Его имени говорят они.\n'
            'Дрожи пред его величием,\n'
            'Ибо все мы ходим в тени Его.'}
#oxxi
priv_oxxi=0
Imperator=0
Petrov=0
Magos_Data_Operus=0
flag_status_Megasa=0
status_Megasa='За Хана и Императора!'
def get(vk_session, id_group,vk):
    try:
        attachment = ''
        # print('До всего '+str(time.ctime(time.time())))
        max_num = vk.photos.get(owner_id=id_group, album_id='wall', count=0)['count']
        # print('Смотрим время после получения количества всех картинок ' + str(time.ctime(time.time())))
        num = random.randint(1, max_num)
        # print('Время до получения пикчи ' + str(time.ctime(time.time())))
        pictures = vk.photos.get(owner_id=str(id_group), album_id='wall', count=5, offset=num)['items']
        buf = []
        for element in pictures:
            buf.append('photo' + str(id_group) + '_' + str(element['id']))
        print(buf)
        attachment = ','.join(buf)
        print(type(attachment))
        # print('Время после получения пикчи '+str(time.ctime(time.time())))
        print(attachment)
        return attachment
    except:
        return get(vk_session, id_group, vk)


while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
            print(event.user_id)
            response = event.text.lower()
            print(response)
            if (event.from_user and event.user_id==ya):
                if response == "морати":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Морати лох', 'random_id':random.randint(-2147483648,+2147483648)})
                if response == "баина":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Баина+Дорж',
                                       'random_id': random.randint(-2147483648, +2147483648)})
                if response == "алар":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Кусака Кусь Кусь',
                                       'random_id': random.randint(-2147483648, +2147483648)})
                if response == "даров":
                    vk_session.method('messages.send',
                                      {'user_id': event.user_id, 'message': 'Вечер в хату',
                                       'random_id': random.randint(-2147483648, +2147483648)})
                if response == "привет":
                        vk_session.method('messages.send',
                                          {'user_id': event.user_id, 'message': 'Приветствую',
                                           'random_id': random.randint(-2147483648, +2147483648)})
                if response == "rasputin":
                        vk_session.method('messages.send',
                                          {'user_id': event.user_id, 'message': 'https://www.youtube.com/watch?v=xHLes2dUuEQ',
                                           'random_id': random.randint(-2147483648, +2147483648)})
                if response == "молитва":
                        vk_session.method('messages.send',
                                          {'user_id': event.user_id, 'message': molitva1,
                                           'random_id': random.randint(-2147483648, +2147483648)})
                if flag_status_Megasa==1:
                        status_Megasa=response
                        flag_status_Megasa=0
                if response == "статус":
                        flag_status_Megasa=1
                if response == "омега":
                        #hh_parse(headers)
                        vk_session.method('messages.send',
                                          {'user_id': event.user_id, 'message': 'Цитирую моего создателя: {0}'.format(status_Megasa),
                                           'random_id': random.randint(-2147483648, +2147483648)})
                if response == "порно":
                        hh_parse(headers)
            if (event.from_user and event.user_id==179666336):
                if response == "порно":
                    hh_parse(headers)
                    time.sleep(3)
                    vk_session.method('messages.send',
                                          {'user_id': event.user_id, 'message': 'Удачно подрочить!',
                                           'random_id': random.randint(-2147483648, +2147483648)})
                time.sleep(3)
                if(response == "как мегас" or response == "как дела мегаса" or response == "как дела у мегаса" or response == "как создатель"):
                    vk_session.method('messages.send',
                                          {'user_id': event.user_id, 'message': 'Цитирую моего создателя: {0}'.format(status_Megasa),
                                           'random_id': random.randint(-2147483648, +2147483648)})
                time.sleep(3)
            if (event.from_user and event.user_id==50230213):
                if (response == "хеллоу" or response == "привет" or response == "даров" or response == "приветствую"):
                    vk_session.method('messages.send',
                                          {'user_id': event.user_id, 'message': 'Я - верноподданый Бога Императора и слуга Лорда Инквизитора, приветствую тебя',
                                           'random_id': random.randint(-2147483648, +2147483648)})
                    time.sleep(3)
                    vk_session.method('messages.send',
                                          {'user_id': event.user_id, 'message': 'Если нам суждено умереть, мы умрем с огнем в глазах и с молитвой Императору на устах!',
                                           'random_id': random.randint(-2147483648, +2147483648)})
                    time.sleep(3)
                    vk_session.method('messages.send',
                                          {'user_id': event.user_id, 'message': 'Если захочешь узнать как правильно молиться Богу Императору, напиши мне - молитва',
                                           'random_id': random.randint(-2147483648, +2147483648)})
                    time.sleep(3)
                    vk_session.method('messages.send',
                                          {'user_id': event.user_id, 'message': 'Император Защищает',
                                           'random_id': random.randint(-2147483648, +2147483648)})
                if response == "молитва":
                    vk_session.method('messages.send',
                                          {'user_id': event.user_id, 'message': molitva1,
                                           'random_id': random.randint(-2147483648, +2147483648)})
                if(response == "как мегас" or response == "как дела мегаса" or response == "как дела у мегаса" or response == "как создатель"):
                    vk_session.method('messages.send',
                                          {'user_id': event.user_id, 'message': 'Цитирую моего создателя: {0}'.format(status_Megasa),
                                           'random_id': random.randint(-2147483648, +2147483648)})
                time.sleep(3)
            if (event.from_user and event.user_id==61705242):
                if(priv_oxxi==0):
                    vk_session.method('messages.send',
                                    {'user_id': event.user_id, 'message': 'Мое почтение, Магос.Чем я могу быть полезен? \nИмператор защищает', 'random_id':random.randint(-2147483648,+2147483648)})
                    priv_oxxi=1;
                    time.sleep(3)
                vk_session.method('messages.send',
                                    {'user_id': event.user_id, 'message': 'Я могу работать как поисковая система \nМой создатель оставил пару пасхалок, найдите их все! \nУверен он будет очень рад', 'random_id':random.randint(-2147483648,+2147483648)})
                if response == "император защищает":
                    vk_session.method('messages.send',
                                          {'user_id': event.user_id, 'message': molitva1,
                                           'random_id': random.randint(-2147483648, +2147483648)})
                    Imperator=1
                if response == "петров":
                    vk_session.method('messages.send',
                                          {'user_id': event.user_id, 'message': "Мерген, Его зовут Мерген!",
                                           'random_id': random.randint(-2147483648, +2147483648)})
                    time.sleep(3)
                    vk_session.method('messages.send',
                                          {'user_id': event.user_id, 'message': "Ну или хотя бы Мегас",
                                           'random_id': random.randint(-2147483648, +2147483648)})
                    Petrov=1
                if response == "мой ранг":
                    vk_session.method('messages.send',
                                          {'user_id': event.user_id, 'message': "Magos Data Operus",
                                           'random_id': random.randint(-2147483648, +2147483648)})
                    Magos_Data_Operus=1
                if (Imperator==1 and Petrov==1 and Magos_Data_Operus==1):
                    vk_session.method('messages.send',
                                          {'user_id': event.user_id, 'message': "Поздравляю!\nВсе пасхалки найдены",
                                           'random_id': random.randint(-2147483648, +2147483648)})
            if (event.from_user):
                if response == "мегас":
                        vk_session.method('messages.send',
                                          {'user_id': event.user_id, 'message': 'Цитирую моего создателя: {0}'.format(status_Megasa),
                                           'random_id': random.randint(-2147483648, +2147483648)})
                        time.sleep(3)
                        vk_session.method('messages.send',
                                          {'user_id': event.user_id, 'message': 'https://vk.com/music?z=audio_playlist289841871_1',
                                           'random_id': random.randint(-2147483648, +2147483648)})
                        time.sleep(3)