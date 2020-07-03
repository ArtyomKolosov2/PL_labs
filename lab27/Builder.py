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
    amount = 0
    TYPES = ("Computer", "NoteBook", "Laptop",
             "Phone", "Mouse", "Camera",
             "MicroPhone", "HeadPhones", "Charge")

    UNDERTYPES = ("Reborn", "Edge", "Plus",
                  "Extra", "Razr", "Sharp",
                  "Light", "Image", "GTX",
                  "Ti", "Gold", "Silver",
                  "Premium")
    PRICE_LIST = (100, 500, 50,
                  10000, 1000, 75,
                  25, 999, 99, 10, 39)
    MODEL_START = 1
    MODEL_END = 5

    def __init__(self):
        Builder.amount += 1

    def __del__(self):
        print("Factory Closed!")

    def create_goods(self, amount):

        goods_list = []
        for i in range(amount):
            name = random.choice(self.TYPES) + " " + random.choice(self.UNDERTYPES) + " " + \
                   str(random.randrange(self.MODEL_START, self.MODEL_END))
            price = random.choice(self.PRICE_LIST)
            goods_list.append(Good(name, price, i))

        return goods_list

    def get_string_repr(self, goods_list):
        string = "List Of Goods:\nNothing!"
        if isinstance(goods_list, list) and goods_list:
            string = "List Of Goods:\n"
            for good in goods_list:
                if isinstance(good, Good):
                    string += good.get_info()
        return string

    def get_types(self):
        info = ""
        for typ in self.TYPES:
            info += typ + "\n"
        return info

    def get_undertypes(self):
        info = ""
        for undertype in self.UNDERTYPES:
            info += undertype + "\n"
        return info
