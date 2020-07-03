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
    __salary_add_coef = 0.1
    __amount = 0
    __sold_good_amount = 0
    __sold_goods_info = []

    def __init__(self, name="", salary=0, greedy_level=1, status="Consultant"):
        self.__name = name
        self.__status = status
        self.__salary = salary
        self.greedy_level = greedy_level
        Worker.__amount += 1

    def __del__(self):
        print("{0} {1} Fired!".format(self.__status, self.__name))
        Worker.__amount -= 1

    def __str__(self):
        string = "Worker {0} {1}".format(self.__name, self.__status)
        return string

    def upscale_prices(self, goods_list):
        print(self.__status, self.__name,
              ": Black Friday! Prices are increased for {0} %".format(round((self.greedy_level - 1) * 100)))
        for good in goods_list:
            if isinstance(good, Good):
                good.Price = round(good.Price * self.greedy_level, 2)

    def sale_prices(self, goods_list, sale_coef=0.5):
        if 0 < sale_coef < 1:
            print(self.__status, self.__name,
                  ": Sales!!! Decreasing prices for {0}%".format(round((1 - sale_coef) * 100)))
            for good in goods_list:
                if isinstance(good, Good):
                    good.Price = round(good.Price * sale_coef, 2)
        else:
            print("What?")

    def sell_one_good(self, goods_list):
        if goods_list:
            delete_index = random.randint(0, len(goods_list) - 1)
            if isinstance(goods_list[delete_index], Good):
                good = goods_list.pop(delete_index)
                print(self.get_info(), " sold ", good.get_info())
                self.__salary += self.__salary_add_coef * good.Price
                self.__sold_good_amount += 1
                self.__sold_goods_info.append(good.get_info())

    def get_sold_goods_info(self):
        result = "{0} {1} Sold Nothing".format(self.__status, self.__name)
        if isinstance(self.__sold_goods_info, list) and self.__sold_goods_info:
            result = "{0} {1} Sold:".format(self.__status, self.__name)
            for info in self.__sold_goods_info:
                if isinstance(info, str):
                    result += info
        return result

    def get_name(self):
        return self.__name

    def get_status(self):
        return self.__status

    def set_status(self, value):
        self.__status = value

    def get_salary(self):
        return self.__salary

    def set_salary(self, value):
        self.__salary = value

    def get_sold_goods_amount(self):
        return self.__sold_good_amount

    def get_salary_coef(self):
        return self.__salary_add_coef

    def set_salary_coef(self, value):
        if 0 < value <= 1:
            self.__salary_add_coef = value

    def get_info(self):
        return "{0} {1} ( Greedy level = {2}, Salary {3}, Goods Sold {4})".format(self.__status,
                                                                                  self.__name,
                                                                                  self.greedy_level,
                                                                                  round(self.__salary, 2),
                                                                                  self.__sold_good_amount)

    @staticmethod
    def get_amount():
        return Worker.__amount

    Name = property(get_name)
    SoldGoodsAmount = property(get_sold_goods_amount)
    Status = property(get_status, set_status)
    Salary = property(get_salary, set_salary)
    SalaryCoef = property(get_salary_coef, set_salary_coef)
