try:
    print("Pohatok kody")
    print(10/0)
    print("Nema pomulok")
except (NameError, ZeroDivisionError) as error:
    print(error)#print("error:")
else:
    print("else")
finally:
    print("Kod akuq byde v bydakomy vupadky")

print("Kod pisla kapsylu")
