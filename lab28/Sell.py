# Класс Seller, который работает с классами Worker, Good
# Класс Seller, общий класс, в котором описываются и существенные
# характеристики работника, товара
# Version: 1.0
# Group: 10701219
# Author: Колосов Артём Александрович
# Date: 16.4.2020

from Goods import Good
from Worker import Worker
import random


class Seller:
    __amount = 0

    def __init__(self, name="", goods_list=[], worker_list=[]):
        self.__goods_list = goods_list[:]
        self.__worker_list = worker_list[:]
        goods_list.clear()
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
        print(self.__name, " Closed")
        Seller.__amount -= 1

    def __str__(self):
        string = "Seller {0}".format(self.__name)
        return string

    @staticmethod
    def get_amount():
        return Seller.__amount

    def calculate_prices(self):
        all_price = 0
        for good in self.__goods_list:
            if isinstance(good, Good):
                all_price += good.Price
        return all_price

    def find_good_by_id(self, identity):
        if not (isinstance(identity, int) and self.__goods_list):
            return None
        result = "NotFound"
        for good in self.__goods_list:
            if isinstance(good, Good):
                if good.Identity == identity:
                    result = good.get_info()
                    break
        return result

    def find_best_worker(self):
        if not isinstance(self.__worker_list, list):
            return None
        max_index = 0
        maximum = self.__worker_list[max_index].SoldGoodsAmount

        for i in range(0, len(self.__worker_list)):
            if isinstance(self.__worker_list[i], Worker):
                new_max = self.__worker_list[i].SoldGoodsAmount
                if 0 <= maximum < new_max:
                    maximum = new_max
                    max_index = i
        return self.__worker_list[max_index].get_info()


    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.__worker_list.append(worker)

    def get_random_worker(self):
        return random.choice(self.__worker_list)

    def get_info(self):
        return self.__name

    def get_workers_info(self):
        result = "List Of Workers:\n"
        for worker in self.__worker_list:
            if isinstance(worker, Worker):
                result += worker.get_info() + "\n"
        return result

    def get_name(self):
        return self.__name

    def get_goods_list(self):
        return self.__goods_list

    def get_worker_list(self):
        return self.__worker_list

    GoodsList = property(get_goods_list)
    WorkerList = property(get_worker_list)
    Name = property(get_name)
