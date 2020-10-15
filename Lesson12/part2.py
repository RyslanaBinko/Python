from random import randint


class City:

    def __init__(self, name):
        self.__name = name
        self.__streets = []

    def create_a_streets(self, name):
        self.__streets.append(Street(name))

    def full_city(self):
        for i in range(0, len(self.__streets)):
            for j in range(0, len(self.__streets[i].get_houses())):
                self.__streets[i].get_houses()[j].set_tenants()

    def get_streets(self):
        return self.__streets

    def tenants_count(self):
        count = 0
        for i in self.__streets:
            count += i.tenants_count()
        return count


class Street:
    def __init__(self, name):
        self.__name = name
        self.__houses = []
        for i in range(1, randint(5, 20)):
            self.__houses.append(House(i + 1))

    def get_houses(self):
        return self.__houses

    def create_a_house(self):
        self.__houses.append()

    def tenants_count(self):
        count = 0
        for i in self.__houses:
            count += i.get_tenants()
        return count


class House:
    def __init__(self, number):
        self.__number = number
        self.__tenants = randint(1, 100)

    def get_tenants(self):
        return self.__tenants

    def set_tenants(self):
        self.__tenants = randint(1, 100)


City1 = City("gorod")
City1.create_a_streets(1)
print(City1.get_streets()[0].tenants_count())
City1.create_a_streets(2)
print(City1.get_streets()[1].tenants_count())
print(City1.tenants_count())