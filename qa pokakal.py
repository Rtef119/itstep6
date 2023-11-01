def cheker(var_1):
    if type(var_1) != str:
        raise TypeError (f"Vubacte, ale mu ne mogemo prazybatu z {type(var_1)},mu prazuemo z str")

    else:
        return var_1

first_var = Hallo
cheker(first_var)
