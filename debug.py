from functions import *


def debug_auto():


    assert validate_ap(-1) == False
    assert validate_ap(100) == True
    assert validate_tip("Ceva") == False
    assert validate_tip("Canal") == True
    assert validate_suma(-200) == False
    assert validate_suma(200) == True

    assert tiparire_sume_mai_mari([{'ap': 1, 'tip': 'Apa', 'suma': 200}, {'ap': 1, 'tip': 'Gaz', 'suma': 300}, {'ap': 2, 'tip': 'Gaz', 'suma': 500}, {'ap': 4, 'tip': 'Canal', 'suma': 100}, {'ap': 69, 'tip': 'Altele', 'suma': 250}], 300) == [1, 2]
    assert tiparire_sume_mai_mari([{'ap': 1, 'tip': 'Apa', 'suma': 200}, {'ap': 1, 'tip': 'Gaz', 'suma': 300}, {'ap': 2, 'tip': 'Gaz', 'suma': 500}, {'ap': 4, 'tip': 'Canal', 'suma': 100}, {'ap': 69, 'tip': 'Altele', 'suma': 250}], 1000) == []
    assert tiparire_sume_mai_mari([{'ap': 1, 'tip': 'Apa', 'suma': 200}, {'ap': 1, 'tip': 'Gaz', 'suma': 300}, {'ap': 2, 'tip': 'Gaz', 'suma': 500}, {'ap': 4, 'tip': 'Canal', 'suma': 100}, {'ap': 69, 'tip': 'Altele', 'suma': 250}], 100) == [1, 2, 4, 69]
"""
    assert tiparire_cheltuieeli_tip(['1.Apa=200', '1.Gaz=300', '2.Gaz=500', '4.Canal=100'], "Gaz") == ['Apartamentul 1 suma 300', 'Apartamentul 2 suma 500']
    assert tiparire_cheltuieeli_tip(['1.Apa=200', '1.Gaz=300', '2.Gaz=500', '4.Canal=100'], "Incalzire") == []
    assert tiparire_cheltuieeli_tip(['1.Canal=200', '2.Canal=300', '3.Canal=500', '4.Canal=100'], "Canal") == ['Apartamentul 1 suma 200', 'Apartamentul 2 suma 300', 'Apartamentul 3 suma 500', 'Apartamentul 4 suma 100']

    assert raport_sum_tip(['1.Apa=200', '1.Gaz=300', '2.Gaz=500', '4.Canal=100', '1.Canal=100', '69.Apa=250', '250.Apa=250'],"Apa") == 700
    assert raport_sum_tip(['1.Apa=200', '1.Gaz=300', '2.Gaz=500', '4.Canal=100', '1.Canal=100', '69.Apa=250', '250.Apa=250'], "Gaz") == 800
    assert raport_sum_tip(['1.Apa=200', '1.Gaz=300', '2.Gaz=500', '4.Canal=100', '1.Canal=100', '69.Apa=250', '250.Apa=250'], "Incalzire") == 0

    assert raport_ap_sort_tip(['1.Apa=200', '1.Gaz=300', '2.Gaz=500'], "Gaz") == [1, 2]
    assert raport_ap_sort_tip(['2.Gaz=500', '4.Canal=100', '1.Canal=100', '69.Apa=250'], "Canal") == [1, 4]
    assert raport_ap_sort_tip(['2.Gaz=500', '4.Canal=100', '1.Canal=100'], "Apa") == []

    assert raport_total_ap(['1.Apa=200', '1.Gaz=300', '2.Gaz=500', '4.Canal=100', '1.Canal=100'], "1") == 600
    assert raport_total_ap(['1.Apa=200', '1.Gaz=300', '2.Gaz=500', '4.Canal=100', '1.Canal=100'], "2") == 500
    assert raport_total_ap(['1.Apa=200', '1.Gaz=300', '2.Gaz=500', '4.Canal=100', '1.Canal=100'], "10") == 0

    assert filter_tip(['1.Apa=200', '1.Gaz=300', '2.Gaz=500', '4.Canal=100', '1.Canal=100', '69.Apa=250', '250.Apa=250'], "Apa") == ['1.Gaz=300', '2.Gaz=500', '4.Canal=100', '1.Canal=100']
    assert filter_tip(['1.Gaz=300', '2.Gaz=500', '4.Gaz=100'], "Gaz") == []
    assert filter_tip(['1.Apa=200', '1.Gaz=300', '2.Gaz=500', '4.Canal=100'],"Incalzire") == ['1.Apa=200', '1.Gaz=300', '2.Gaz=500', '4.Canal=100']

    assert filter_suma(['1.Apa=200', '1.Gaz=300', '2.Gaz=500', '4.Canal=100', '1.Canal=100', '69.Apa=250'],300) == ['1.Gaz=300', '2.Gaz=500']
    assert filter_suma(['1.Apa=200', '2.Gaz=500', '4.Canal=100', '69.Apa=250'], 100) == ['1.Apa=200', '2.Gaz=500', '4.Canal=100', '69.Apa=250']
    assert filter_suma(['1.Apa=200', '2.Gaz=500', '4.Canal=100', '69.Apa=250'], 600) == []
    """