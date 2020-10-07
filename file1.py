class VolonteersRes:
    def __init__(self, name, city, status):
        self.name = name
        self.city = city
        self.status = status
    def returnMan(self):
        print(self.name, self.city, self.status)

class donatersRes:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def returnMan(self):
        print(self.name, self.balance)