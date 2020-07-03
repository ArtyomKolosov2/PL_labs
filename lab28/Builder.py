# Класс Builder, утилитный класс для
# создания списка товаров, а также
# представления данного списка в
# строковом варианте для вывода на консоль.
#
# Version: 1.0
# Group: 10701219
# Author: Колосов Артём Александрович
# Date: 16.4.2020

import random
from Goods import Good


class Builder:
    __amount = 0
    __TYPES = ("Computer", "NoteBook", "Laptop",
               "Phone", "Mouse", "Camera",
               "MicroPhone", "HeadPhones", "Charge")

    __UNDERTYPES = ("Reborn", "Edge", "Plus",
                    "Extra", "Razr", "Sharp",
                    "Light", "Image", "GTX",
                    "Ti", "Gold", "Silver",
                    "Premium")

    __PRICE_LIST = (100, 500, 50,
                    10000, 1000, 75,
                    25, 999, 99, 10, 39)
    __MODEL_START = 1
    __MODEL_END = 5

    def __init__(self, name=""):
        self.__name = name
        Builder.__amount += 1

    def __del__(self):
        Builder.__amount -= 1
        print("Factory Closed!")

    def __str__(self):
        string = "Factory {0}".format(self.__name)
        return "Factory"

    def create_goods(self, amount):

        goods_list = []
        for i in range(amount):
            name = random.choice(self.__TYPES) + " " + random.choice(self.__UNDERTYPES) + " " + \
                   str(random.randrange(self.__MODEL_START, self.__MODEL_END))
            price = random.choice(self.__PRICE_LIST)
            goods_list.append(Good(name, price, i))

        return goods_list

    def get_types(self):
        info = ""
        for typ in self.__TYPES:
            info += typ + "\n"
        return info

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value

    def get_undertypes(self):
        info = ""
        for undertype in self.__UNDERTYPES:
            info += undertype + "\n"
        return info

    @staticmethod
    def get_amount():
        return Builder.__amount

    @staticmethod
    def get_string_repr(goods_list):
        string = "List Of Goods:\nNothing!"
        if isinstance(goods_list, list) and goods_list:
            string = "List Of Goods:\n"
            for good in goods_list:
                if isinstance(good, Good):
                    string += good.get_info()
        return string

    Name = property(get_name, set_name)
