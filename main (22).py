def sehet ():
    a = input ("Введите первое число:")
    a = float (a)
    b = input ("Введите второе число:")
    b = float (b)
    if a > b:
        print (a-b)
    else:
        print (b-a)
    return a, b
    
c, d = sehet ()
e, f = sehet ()
z, x = sehet ()