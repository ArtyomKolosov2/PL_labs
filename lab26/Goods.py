# Класс Good, класс-сущность, описывающий существенные характеристики
# товара
#
# Version: 1.0
# Group: 10701219
# Author: Колосов Артём Александрович
# Date: 16.4.2020

class Good:
    price = 0

    def __init__(self, name, recomended_price):
        self.name = name
        self.recomended_price = recomended_price
        self.price = recomended_price

    def get_info(self):
        return "{0} - {1}$\n".format(self.name, self.price)

    def get_recomended_price(self):
        return self.recomended_price
