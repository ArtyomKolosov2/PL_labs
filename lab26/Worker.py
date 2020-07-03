# Класс Worker, функциональный класс, в котором описывается
# основная бизнес логика приложения
#
# Version: 1.0
# Group: 10701219
# Author: Колосов Артём Александрович
# Date: 16.4.2020

from Goods import Good
import random


class Worker:
    add_to_salary = 0.1

    def __init__(self, name, salary, greedy_level=1, status="Consultant"):
        self.name = name
        self.status = status
        self.salary = salary
        self.greedy_level = greedy_level

    def upscale_prices(self, goods_list):
        print(self.status, self.name, ": Black Friday! Prices are increased for {0} %".format(round((self.greedy_level - 1) * 100)))
        for good in goods_list:
            if isinstance(good, Good):
                good.price = round(good.price * self.greedy_level, 2)

    def sale_prices(self, goods_list, sale_coef=0.5):
        if 0 < sale_coef < 1:
            print(self.status, self.name, ": Sales!!! Decreasing prices for {0}%".format(round((1-sale_coef) * 100)))
            for good in goods_list:
                if isinstance(good, Good):
                    good.price = round(good.price * sale_coef, 2)
        else:
            print("What?")

    def sell_one_good(self, goods_list):
        delete_index = random.randint(0, len(goods_list)-1)
        if isinstance(goods_list[delete_index], Good):
            good = goods_list.pop(delete_index)
            print(self.get_info(), " sold ", good.get_info())
            self.salary += (self.add_to_salary * good.price)

    def get_info(self):
        return "{0} {1}: Greedy level = {2}: Salary {3}".format(self.status,
                                                                    self.name,
                                                                    self.greedy_level,
                                                                    self.salary)
