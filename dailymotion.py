import requests


page = 0
with open(file='dailymotion.txt', mode='w', encoding='utf-8') as file:
    file.write('Cсылка' + '\t' + 'Название' + '\t' + 'Описание' + '\t' + 'Просмотры' + '\t' + 'Название Канала' + '\t'
               + 'Длительность видео' + '\n')

title_input = input('Введите запрос для поиска - ')
print('Ожидайте')
for _ in range(10):
    page += 1
    url = 'https://api.dailymotion.com/videos?limit=100&fields=id,title,description,views_total,user.username,' \
          'duration,channel.created_time&search=' + str(title_input) + '&page=' + str(page)
    r = requests.get(url)
    _text = r.text.split('"list":[')[1]
    r_text = _text.split('},{')
    try:
        for pages in r_text:
            splited_text = pages.split(',"')
            id_title = splited_text[0].replace('"', '').replace('id:', '').replace('{', '')
            url = 'https://www.dailymotion.com/video/' + str(id_title)
            title = splited_text[1].replace('"', '').replace('title:', '')
            description = splited_text[2].replace('"', '').replace('description:', '')
            views_total = splited_text[3].replace('"', '').replace('views_total:', '')
            user_username = splited_text[4].replace('"', '').replace('user.username:', '')
            duration = splited_text[5].replace('"', '').replace('duration:', '')
            need_duration = round(int(duration) / 60)
            with open(file='dailymotion.txt', mode='a', encoding='utf-8') as file:
                file.write(str(url) + '\t' + str(title) + '\t' + str(description) + '\t' + str(views_total) + '\t'
                           + str(user_username) + '\t' + str(str(need_duration) + ' минут') + '\n')
    except:
        pass
print('Готово! результаты поиска смотри в файле dailymotion.txt')
