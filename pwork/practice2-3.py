person1 = {'サッカー', 'ゲーム', 'ゴルフ', '漫画', '読書'}
person2 = {'ピアノ', 'ゲーム', 'テニス', '読書', 'アニメ'}

input('心の準備が出来たらenterキーを押してください')

common = person1 & person2
total = person1 | person2

rate = len(common) / len(total) * 100

print(f'相性は{rate}%です')
