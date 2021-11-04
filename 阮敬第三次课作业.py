import random

a = ['T劣', 'T良', 'T优']
b = ['M劣', 'M良', 'M优']
c = [0, 1, 2]
d = {}
while 1:
    g = 0
    h = 0
    e = random.sample(c, 3)
    f = random.sample(c, 3)
    for i in range(3):
        if a[e[i]] == 'T优':
            if b[f[i]] == 'M良':
                print('第二个条件满足')
            else:
                print('第二个条件不满足')
                h = h + 3
        if a[e[i]] == 'T劣':
            if b[f[i]] == 'M劣':
                print('第一个条件不满足')
                g = g + 2
            else:
                print('第一个条件满足')
    if g != 0 or h != 0:
        print('不满足条件，重新开始抽签')
        continue
    for i in range(3):
        d[a[e[i]]] = b[f[i]]
    print('满足抽签条件，最终的抽签结果为：')
    print(d)

    if g == 0 and h == 0:
        break
