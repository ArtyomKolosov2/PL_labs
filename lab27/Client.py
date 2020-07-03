class Client:
    number_of_clients = 0

    def __init__(self, name, money, id):
        self.name = name
        self.money = money
        self.id = id
        Client.number_of_clients += 1

    def __del__(self):
        print(self.name, " - deleted")
        Client.number_of_clients -= 1

    def __repr__(self):
        return self.name


def main():
    lst = []
    for i in range(20):
        lst.append(Client("A"+str(i), 100*i, i))
    print(lst)


main()