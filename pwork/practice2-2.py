test = []

test.append(int(input('国語の点数>>')))
test.append(int(input('数学の点数>>')))
test.append(int(input('英語の点数>>')))
test.append(int(input('理科の点数>>')))
test.append(int(input('社会の点数>>')))

s = sum(test)
ave = s / len(test)

print(s)
print(ave)
