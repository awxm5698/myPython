import time


class SceneWalk:
    def __init__(self, way, enemy, base=(500, 500), move=10, sale=7):
        self.way = way
        self.enemy = enemy
        self.sale = sale
        self.base = base
        self.move = move

    def list_to_way(self):
        way_list = []
        for i in self.way:
            way_list.append(i)
        return way_list

    def list_to_enemy(self):
        enemy_list = []
        for i in self.enemy:
            enemy_list.append(i)
        return enemy_list

    def main(self):
        c = {'w': (self.base[0], self.base[1]-self.move),
             'a': (self.base[0]-self.move, self.base[1]),
             's': (self.base[0], self.base[1]+self.move),
             'd': (self.base[0]+self.move, self.base[1])}

        fight_time = 0
        way_list = self.list_to_way()
        enemy_list = self.list_to_enemy()
        for i in range(len(way_list)):
            print('Player move to location {}'.format(c[way_list[i]]))
            time.sleep(0.5)
            if int(enemy_list[i]) == 1:
                print('Player come across enemy')
                time.sleep(2)
                print('==== Player defeat the enemy, click the button sure ====')
                fight_time = fight_time + 1
            if fight_time != 0 and fight_time % 7 == 0:
                fight_time = 0
                print('Player sale of goods')
                time.sleep(1)
                print('Player back scene')


if __name__ == '__main__':

    _way = 'ddddddwwaaaaaawwwddwwwwddddddddsssssss'
    _enemy = '00000001000010001000100010010010001000'
    _sale = 7
    _base = (500, 500)
    _move = 10

    s = SceneWalk(_way, _enemy, _base, _move, _sale)
    s.main()



