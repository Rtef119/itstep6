try:
    print("Pohatok kody")                     #print(6/0)                   2
    print(10/0)
    print("Nema pomulok")                     #except ZeroDivisionError:    3
except NameError:
    print("error")                            #print("no")                  4
except ZeroDivisionError:
    print("Tut /0 Artem")

print("Kod pisla kapsylu")
