def derevo():
    k=0
    while k < 3:
        ans = input("Отгадайте загадку 1, у вас 3 попыток - Зимой и летом одним цветом:")
        if ans == "Elka":
            print("Правильно")
            break
        else:
            k += 1
            print("НеправильноБ это была ваша", k, "попытка")
            if (k >= 3):
                print("Лох")
    while k < 3:
        xns = input("Ёлка? ")
        if xns == "Elka":
            print("Правильно")
            break
        else:
            k += 1
            print("НеправильноБ это была ваша", k, "попытка")
            if (k >= 3):
                print("Лох")
    while k < 3:
        dns = input("Ёлка?? ")
        if dns == "Elka":
            print("Правильно")
            break
        else:
            k += 1
            print("НеправильноБ это была ваша", k, "попытка")
            if (k >= 3):
                print("Лох")
                break
derevo()
