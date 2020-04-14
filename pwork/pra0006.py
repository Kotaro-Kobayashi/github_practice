class hero:
    name = 'JUN'
    hp = 100

    def sleep(self, hours):
        print('{}は{}時間ネタ' .format(self.name, hours))
        self.hp += hours


# ゲーム開始
print('ゴミゲーの始まりだ')
h = hero()
h.sleep(3)
print('{}のhpは{}' .format(h.name, h.hp))
