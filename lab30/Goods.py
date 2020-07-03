# Класс Good, класс-сущность, описывающий существенные характеристики
# товара
#
# Version: 1.0
# Group: 10701219
# Author: Колосов Артём Александрович
# Date: 16.4.2020


class Good:
    __amount = 0

    def __init__(self, name="", recomended_price=0, identity=0):
        if not (isinstance(name, str) and isinstance(recomended_price, int) and isinstance(identity, int)):
            raise TypeError("Types of arguments are wrong!")
        self.__name = name
        self.__recomended_price = recomended_price
        self.__price = recomended_price
        self.__identity = identity
        Good.__amount += 1

    def __del__(self):
        Good.__amount -= 1
        print(self.__name, " Deleted")

    def __str__(self):
        return "{0} (price: {1}$, id = {2})\n".format(self.__name,
                                                      self.__price,
                                                      self.__identity)

    def get_info(self):
        return "{0} (price: {1}$, id = {2})\n".format(self.__name,
                                                      self.__price,
                                                      self.__identity)

    def set_price(self, value):
        self.__price = value

    def get_price(self):
        return self.__price

    def set_id(self, value):
        self.__identity = value

    def get_id(self):
        return self.__identity

    def get_recomended_price(self):
        return self.__recomended_price

    @classmethod
    def get_amount(cls):
        return cls.__amount

    Price = property(get_price, set_price)
    Identity = property(get_id, set_id)

