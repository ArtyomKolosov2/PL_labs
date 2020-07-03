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
    worker_list = []
    amount = 0

    def __init__(self, goods_list, name):
        self.goods_list = goods_list[:]
        goods_list.clear()
        self.name = name
        Seller.amount += 1

    def __del__(self):
        for worker in self.worker_list:
            if isinstance(worker, Worker):
                del worker
        for good in self.goods_list:
            if isinstance(good, Good):
                del good
        print(self.name, " Closed")
        Seller.amount -= 1

    def calculate_prices(self):
        all_price = 0
        for good in self.goods_list:
            if isinstance(good, Good):
                all_price += good.price
        return all_price

    def find_good_by_id(self, identity):
        if not (isinstance(identity, int) and self.goods_list):
            return None
        result = "NotFound"
        for good in self.goods_list:
            if isinstance(good, Good):
                if good.identity == identity:
                    result = good.get_info()
                    break
        return result

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.worker_list.append(worker)

    def get_random_worker(self):
        return random.choice(self.worker_list)

    def get_info(self):
        return self.name

    def get_workers_info(self):
        result = "List Of Workers:\n"
        for worker in self.worker_list:
            if isinstance(worker, Worker):
                result += worker.get_info() + "\n"
        return result
