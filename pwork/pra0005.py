def eat(b, l, d, *oyatu):
    print('朝食>>{}' .format(b))
    print('昼食>>{}' .format(l))
    print('夕飯>>{}' .format(d))
    for o in oyatu:
        print('おやつ>>{}' .format(o))


eat('トースト', 'ラーメン', 'カレー', 'A', 'B', 'C')
