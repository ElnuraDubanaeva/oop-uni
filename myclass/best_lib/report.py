import time
import requests


def make_report(link):
    with open('reports.txt', mode='a') as reports:
        response = requests.get(link)
        reports.write(time.strftime('%x ,%X '))
        reports.write(link)
        reports.write('  ')
        reports.write(str(response.status_code))
        reports.write('\n')
        reports.close()
link1 = make_report('https://jsonplaceholder.typicode.com/posts/1/')
link2 = make_report('https://habr.com/ru/company/vk/blog/692062/')
if link1 == link2:
    print('Свойства равны')
else:
    print("Свойства не равны")
response1 = requests.get('https://jsonplaceholder.typicode.com/posts/1/')
response2 = requests.get('https://habr.com/ru/company/vk/blog/692062/')
text1 = response1.text
text2 = response2.text
if text1 == text2:
    print('код равен')
else:
    print("код не равен")