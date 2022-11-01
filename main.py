from debug import debug_auto
from menu import *
from functions import *


def start():
    cheltuieli_list=[]
    populate_list(cheltuieli_list)
    undo_list = []
    undo_list.append(copy_list(cheltuieli_list))
    debug_auto()
    while True:
        print_menu()
        print('Lista cheltuieli bloc: ', cheltuieli_list)
        option = int(input("Optiunea dumneavoastra este: "))
        if option == 1:
            print_opt1_menu()
            option1 = int(input("Optiunea dumneavoastra este: "))
            if option1 == 1:
                read_list(cheltuieli_list, undo_list)

            if option1 == 2:
                edit_list(cheltuieli_list, undo_list)
            if option1 == 3:
                continue

        if option == 2:
            print_opt2_menu()
            option2 = int(input("Optiunea dumneavoastra este:"))
            if option2 == 1:
                delete_cheltuieli_ap(cheltuieli_list, undo_list)
            if option2 == 2:
                delete_cheltuieli_consec(cheltuieli_list, undo_list)
            if option2 == 3:
                delete_cheltuieli_tip(cheltuieli_list, undo_list)
            if option2 == 4:
                continue
        if option == 3:
            print_opt3_menu()
            option3 = int(input("Optiunea dumneavoastra este:"))
            if option3 == 1:
                suma = int(input("Introduce suma: "))
                while validate_suma(suma) == False:
                    print("Suma invalida!")
                    suma = int(input("Introduce suma: "))
                print("Lista apartamente: ", tiparire_sume_mai_mari(cheltuieli_list, suma))

            if option3 == 2:
                tip = str(input("Introduceti tipul: "))
                while validate_tip(tip) == False:
                    print("Tipul invalid!")
                    tip = str(input("Introduceti tipul: "))
                print("Lista cheltuieli: ", tiparire_cheltuieeli_tip(cheltuieli_list, tip))
            if option3 == 3:
                print("nu e gata")
            if option3 == 4:
                continue
        if option == 4:
            print_opt4_menu()
            option4 = int(input("Optiunea dumneavoastra este:"))
            if option4 == 1:
                tip = str(input("Introduceti tipul: "))
                while validate_tip(tip) == False:
                    print("Tipul invalid!")
                    tip = str(input("Introduceti tipul: "))
                print("Suma totala pentru ", tip, ": ", raport_sum_tip(cheltuieli_list, tip))
            if option4 == 2:
                tip = str(input("Introduceti tipul: "))
                while validate_tip(tip) == False:
                    print("Tipul invalid!")
                    tip = str(input("Introduceti tipul: "))
                print("Apartamentele ce au cheltuieli de tip ", tip, ": ", raport_ap_sort_tip(cheltuieli_list, tip))
            if option4 == 3:
                ap = int(input("Introduce apartament: "))
                while validate_ap(ap) == False:
                    print("Apartament invalid!")
                    ap = int(input("Introduce apartament: "))
                print("Totalul cheltuielilor pentru apartamentul", ap, ": ", raport_total_ap(cheltuieli_list, ap))
            if option4 == 4:
                continue
        if option == 5:
            print_opt5_menu()
            option5 = int(input("Optiunea dumneavoastra este:"))
            if option5 == 1:
                tip = str(input("Introduceti tipul: "))
                while validate_tip(tip) == False:
                    print("Tipul invalid!")
                    tip = str(input("Introduceti tipul: "))
                print("Lista filtrata: ", filter_tip(cheltuieli_list, tip))
            if option5 == 2:
                suma = int(input("Introduceti suma: "))
                while validate_suma(suma) == False:
                    print("Suma invalida!")
                    suma = int(input("Introduceti suma: "))
                print("Lista filtrata: ", filter_suma(cheltuieli_list, suma))
            if option5 == 3:
                continue

        if option == 6:
            if len(undo_list) > 1:
                cheltuieli_list = undo_step(undo_list)
                print("Lista a fost modificata!")
                del undo_list[-1]
            else:
                print("Lista cheltuielilor a ajuns la faza initiala!")
        if option == 7:
            return
        elif option > 7:
            print("Optiune invalida!")


start()
