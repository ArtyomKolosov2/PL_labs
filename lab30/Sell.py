# Класс Seller, который работает с классами Worker, Good
# Класс Seller, общий класс, в котором описываются и существенные
# характеристики работника, товара
# Version: 1.0
# Group: 10701219
# Author: Колосов Артём Александрович
# Date: 16.4.2020

from Goods import Good
from Worker import WorkerConsultant, Worker
import random


class Seller:
    __amount = 0

    def __init__(self, name="", goods_list=[], worker_list=[]):
        if not (isinstance(goods_list, list) and isinstance(name, str) and isinstance(worker_list, list)):
            raise TypeError("Types of arguments are wrong!")
        self.__goods_list = goods_list[:]
        goods_list.clear()
        self.__worker_list = worker_list[:]
        worker_list.clear()
        self.__name = name
        Seller.__amount += 1

    def __del__(self):
        for worker in self.__worker_list:
            if isinstance(worker, Worker):
                del worker
        for good in self.__goods_list:
            if isinstance(good, Good):
                del good
        print(self.__name, "Closed")
        Seller.__amount -= 1

    def __str__(self):
        string = "Seller {0}".format(self.__name)
        return string

    def calculate_prices(self):
        all_price = 0
        for good in self.__goods_list:
            if isinstance(good, Good):
                all_price += good.Price
        return round(all_price, 2)

    def add_goods(self, new_goods_list):
        if isinstance(new_goods_list, list):
            for new_good in new_goods_list:
                if isinstance(new_good, Good):
                    self.__goods_list.append(new_good)

    def find_good_by_id(self, identity):
        if not (isinstance(identity, int) and self.__goods_list):
            return None
        result = "NotFound"
        for good in self.__goods_list:
            if isinstance(good, Good):
                if good.Identity == identity:
                    result = good
                    break
        return result

    def find_best_consultant(self):
        if not isinstance(self.__worker_list, list):
            return None
        max_index = 0
        maximum = self.__worker_list[max_index].SoldGoodsAmount

        for i in range(0, len(self.__worker_list)):
            if isinstance(self.__worker_list[i], WorkerConsultant):
                new_max = self.__worker_list[i].SoldGoodsAmount
                if 0 <= maximum < new_max:
                    maximum = new_max
                    max_index = i
        return self.__worker_list[max_index]

    def find_worst_consultant(self):
        if not isinstance(self.__worker_list, list):
            return None
        min_index = 0
        minimum = self.__worker_list[min_index].SoldGoodsAmount

        for i in range(0, len(self.__worker_list)):
            if isinstance(self.__worker_list[i], WorkerConsultant):
                new_min = self.__worker_list[i].SoldGoodsAmount
                if 0 <= new_min < minimum:
                    minimum = new_min
                    min_index = i
        return self.__worker_list[min_index]

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.__worker_list.append(worker)

    def get_random_consultant(self):
        result = None
        repeat = len(self.__worker_list)
        while repeat > 0 and not isinstance(result, WorkerConsultant):
            result = random.choice(self.__worker_list)
        return result

    def get_highest_salary_worker(self):
        if not isinstance(self.__worker_list, list):
            return None
        highest_index = 0
        highest = self.__worker_list[0].Salary if isinstance(self.__worker_list[0], Worker) else None
        for i in range(len(self.__worker_list)):
            if isinstance(self.__worker_list[i], Worker): # Полиморфизм
                new_high = self.__worker_list[i].Salary
                if new_high > highest:
                    highest = new_high
                    highest_index = i
        return self.__worker_list[highest_index]

    def get_workers_info(self):
        result = "List Of Workers:\n"
        for worker in self.__worker_list:
            if isinstance(worker, Worker): # Полиморфизм
                result += worker.get_info() + "\n"
        return result

    def get_info(self):
        return self.__name


    def get_name(self):
        return self.__name

    def get_goods_list(self):
        return self.__goods_list

    def get_worker_list(self):
        return self.__worker_list

    @classmethod
    def get_amount(cls):
        return cls.__amount

    GoodsList = property(get_goods_list)
    WorkerList = property(get_worker_list)
    Name = property(get_name)
