class Worker:
    def __init__(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary

class Seller:
    def __init__(self, name, worker):
        self.worker = worker
        self.name = name

    def get_name(self):
        return self.name

    def get_worker_salary(self):
        return self.worker.get_salary()

work = Worker(777)
sell = Seller("Pe32+", work)
print(sell.get_name())
print(sell.get_worker_salary())
