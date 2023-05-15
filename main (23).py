def sehet ():
    a = int(input("Введите первое число:"))
    b = int(input("Введите второе число:"))
    if a > b:
        print (a-b)
    else:
        print (b-a)
    return a, b
    
c, d = sehet ()
e, f = sehet ()
z, x = sehet ()