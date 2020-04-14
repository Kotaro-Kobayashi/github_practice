def add_san(names):
    for n in range(len(names)):
        names[n] = names[n] + 'さん'

    return names


before = ['マツダ', 'コバヤシ', '佐々木']
copy = list()
for n in before:
    copy.append(n)

after = add_san(copy)
print('after:' + after[0])
print('before' + before[0])
