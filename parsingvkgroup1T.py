import csv
import requests
import time

def take_members():
    token = "4c2383fb4c2383fb4c2383fbc54f36939444c234c2383fb289d065c5757428dad3c19af"
    version = 5.131
    group_id = "1tsprint"
    response = requests.get('https://api.vk.com/method/groups.getMembers',
                            params={
                                'access_token': token,
                                'v': version,
                                'group_id': group_id,
                            })
    all_members = response.json()['response']['count']
    return all_members

def take_1000_posts():
    token = "4c2383fb4c2383fb4c2383fbc54f36939444c234c2383fb289d065c5757428dad3c19af"
    version = 5.131
    domain = "1tsprint"
    offset = 0
    count = 100
    date = []
    while offset < 1000:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain,
                                    'offset': offset,
                                    'count': count
                                })
        all_posts = response.json()['response']['items'] ## Если тут выскакивает ошибка, мол не видит 'response' запустите снова.
        date.extend(all_posts)
        offset += 100
        time.sleep(0.09)
    return date

def file_writer(date, all_members):
    with open('1Ttest.csv', 'w') as file:
        write = csv.writer(file)
        write.writerow(('count_post', 'count_members', 'reposts'))
        pocket = []
        for post, i in enumerate(date):
            pocket.append(date[post]['reposts']['count'])
        write.writerow([all_post.__len__(), all_members, sum(pocket)])
        print("Congratulations, view your csv file to views your results")
all_post = take_1000_posts()
all_member = take_members()
file_writer(all_post, all_member)