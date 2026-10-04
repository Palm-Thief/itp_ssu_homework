alph = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

def cezar(letter, shift):
    ind = alph.index(letter) + ((-1)**shift) * shift
    return alph[ind if ind < 32 else ind % 32]

text = 'Батюшка сказал мне: Прощай, Петр. Служи верно, кому присягнешь; слушайся начальников; за их лаской не гоняйся; на службу не напрашивайся; от службы не отговаривайся; и помни пословицу: береги платье снову, а честь смолоду. Матушка в слезах наказывала мне беречь мое здоровье, а Савельичу смотреть за дитятей. Надели на меня заячий тулуп, а сверху лисью шубу. Я сел в кибитку...'
new_text = []
for w in text.split():
    leng = len([c for c in w if c.lower() in alph])
    new_w = []
    for c in w:
        new_c = ''
        if c in ',.;:':
            new_c = c
        elif c.isupper():
            new_c = cezar(c.lower(), leng).upper()
        else:
            new_c = cezar(c, leng)
        new_w.append(new_c)
    new_text.append(''.join(new_w))

print(' '.join(new_text))