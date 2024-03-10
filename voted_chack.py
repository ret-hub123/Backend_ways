
voted = {}

def chack_voted(name):
    if voted.get(name):
        return ('Выйди отсюда!')
    else:
        voted[name] = True
        return ('Спасибо за ваш голос!')


print(chack_voted("Tom"))
print(chack_voted("Mike"))
print(chack_voted("Mike"))

sss = {}
sss['priv'] = 123
