score1 = [80, 40, 60]
score2 = [80, 40, 60]

print('score1のidentity: {}' .format(id(score1)))
print('score2のidentity: {}' .format(id(score2)))

if score1 == score2:
    print('same value')
else:
    print('not same value')

if id(score1) == id(score2):
    print('same id')
else:
    print('not same id')
