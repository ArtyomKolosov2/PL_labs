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

    def __init__(self, name="", salary=0, status=""):
        self.__name = name
        self.__salary = salary
        self.__status = status

    def say(self, msg):
        print(self.__status, self.__name, msg)

    def __str__(self):
        return self.__status + " " + self.__name

    def __del__(self):
        print(self.__name, self.__status, "Fired")

    def get_name(self):
        return self.__name

    def get_status(self):
        return self.__status

    def get_salary(self):
        return self.__salary

    def set_salary(self, value):
        self.__salary = value

    def get_info(self):
        return self.__name + self.__status

    Name = property(get_name)
    Status = property(get_status)
    Salary = property(get_salary, set_salary)


class WorkerManager(Worker):
    __amount = 0

    def __init__(self, name="", salary=0):
        if not (isinstance(name, str) and isinstance(salary, int)):
            raise TypeError("Types of arguments are wrong!")
        super().__init__(name, salary, "Manager")
        WorkerManager.__amount += 1

    def __del__(self):
        print("{0} {1} Deleted!".format(self.Status, self.Name))
        WorkerManager.__amount -= 1

    def __str__(self):
        string = "{0} {1}".format(self.Status, self.Name)
        return string

    def say(self, msg):
        print(self, "says", msg)

    def get_info(self):
        return "{0} {1} (Salary = {2})".format(self.Status,
                                               self.Name,
                                               round(self.Salary, 2))

    def fire_worker(self, worker, worker_list):
        if isinstance(worker_list, list):
            if isinstance(worker, WorkerConsultant):
                if worker in worker_list:
                    worker_list.remove(worker)
                    self.say("fired {0}".format(worker))

    @classmethod
    def get_amount(cls):
        return cls.__amount


class WorkerConsultant(Worker):
    __amount = 0
    __salary_add_coef = 0.1

    def __init__(self, name="", salary=0, greedy_level=1.1):
        if not (isinstance(name, str) and isinstance(salary, int) and isinstance(greedy_level, float)):
            raise TypeError("Types of arguments are wrong!")
        super().__init__(name, salary, "Consultant")
        self.__greedy_level = greedy_level
        self.__sold_goods_info = []
        self.__sold_good_amount = 0
        WorkerConsultant.__amount += 1

    def __del__(self):
        print("{0} {1} Deleted!".format(self.Status, self.Name))
        WorkerConsultant.__amount -= 1

    def __str__(self):
        string = "Worker {0} {1}".format(self.Name, self.Status)
        return string

    def say(self, msg):
        print(self, "says", msg)

    def sell_one_good(self, goods_list):
        if goods_list:
            delete_index = random.randint(0, len(goods_list) - 1)
            if isinstance(goods_list[delete_index], Good):
                good = goods_list.pop(delete_index)
                print(self.get_info(), "sold", good.get_info(), end='')
                self.Salary += self.__salary_add_coef * good.Price
                self.__sold_good_amount += 1
                self.__sold_goods_info.append(good.get_info())

    def sale_prices(self, goods_list, sale_coef=0.5):
        if 0 < sale_coef < 1:
            self.say("Sales!!! Decreasing prices for {0} %".format(round((1 - sale_coef) * 100)))
            for good in goods_list:
                if isinstance(good, Good):
                    good.Price = round(good.Price * sale_coef, 2)
        else:
            self.say("What?")

    def upscale_prices(self, goods_list):
        self.say(msg="Black Friday! Prices are increased for {0} %".format(round((self.__greedy_level - 1) * 100)))
        for good in goods_list:
            if isinstance(good, Good):
                good.Price = round(good.Price * self.__greedy_level, 2)

    def get_sold_goods_info(self):
        result = "{0} {1} Sold Nothing".format(self.Status, self.Name)
        if isinstance(self.__sold_goods_info, list) and self.__sold_goods_info:
            result = "{0} {1} Sold:\n".format(self.Status, self.Name)
            for info in self.__sold_goods_info:
                if isinstance(info, str):
                    result += info
        return result

    def get_info(self):
        return "{0} {1} ( Greedy level = {2}, Salary = {3}, Goods Sold = {4})".format(self.Status,
                                                                                      self.Name,
                                                                                      self.__greedy_level,
                                                                                      round(self.Salary, 2),
                                                                                      self.__sold_good_amount)

    def get_sold_goods_amount(self):
        return self.__sold_good_amount

    def get_salary_coef(self):
        return self.__salary_add_coef

    def get_greedy_level(self):
        return self.__greedy_level

    def set_greedy_level(self, value):
        if 0 < value < 3:
            self.__greedy_level = value

    def set_salary_coef(self, value):
        if 0 < value <= 1:
            self.__salary_add_coef = value

    @classmethod
    def get_amount(cls):
        return cls.__amount

    SoldGoodsAmount = property(get_sold_goods_amount)
    SalaryCoef = property(get_salary_coef, set_salary_coef)
    GreedyLevel = property(get_greedy_level, set_greedy_level)
