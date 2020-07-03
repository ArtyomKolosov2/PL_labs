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


def main():

    build = Builder()

    goods_list = build.create_goods(10)

    eldorado = Seller(goods_list, "eldorado")

    worker_vasya = Worker("Вася", salary=100, greedy_level=1.4)

    worker_petya = Worker("Петя", salary=80, greedy_level=1.2)

    eldorado.add_worker(worker_petya)
    eldorado.add_worker(worker_vasya)

    worker_vasya.sell_one_good(eldorado.goods_list)
    worker_petya.sell_one_good(eldorado.goods_list)
    print(eldorado.get_workers_info())
    

    print(build.get_string_repr(eldorado.goods_list))

    worker_petya.sale_prices(eldorado.goods_list, 0.8)

    worker_vasya.upscale_prices(eldorado.goods_list)
    print(build.get_string_repr(eldorado.goods_list))
    input()

if __name__ == "__main__":
    main()
