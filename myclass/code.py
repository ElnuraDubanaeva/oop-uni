from best_lib.balance import Balance
from best_lib.report import make_report
import requests
balance = Balance()

link1 = make_report('https://jsonplaceholder.typicode.com/posts/1/')
link2 = make_report('https://habr.com/ru/company/vk/blog/692062/')

