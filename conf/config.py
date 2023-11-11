# coding:utf-8
import time
n: int = 0

user: dict = {
    'Mr.Yao': 1022,
    'Akarry': 1445
}


def login(name, passwd):
    for i in user:
        if name == i:
            if passwd == user.get(i):
                with open(file='log/log.log', mode='wt', encoding='utf-8')as f:
                    f.write(f'[{n}]')


funcs: dict = {
    0: exit,
    1: login
}
