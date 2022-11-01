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


def populate_list(the_list):
    the_list.append({'ap': 1, 'tip': 'Apa', 'suma': 200})
    the_list.append({'ap': 1, 'tip': 'Gaz', 'suma': 300})
    the_list.append({'ap': 2, 'tip': 'Gaz', 'suma': 500})
    the_list.append({'ap': 4, 'tip': 'Canal', 'suma': 100})
    the_list.append({'ap': 69, 'tip': 'Altele', 'suma': 250})


def read_list(current_list, undo_list):
    n = int(input("Cate cheltuieli se citesc? "))
    for i in range(n):
        current_list.append({'ap': None, 'tip': None, 'suma': None})

        ap = input("Introduceti Apartamentul: ")
        while validate_ap(ap) == False:
            print("Apartament invalid!")
            ap = input("Introduceti Apartamentul: ")
        current_list[len(current_list) - 1]['ap'] = ap

        tip = input("Introduceti Tipul: ")
        while validate_tip(tip) == False:
            print("Tip invalid!")
            tip = input("Introduceti Tipul: ")
        current_list[len(current_list) - 1]['tip'] = tip

        suma = input("Introduceti Suma: ")
        while validate_suma(suma) == False:
            print("Suma invalida!")
            suma = input("Introduceti Suma: ")
        current_list[len(current_list) - 1]['suma'] = suma

        undo_list.append(copy_list(current_list))


def edit_list(cheltuieli_list, undo_list):
    n = int(input("Cate cheltuieli doresti sa modifici? "))
    for i in range(n):
        ap = input("Introduce Apartamentul: ")
        while validate_ap(ap) == False:
            print("Apartament invalid!")
            ap = input("Introduceti Apartamentul: ")
        ap=int(ap)
        tip = input("Introduceti Tipul: ")
        while validate_tip(tip) == False:
            print("Tip invalid!")
            tip = input("Introduceti Tipul: ")
        tip=str(tip)
        ok = 0  # verifica existenta cheltuielii
        for i in range(len(cheltuieli_list)):
            print(cheltuieli_list[i]['ap'])
            print(cheltuieli_list[i]['tip'])
            if cheltuieli_list[i]['ap'] == ap and cheltuieli_list[i]['tip'] == tip:
                ok = 1
                suma = input("Introduceti suma noua: ")
                while validate_suma(suma) == False:
                    print("Suma invalida!")
                    suma = input("Introduceti suma noua: ")
                cheltuieli_list[i]['suma'] = suma
                undo_list.append(copy_list(cheltuieli_list))
                break

        if ok == 0:
            print("Nu Exista aceasta cheltuiala! ")


def delete_cheltuieli_ap(cheltuieli_list, undo_list):
    ap = int(input("Introduce numarul apartamentului: "))
    while validate_ap(ap) == False:
        print("Apartament invalid!")
        ap = int(input("Introduce numarul apartamentului: "))
    for j in range(len(cheltuieli_list)):
        for i in range(len(cheltuieli_list)):
            if cheltuieli_list[i]['ap'] == ap:
                cheltuieli_list.pop(i)
                break
    undo_list.append(copy_list(cheltuieli_list))


def delete_cheltuieli_consec(cheltuieli_list, undo_list):
    nr_start = int(input("Introduce numarul apartamentului de la care se incepe stergerea: "))
    while validate_ap(nr_start) == False:
        print("Apartament invalid!")
        nr_start = int(input("Introduce numarul apartamentului de la care se incepe stergerea: "))
    nr_stop = int(input("Introduce numarul apartamentului pana la care se sterge: "))
    while validate_ap(nr_stop) == False:
        print("Apartament invalid!")
        nr_stop = int(input("Introduce numarul apartamentului pana la care se sterge: "))
    for j in range(len(cheltuieli_list)):
        for i in range(len(cheltuieli_list)):
            if cheltuieli_list[i]['ap'] >= nr_start and cheltuieli_list[i]['ap'] <= nr_stop:
                cheltuieli_list.pop(i)
                break
    undo_list.append(copy_list(cheltuieli_list))


def delete_cheltuieli_tip(cheltuieli_list, undo_list):
    tipul = str(input("Introduce tipul cheltuielii: "))
    while validate_tip(tipul) == False:
        print("Tipul invalid!")
        tipul = str(input("Introduce tipul cheltuielii: "))
    for j in range(len(cheltuieli_list)):
        for i in range(len(cheltuieli_list)):
            if cheltuieli_list[i]['tip'] == tipul:
                cheltuieli_list.pop(i)
                break
    undo_list.append(copy_list(cheltuieli_list))


def tiparire_sume_mai_mari(cheltuieli_list, suma):
    lista = []
    ap = 0
    cnt = 0
    while cnt != len(cheltuieli_list):
        ap += 1
        el_suma = 0
        for i in range(len(cheltuieli_list)):
            if cheltuieli_list[i]['ap'] == ap:
                el_suma += cheltuieli_list[i]['suma']
                cnt += 1
        if el_suma >= suma:
            lista.append(ap)
    return lista


def tiparire_cheltuieeli_tip(cheltuieli_list, tipul):
    lista = []
    for i in range(len(cheltuieli_list)):
        if tipul == cheltuieli_list[i]['tip']:
            ap=str(cheltuieli_list[i]['ap'] )
            suma=str(cheltuieli_list[i]['suma'] )
            el_cheltuiala = "Apartamentul " + ap + " suma " + suma
            lista.append(el_cheltuiala)
    return lista


def raport_sum_tip(cheltuieli_list, tipul):
    suma = 0
    for i in range(len(cheltuieli_list)):
        if tipul == cheltuieli_list[i]['tip']:
            suma += cheltuieli_list[i]['suma']
    return suma


def raport_ap_sort_tip(cheltuieli_list, tip):
    lista = []
    for i in range(len(cheltuieli_list)):
        if tip == cheltuieli_list[i]['tip']:
            lista.append(cheltuieli_list[i]['ap'])
    lista.sort()
    return lista


def raport_total_ap(cheltuieli_list, ap):
    suma = 0
    for i in range(len(cheltuieli_list)):
        if ap == cheltuieli_list[i]['ap']:
            suma += cheltuieli_list[i]['suma']
    return suma


def filter_tip(cheltuieli_list, tipul):
    lista = []
    for i in range(len(cheltuieli_list)):
        if cheltuieli_list[i]['tip'] != tipul:
            lista.append(cheltuieli_list[i])
    return lista


def filter_suma(cheltuieli_list, suma):
    lista = []
    for i in range(len(cheltuieli_list)):
        if cheltuieli_list[i]['suma'] >= suma:
            lista.append(cheltuieli_list[i])
    return lista


def copy_list(lst):
    lst_copy = []
    for elem in lst:
        lst_copy.append(elem)
    return lst_copy


def undo_step(undo_list):
    lista = undo_list[len(undo_list) - 2]
    return lista
