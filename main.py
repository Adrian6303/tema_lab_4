from debug import debug_auto
from menu import *
from functions import *


def start():
    current_list = []
    populate_list(current_list)
    debug_auto()
    while True:
        print_menu()
        print('Lista cheltuieli bloc: ', current_list)
        option = int(input("Optiunea dumneavoastra este: "))
        if option == 1:
            print("1. Adaugă cheltuială pentru un apartament")
            print("2. Modifică cheltuială")
            print("3. Inapoi")
            option1 = int(input("Optiunea dumneavoastra este: "))
            if option1 == 1:
                read_list(current_list)

            if option1 == 2:
                edit_list(current_list)
            if option1 == 3:
                continue

        if option == 2:
            print("1. Șterge toate cheltuielile de la un apartament")
            print("2. Șterge cheltuielile de la apartamente consecutive")
            print("3. Șterge cheltuielile de un anumit tip de la toate apartamentele")
            print("4. Inapoi")
            option2 = int(input("Optiunea dumneavoastra este:"))
            if option2 == 1:
                delete_cheltuieli_ap(current_list)
            if option2 == 2:
                delete_cheltuieli_consec(current_list)
            if option2 == 3:
                delete_cheltuieli_tip(current_list)
            if option2 == 4:
                continue
        if option == 3:
            print("1. Tipărește toate apartamentele care au cheltuieli mai mari decât o sumă dată")
            print("2. Tipărește cheltuielile de un anumit tip de la toate apartamentele")
            print("3. Tipărește toate cheltuielile efectuate înainte de o zi și mai mari decât o sumă")
            print("4. Inapoi")
            option3 = int(input("Optiunea dumneavoastra este:"))
            if option3 == 1:
                suma = int(input("Introduce suma: "))
                print("Lista apartamente: ", tiparire_sume_mai_mari(current_list, suma))
            if option3 == 2:
                tip=str(input("Introduceti tipul: "))
                print("Lista cheltuieli: ",tiparire_cheltuieeli_tip(current_list, tip))
            if option3 == 3:
                print("nu e gata")
            if option3 == 4:
                continue
        if option == 4:
            print("1. Tipărește suma totală pentru un tip de cheltuială")
            print("2. Tipărește toate apartamentele sortate după un tip de cheltuială")
            print("3. Tipărește totalul de cheltuieli pentru un apartament dat")
            print("4. Inapoi")
            option4 = int(input("Optiunea dumneavoastra este:"))
            if option4 == 1:
                tip = str(input("Introduceti tipul: "))
                print("Suma totala pentru ",tip,": ",raport_sum_tip(current_list, tip))
            if option4 == 2:
                print("nu e gata")
            if option4 == 3:
                print("nu e gata")
            if option4 == 4:
                continue
        if option == 5:
            print("1. Elimină toate cheltuielile de un anumit tip")
            print("2. Elimină toate cheltuielile de un anumit tip")
            print("3. Inapoi")
            option5 = int(input("Optiunea dumneavoastra este:"))
            if option5 == 1:
                print("nu e gata")
            if option5 == 2:
                print("nu e gata")
            if option5 == 3:
                continue

        if option == 6:
            print("nu e gata")
        if option == 7:
            return
        elif option>7:
            print("Optiune invalida!")


start()
