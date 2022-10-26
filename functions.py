def validate_list(elem):
    el_ap = int(elem.split(".")[0])
    el_tip = str(elem.split(".")[1])
    el_tip = str(el_tip.split("=")[0])
    el_suma = int(elem.split("=")[1])
    if validate_ap(el_ap) == False:
        return False
    if validate_tip(el_tip) == False:
        return False
    if validate_suma(el_suma) == False:
        return False
    return True


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


def read_list(current_list):
    # Lista sa fie data sub forma: 1.Apa=200, 2.Canal=500, 3.Gaz=700
    # list_as_string = input("Introduceti lista sub formatul cerut: ")
    # the_list = list_as_string.split()
    # return the_list
    n = int(input("Cate cheltuieli se citesc? "))
    for i in range(n):
        cheltuiala = input("Introduceti cheltuiala sub forma NrAp.TipCheltiiala=Suma : ")
        if validate_list(cheltuiala) == True:
            current_list.append(cheltuiala)
        else:
            print("Cheltuiala Invalida!")


def populate_list(the_list):
    """
    Populeaza lista data cu niste seriale predefinite
    :param the_list: lista data
    :type the_list: list
    :return: -; lista data se modifica prin adaugarea cheltuielilor date
    :rtype:
    """
    the_list.append("1.Apa=200")
    the_list.append("1.Gaz=300")
    the_list.append("2.Gaz=500")
    the_list.append("4.Canal=100")
    the_list.append("1.Canal=100")
    the_list.append("69.Apa=250")
    the_list.append("250.Apa=250")


def edit_list(current_list):
    n = int(input("Cate cheltuieli doresti sa modifici? "))
    for i in range(n):
        el_edit = str(input("Introduce cheltuiala ce trebuie modificata sub forma NrAp.TipCheltuiala : "))
        cnt = 0  # contor pozitie, el element lista
        ok = 0  # verifica existenta cheltuielii
        for el in current_list:
            if el[0:len(el_edit)] == el_edit:
                ok = 1
                cheltuiala = str(input("Introduceti suma noua: "))
                while validate_suma(cheltuiala) == False:
                    print("Suma invalida!")
                    cheltuiala = str(input("Introduceti suma noua: "))
                current_list[cnt] = el_edit + '=' + cheltuiala
                break

            cnt += 1
        if ok == 0:
            print("Nu Exista aceasta cheltuiala! ")


def delete_cheltuieli_ap(current_list):
    n = str(input("Introduce numarul apartamentului: "))
    while validate_ap(n) == False:
        print("Apartament invalid!")
        n = str(input("Introduce numarul apartamentului: "))
    for i in range(len(current_list)):
        for el in current_list:
            if el[0:len(n)] == n:
                current_list.remove(el)
                break


def delete_cheltuieli_consec(current_list):
    nr_start = int(input("Introduce numarul apartamentului de la care se incepe stergerea: "))
    while validate_ap(nr_start) == False:
        print("Apartament invalid!")
        nr_start = int(input("Introduce numarul apartamentului de la care se incepe stergerea: "))
    nr_stop = int(input("Introduce numarul apartamentului pana la care se sterge: "))
    while validate_ap(nr_stop) == False:
        print("Apartament invalid!")
        nr_stop = int(input("Introduce numarul apartamentului pana la care se sterge: "))
    for i in range(len(current_list)):
        for el in current_list:
            el_nr = int(el.split(".")[0])
            if el_nr >= nr_start and el_nr <= nr_stop:
                current_list.remove(el)
                break


def delete_cheltuieli_tip(current_list):
    tipul = str(input("Introduce tipul cheltuielii: "))
    while validate_tip(tipul) == False:
        print("Tipul invalid!")
        tipul = str(input("Introduce tipul cheltuielii: "))
    for i in range(len(current_list)):
        for el in current_list:
            el_tip = str(el.split(".")[1])
            el_tip = str(el_tip.split("=")[0])
            if el_tip == tipul:
                current_list.remove(el)
                break


def tiparire_sume_mai_mari(current_list, suma):
    lista = []
    ap = 0
    cnt = 0
    while cnt != len(current_list):
        ap += 1
        el_suma = 0
        for el in current_list:
            if ap == int(el.split(".")[0]):
                el_suma += int(el.split("=")[1])
                cnt += 1
        if el_suma >= suma:
            lista.append(ap)
    return lista


def tiparire_cheltuieeli_tip(current_list, tipul):
    lista = []
    for el in current_list:
        el_tip = str(el.split(".")[1])
        el_tip = str(el_tip.split("=")[0])
        if tipul == el_tip:
            el_cheltuiala = str(el.split(".")[0])
            el_cheltuiala = "Apartamentul " + el_cheltuiala + " suma " + str(el.split("=")[1])
            lista.append(el_cheltuiala)
    return lista


def raport_sum_tip(current_list, tipul):
    suma = 0
    for el in current_list:
        el_tip = str(el.split(".")[1])
        el_tip = str(el_tip.split("=")[0])
        if tipul == el_tip:
            el_suma = int(el.split("=")[1])
            suma += el_suma
    return suma


def raport_ap_sort_tip(current_list, tip):
    lista = []
    for el in current_list:
        el_tip = str(el.split(".")[1])
        el_tip = str(el_tip.split("=")[0])
        if tip == el_tip:
            el_ap = int(el.split(".")[0])
            lista.append(el_ap)
    lista.sort()
    return lista


def raport_total_ap(current_list, ap):
    suma = 0
    for el in current_list:
        el_ap = str(el.split(".")[0])
        if ap == el_ap:
            el_suma = int(el.split("=")[1])
            suma += el_suma
    return suma


def filter_tip(current_list, tipul):
    lista = []
    for el in current_list:
        el_tip = str(el.split(".")[1])
        el_tip = str(el_tip.split("=")[0])
        if el_tip != tipul:
            lista.append(el)
    return lista


def filter_suma(current_list, suma):
    lista = []
    for el in current_list:
        el_suma = int(el.split("=")[1])
        if el_suma >= suma:
            lista.append(el)
    return lista


def copy_list(lst):
    lst_copy = []
    for elem in lst:
        lst_copy.append(elem)
    return lst_copy
