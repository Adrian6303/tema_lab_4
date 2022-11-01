def validate_ap(el):
    el = int(el)
    if el <= 0:
        return False
    else:
        return True


def validate_tip(el):
    lista_tipuri = ["Apa", "Canal", "Incalzire", "Gaz", "Altele"]
    ok = 0
    for elem in lista_tipuri:
        if elem == el:
            ok = 1
            break
    if ok == 0:
        return False
    return True


def validate_suma(el):
    el = int(el)
    if el < 0:
        return False
    return True


def copy_list(lst):
    lst_copy = []
    for elem in lst:
        lst_copy.append(elem)
    return lst_copy
