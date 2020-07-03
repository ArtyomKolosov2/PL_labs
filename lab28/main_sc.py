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

    build = Builder("Toshiba")
    go = build.create_goods(10)
    eldorado = Seller("ELDORADO", go)

    eldorado.add_worker(Worker("Egor", salary=100, greedy_level=1.3))
    eldorado.add_worker(Worker("Petya", salary=200, greedy_level=1.8))
    eldorado.add_worker(Worker("Ivan", salary=150, greedy_level=1.1))
    eldorado.add_worker(Worker("Vasya", salary=560, greedy_level=1.4))
    print(eldorado.find_good_by_id(2))

    eldorado.get_random_worker().sell_one_good(eldorado.GoodsList)
    print("BestWorker", eldorado.find_best_worker())
    eldorado.get_random_worker().upscale_prices(eldorado.GoodsList)
    print(eldorado.get_random_worker().get_sold_goods_info())
    print(build.get_string_repr(eldorado.GoodsList))
    print("Amount of Worker class:", Worker.get_amount())
    print("Amount of Good class:", Good.get_amount())
    print("Amount of Builder class:", Builder.get_amount())
    print("Amount of Seller class:", Seller.get_amount())
    input("PressEnter")


if __name__ == "__main__":
    main()
