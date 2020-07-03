# Главный Файл, который собирает
# все классы и позволяет с ними работать
#
# Version: 1.0
# Group: 10701219
# Author: Колосов Артём Александрович
# Date: 16.4.2020

from Builder import Builder
from Sell import Seller
from Worker import WorkerConsultant, WorkerManager
from Goods import Good
from random import randint


def main():
    build = Builder("Toshiba")
    amount_of_goods = 15
    splitter = 60
    goods = build.create_goods(amount_of_goods)
    eldorado = Seller("Eldorado")
    eldorado.add_goods(goods)

    print(build.get_string_repr(eldorado.GoodsList), "\n", "=" * splitter)
    cons_petya = WorkerConsultant("Petya", salary=splitter, greedy_level=1.1)
    cons_vasya = WorkerConsultant("Vasya", salary=200, greedy_level=1.3)
    cons_andrea = WorkerConsultant("Andrea", salary=150, greedy_level=1.5)
    man_victor = WorkerManager("Victor", salary=1000)

    eldorado.add_worker(cons_petya)
    eldorado.add_worker(cons_vasya)
    eldorado.add_worker(cons_andrea)
    eldorado.add_worker(man_victor)

    for i in range(len(eldorado.GoodsList) - 10):
        eldorado.get_random_consultant().sell_one_good(eldorado.GoodsList)

    print("=" * splitter)
    eldorado.get_random_consultant().upscale_prices(eldorado.GoodsList)
    print("=" * splitter)

    for i in range(len(eldorado.GoodsList) - 5):
        eldorado.get_random_consultant().sell_one_good(eldorado.GoodsList)

    print(eldorado.get_workers_info())
    print("=" * splitter)
    man_victor.fire_worker(eldorado.find_worst_consultant(), eldorado.WorkerList)
    print("=" * splitter)
    
    print("\n", eldorado.get_workers_info(), sep="")
   
    print(eldorado.get_random_consultant().get_sold_goods_info())
    print("Highest salary", eldorado.get_highest_salary_worker().get_info())
    print("=" * splitter)
    search_id = randint(0, amount_of_goods-1)
    print("Search Results of id {0}: {1}".format(search_id, eldorado.find_good_by_id(search_id)))
    print("=" * splitter)
    
    print(build.get_string_repr(eldorado.GoodsList))
    
    print("=" * splitter)
    print("Cost of all goods in", eldorado, eldorado.calculate_prices())
    print("=" * splitter)
    
    print("Amount of WorkerConsultant class:", WorkerConsultant.get_amount())
    print("Amount of WorkerManager class:", WorkerManager.get_amount())
    print("Amount of Good class:", Good.get_amount())
    print("Amount of Builder class:", Builder.get_amount())
    print("Amount of Seller class:", Seller.get_amount())
    input("PressEnter")


if __name__ == "__main__":
    main()
