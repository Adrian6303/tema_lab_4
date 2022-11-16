from debug import debug_auto
from menu import *
from functions import *


def start():
    cheltuieli_list = []
    populate_list(cheltuieli_list)
    undo_list = []
    undo_list.append(copy_list(cheltuieli_list))
    debug_auto()
    while True:
        print_menu()
        print('Lista cheltuieli bloc: ', cheltuieli_list)
        option = input("Optiunea dumneavoastra este: ")
        """
        while validate_option(option) == False:
            print("Optiune invalida!")
            option = input("Optiunea dumneavoastra este: ")
        
        option = int(option)
        """
        if option == '1':
            print_opt1_menu()
            option1 = input("Optiunea dumneavoastra este: ")
            while validate_option(option1) == False:
                print("Optiune invalida!")
                option1 = input("Optiunea dumneavoastra este: ")
            option1 = int(option1)
            if option1 == 1:
                read_list(cheltuieli_list, undo_list)

            if option1 == 2:
                edit_list(cheltuieli_list, undo_list)
            if option1 == 3:
                continue

        elif option == '2':
            print_opt2_menu()
            option2 = input("Optiunea dumneavoastra este:")
            while validate_option(option2) == False:
                print("Optiune invalida!")
                option2 = input("Optiunea dumneavoastra este: ")
            option2 = int(option2)
            if option2 == 1:
                delete_cheltuieli_ap(cheltuieli_list, undo_list)
            if option2 == 2:
                delete_cheltuieli_consec(cheltuieli_list, undo_list)
            if option2 == 3:
                delete_cheltuieli_tip(cheltuieli_list, undo_list)
            if option2 == 4:
                continue
        elif option == '3':
            print_opt3_menu()
            option3 = input("Optiunea dumneavoastra este: ")
            while validate_option(option3) == False:
                print("Optiune invalida!")
                option3 = input("Optiunea dumneavoastra este: ")
            option3 = int(option3)
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
                ziua = int(input("Introduce ziua: "))
                while validate_ziua(ziua) == False:
                    print("Zi invalida!")
                    ziua = int(input("Introduce ziua: "))

                suma = int(input("Introduce suma: "))
                while validate_suma(suma) == False:
                    print("Suma invalida!")
                    suma = int(input("Introduce suma: "))
                print("Lista cheltuieli: ", tiparire_cheltuieli_zi(cheltuieli_list, ziua, suma))

            if option3 == 4:
                continue
        elif option == '4':
            print_opt4_menu()
            option4 = input("Optiunea dumneavoastra este:")
            while validate_option(option4) == False:
                print("Optiune invalida!")
                option4 = input("Optiunea dumneavoastra este: ")
            option4 = int(option4)
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
        elif option == '5':
            print_opt5_menu()
            option5 = input("Optiunea dumneavoastra este:")
            while validate_option(option5) == False:
                print("Optiune invalida!")
                option5 = input("Optiunea dumneavoastra este: ")
            option5 = int(option5)
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

        elif option == '6':
            if len(undo_list) > 1:
                cheltuieli_list = undo_step(undo_list)
                print("Lista a fost modificata!")
                del undo_list[-1]
            else:
                print("Lista cheltuielilor a ajuns la faza initiala!")

        elif option == '7':
            return
        else:
            i=0
            comanda = option.split(",")
            while i<len(comanda):
                actiune = comanda[i]
                actiune=actiune.split(" ")
                if actiune[0].lower() == "adauga":
                    data = actiune[1]
                    ac_adauga(data,cheltuieli_list,undo_list)
                elif actiune[0].lower() == "sterge":
                    data = actiune[1]
                    ac_sterge(data,cheltuieli_list,undo_list)
                elif actiune[0].lower() == "cauta":
                    suma = int(actiune[1])
                    while validate_suma(suma) == False:
                        print("Suma invalida!")
                        suma = int(input("Introduce suma: "))
                    print("Lista apartamente: ", tiparire_sume_mai_mari(cheltuieli_list, suma))
                elif actiune[0].lower() == "raport":
                    tip = str(actiune[1])
                    while validate_tip(tip) == False:
                        print("Tipul invalid!")
                        tip = str(input("Introduceti tipul: "))
                    print("Suma totala pentru ", tip, ": ", raport_sum_tip(cheltuieli_list, tip))
                elif actiune[0].lower() == "filtru":
                    tip = str(actiune[1])
                    while validate_tip(tip) == False:
                        print("Tipul invalid!")
                        tip = str(input("Introduceti tipul: "))
                    print("Lista filtrata: ", filter_tip(cheltuieli_list, tip))
                else:
                    print("Optiune invalida!")
                i+=1



start()
