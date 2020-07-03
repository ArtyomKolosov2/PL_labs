# Главный Файл, который собирает
# все классы и позволяет с ними работать
#
# Version: 1.0
# Group: 10701219
# Author: Колосов Артём Александрович
# Date: 16.4.2020

from Builder import Builder
from Sell import Seller
from Worker import Worker
from Goods import Good


def main():
    
    build = Builder()
    go = build.create_goods(10)
    eldorado = Seller(go, "Eldorado")
    
    eldorado.add_worker(Worker("Vasya", salary=100, greedy_level=1.3))
    eldorado.add_worker(Worker("Petya", salary=200, greedy_level=1.8))
    eldorado.add_worker(Worker("Ivan", salary=150, greedy_level=1.1))
    eldorado.add_worker(Worker("Vasya", salary=560, greedy_level=1.4))
    
    print(eldorado.get_random_worker().get_sold_goods_info())
    print(build.get_string_repr(eldorado.goods_list))
    print("Amount of Worker class:", Worker.amount_of_workers)
    print("Amount of Good class:", Good.amount)
    print("Amount of Builder class:", Builder.amount)
    print("Amount of Seller class:", Builder.amount)
    input("PressEnter")


if __name__ == "__main__":
    main()
