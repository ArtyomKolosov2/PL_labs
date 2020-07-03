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

    def __init__(self, goods_list, name):
        self.goods_list = goods_list
        self.name = name

    def calculate_prices(self, goods_list):
        all_price = 0
        for good in goods_list:
            if isinstance(good, Good):
                all_price += good.price
        return all_price

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
