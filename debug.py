from functions import *


def debug_auto():

    assert validate_ap(-1) == False
    assert validate_ap(1) == True

    assert validate_tip('Ceva') == False
    assert validate_tip('Apa') == True

    assert validate_suma(-200) == False
    assert validate_suma(200) == True

    assert validate_ziua(10) == True
    assert validate_ziua(-10) == False
    assert validate_ziua(32) == False

    assert validate_option("-10") == False
    assert validate_option("5") == True
    assert validate_option("12b5") == False
    assert validate_option("-12;h6") == False


    assert tiparire_sume_mai_mari([{'ap': 1, 'tip': 'Apa', 'suma': 200, 'ziua': 5}, {'ap': 1, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}, {'ap': 2, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}, {'ap': 4, 'tip': 'Canal', 'suma': 100, 'ziua': 10}, {'ap': 69, 'tip': 'Altele', 'suma': 250, 'ziua': 17}], 400) == [1, 2]
    assert tiparire_sume_mai_mari([{'ap': 1, 'tip': 'Apa', 'suma': 200, 'ziua': 5}, {'ap': 1, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}], 1000) == []
    assert tiparire_sume_mai_mari([{'ap': 1, 'tip': 'Apa', 'suma': 200, 'ziua': 5}, {'ap': 1, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}, {'ap': 2, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}, {'ap': 4, 'tip': 'Canal', 'suma': 100, 'ziua': 10}], 100) == [1, 2, 4]

    assert tiparire_cheltuieeli_tip([{'ap': 1, 'tip': 'Apa', 'suma': 200, 'ziua': 5}, {'ap': 1, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}, {'ap': 2, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}], "Gaz") == ['Apartamentul 1 suma 300', 'Apartamentul 2 suma 500']
    assert tiparire_cheltuieeli_tip([{'ap': 1, 'tip': 'Apa', 'suma': 200, 'ziua': 5}, {'ap': 1, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}, {'ap': 2, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}, {'ap': 4, 'tip': 'Canal', 'suma': 100, 'ziua': 10}, {'ap': 69, 'tip': 'Altele', 'suma': 250, 'ziua': 17}], "Incalzire") == []
    assert tiparire_cheltuieeli_tip([{'ap': 1, 'tip': 'Canal', 'suma': 200, 'ziua': 5}, {'ap': 2, 'tip': 'Canal', 'suma': 300, 'ziua': 22}, {'ap': 3, 'tip': 'Canal', 'suma': 500, 'ziua': 15}, {'ap': 4, 'tip': 'Canal', 'suma': 100, 'ziua': 10}], "Canal") == ['Apartamentul 1 suma 200', 'Apartamentul 2 suma 300', 'Apartamentul 3 suma 500', 'Apartamentul 4 suma 100']

    assert tiparire_cheltuieli_zi([{'ap': 1, 'tip': 'Apa', 'suma': 200, 'ziua': 5}, {'ap': 1, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}, {'ap': 2, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}],20, 100 ) == ["Apartamentul 1 suma 200", "Apartamentul 2 suma 500"]
    assert tiparire_cheltuieli_zi([{'ap': 1, 'tip': 'Apa', 'suma': 200, 'ziua': 5}, {'ap': 1, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}, {'ap': 2, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}],1,600) == []
    assert tiparire_cheltuieli_zi([{'ap': 1, 'tip': 'Apa', 'suma': 200, 'ziua': 5}, {'ap': 2, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}, {'ap': 3, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}],25,150) == ["Apartamentul 1 suma 200","Apartamentul 2 suma 300", "Apartamentul 3 suma 500"]

    assert raport_sum_tip([{'ap': 1, 'tip': 'Apa', 'suma': 200, 'ziua': 5}, {'ap': 1, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}, {'ap': 2, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}, {'ap': 4, 'tip': 'Canal', 'suma': 100, 'ziua': 10}],"Apa") == 200
    assert raport_sum_tip([{'ap': 1, 'tip': 'Apa', 'suma': 200, 'ziua': 5}, {'ap': 1, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}, {'ap': 2, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}, {'ap': 4, 'tip': 'Canal', 'suma': 100, 'ziua': 10}], "Gaz") == 800
    assert raport_sum_tip([{'ap': 1, 'tip': 'Apa', 'suma': 200, 'ziua': 5}, {'ap': 1, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}, {'ap': 2, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}, {'ap': 4, 'tip': 'Canal', 'suma': 100, 'ziua': 10}], "Incalzire") == 0

    assert raport_ap_sort_tip([{'ap': 1, 'tip': 'Apa', 'suma': 200, 'ziua': 5}, {'ap': 1, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}, {'ap': 2, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}, {'ap': 4, 'tip': 'Canal', 'suma': 100, 'ziua': 10}], "Gaz") == [1, 2]
    assert raport_ap_sort_tip([{'ap': 1, 'tip': 'Apa', 'suma': 200, 'ziua': 5}, {'ap': 1, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}, {'ap': 2, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}, {'ap': 4, 'tip': 'Canal', 'suma': 100, 'ziua': 10}], "Canal") == [4]
    assert raport_ap_sort_tip([{'ap': 1, 'tip': 'Apa', 'suma': 200, 'ziua': 5}, {'ap': 1, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}, {'ap': 2, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}, {'ap': 4, 'tip': 'Canal', 'suma': 100, 'ziua': 10}], "Incalzire") == []

    assert raport_total_ap([{'ap': 1, 'tip': 'Apa', 'suma': 200, 'ziua': 5}, {'ap': 1, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}, {'ap': 2, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}, {'ap': 4, 'tip': 'Canal', 'suma': 100, 'ziua': 10}], 1) == 500
    assert raport_total_ap([{'ap': 1, 'tip': 'Apa', 'suma': 200, 'ziua': 5}, {'ap': 1, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}, {'ap': 2, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}, {'ap': 4, 'tip': 'Canal', 'suma': 100, 'ziua': 10}], 4) == 100
    assert raport_total_ap([{'ap': 1, 'tip': 'Apa', 'suma': 200, 'ziua': 5}, {'ap': 1, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}, {'ap': 2, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}, {'ap': 4, 'tip': 'Canal', 'suma': 100, 'ziua': 10}], 10) == 0

    assert filter_tip([{'ap': 1, 'tip': 'Apa', 'suma': 200, 'ziua': 5}, {'ap': 1, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}, {'ap': 2, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}, {'ap': 4, 'tip': 'Canal', 'suma': 100, 'ziua': 10}], "Apa") == [{'ap': 1, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}, {'ap': 2, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}, {'ap': 4, 'tip': 'Canal', 'suma': 100, 'ziua': 10}]
    assert filter_tip([{'ap': 1, 'tip': 'Gaz', 'suma': 200, 'ziua': 5}, {'ap': 2, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}, {'ap': 3, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}], "Gaz") == []
    assert filter_tip([{'ap': 1, 'tip': 'Apa', 'suma': 200, 'ziua': 5}, {'ap': 2, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}],"Incalzire") == [{'ap': 1, 'tip': 'Apa', 'suma': 200, 'ziua': 5}, {'ap': 2, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}]

    assert filter_suma([{'ap': 1, 'tip': 'Gaz', 'suma': 200, 'ziua': 5}, {'ap': 2, 'tip': 'Gaz', 'suma': 350, 'ziua': 22}, {'ap': 3, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}],300) == [{'ap': 2, 'tip': 'Gaz', 'suma': 350, 'ziua': 22}, {'ap': 3, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}]
    assert filter_suma([{'ap': 1, 'tip': 'Gaz', 'suma': 200, 'ziua': 5}, {'ap': 2, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}, {'ap': 3, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}], 100) == [{'ap': 1, 'tip': 'Gaz', 'suma': 200, 'ziua': 5}, {'ap': 2, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}, {'ap': 3, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}]
    assert filter_suma([{'ap': 1, 'tip': 'Gaz', 'suma': 200, 'ziua': 5}, {'ap': 2, 'tip': 'Gaz', 'suma': 300, 'ziua': 22}, {'ap': 3, 'tip': 'Gaz', 'suma': 500, 'ziua': 15}], 600) == []
