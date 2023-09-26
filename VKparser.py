import csv

import requests

def take_posts():
    token = 'f4109385f4109385f41093853ef705509cff410f41093859103900fe8a492d1f969aa6f'
    version = 5.154
    domain = 'rshu_official'
    count = 100
    offset = 0
    all_posts = []


    while offset < 300:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'count': count,
                                    'offset': offset
                                }
                                )
        data = response.json()['response']['items']
        offset += 100
        all_posts.extend(data)
    return all_posts

def file_writer(data):
    with open('rshu.csv', 'w', encoding='utf8') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(('body', 'url'))
        for post in data:
            try:
                if post['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url = 'pass'
            except:
                pass

            a_pen.writerow((post['text'], img_url))

all_posts = take_posts()
file_writer(all_posts)
