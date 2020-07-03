# Класс Good, класс-сущность, описывающий существенные характеристики
# товара
#
# Version: 1.0
# Group: 10701219
# Author: Колосов Артём Александрович
# Date: 16.4.2020


class Good:
    amount = 0

    def __init__(self, name, recomended_price, identity):
        self.name = name
        self.recomended_price = recomended_price
        self.price = recomended_price
        self.identity = identity
        Good.amount += 1

    def __del__(self):
        Good.amount -= 1
        print(self.name, " Deleted")

    def get_info(self):
        return "{0} (price: {1}$, id = {2})\n".format(self.name,
                                                      self.price,
                                                      self.identity)

    def get_recomended_price(self):
        return self.recomended_price
