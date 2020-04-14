isError = False
n = 99

if isError == False and n < 100:
    print("github")

print("---------------------------------------")

num = int(input("整数を入力>>"))
if num % 2 == 0:
    print("偶数ね")
else:
    print("奇数ね")

print("(3)")

hello = input("挨拶しようね>>")
if hello == 'こんにちは':
    print("ようこそ！")
elif hello == '景気は？':
    print("ぼちぼちです")
elif hello == 'さようなら':
    print("お元気で")
else:
    print("どうしました？？")

print("(4)")

month = int(input("今は何月ですか?>>"))
if month in [1, 3, 5, 7, 8, 10, 12]:
    print("31日までありますね")
else:
    if month != 2:
        print("30日までありますね")
    else:
        print("そっか")

print("年が明けてから{}カ月過ぎてますね" .format(month))
