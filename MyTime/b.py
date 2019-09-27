class Food(object):
    __food_name = 'Quanjude Roast Duck'

    def set_food_name(self, food_name):
        self.__food_name = food_name

    def get_food_name(self):
        return self.__food_name


class Scenery(object):
    __scenery_name = 'Great Wall'

    def set_scenery_name(self, scenery_name):
        self.__scenery_name = scenery_name

    def get_scenery_name(self):
        return self.__scenery_name


class City(Scenery, Food):
    __city_name = 'Beijing'

    def love(self):
        print('{} is a big city!'.format(self.get_city_name()))

    def set_city_name(self, city_name):
        self.__city_name = city_name

    def get_city_name(self):
        return self.__city_name

    def have(self):
        print('{} have {}'.format(self.get_city_name(),
                                  self.get_scenery_name()))


class Person(City):
    def __init__(self, person_name, sex):
        self.person_name = person_name
        self.sex = sex

    def __str__(self):
        return 'This is a person class, name = {}, sex = {}'\
            .format(self.person_name,
                    self.get_person_sex())

    def get_person_sex(self):
        if self.sex == 1:
            return 'Boy'
        if self.sex == 0:
            return 'Girl'

    def live(self):
        print('{} live in {}, there have {}, and he/her like eat {}.'
              .format(self.person_name,
                      self.get_city_name(),
                      self.get_scenery_name(),
                      self.get_food_name()))

    def info(self):
        print('{} is a {}'.format(self.person_name, self.get_person_sex()))


if __name__ == '__main__':
    p = Person('Li Lei', 1)
    p.live()
    p.info()
    print(Person('Li Lei', 1))
