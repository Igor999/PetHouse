from file1 import VolonteersRes, donatersRes
volonteers = []
donaters = []

while True:
    choose_man = int(input("1 - внести сотрудника, 2 - внести пожертвование, 0 - выход"))
    if choose_man == 0:
        print("Выход")
        break
    elif choose_man == 1:
        volonteers.append({"name": input("Введите имя волонтера: "),
                           "city": input("Введите название города: "),
                           "status": input("Введите его должность: "),
                           })
    elif choose_man == 2:
        donaters.append({"name": input("Введите имя жертвователя: "),
                         "balance": float(input("Введите сумму: ")),
                         })
    else:
        print("Выберите 0 или 1 или 2")

# print(volonteers)
# print(donaters)


class VolonteersPrint(VolonteersRes):
    def showVolonteers(self):
        print(self.name+", г."+self.city+", статус", self.status)

class DonatersPrint(donatersRes):
    def showDonaters(self):
        print("Клиент «"+self.name+"». Баланс: "+str(self.balance),"руб.")

if len(volonteers) != 0:
    for volonteer in volonteers:
        man = VolonteersPrint(name=volonteer.get("name"),
            city=volonteer.get("city"),
            status=volonteer.get("status"))
        man.showVolonteers()

if len(donaters)!=0:
    for donater in donaters:
        man = DonatersPrint(name=donater.get("name"),
            balance=donater.get("balance"))
        man.showDonaters()