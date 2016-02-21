# -*- coding: utf-8 -*-
def replaceValue(value):
    '''
    :param value: wartość z inputa wpisana przez użytkownika
    :return: liczbę o typie "float", albo 0 jeżeli zostanie wpisana niepoprawna wartość
    '''
    num = ''
    for item in value:
        if item.isalpha() or item == '+' or item == ' ':
            num += ''
        else:
            num += item
    try:
        return float(num.replace(',', '.'))
    except:
        return 0.0

def internet(value, total):
    '''
    :param value: kwota odliczenia np. za internet
    :param odliczenia: dochód po odliczeniu składek społecznych
    :return: kwota internetu do odliczenia
    '''
    #sprawdzenie czy użytkownik nie wpisał większej kwoty niż 760
    if value > 760:
        value = 760
    #sprawdzenie czy kwota za internet nie przekracza dochodu po odliczeniu składek społecznych
    if value > total:
        value = total
    return value

def kidsBenefit(kid, months):
    '''
    :param kid: od 3 dziecka przysługuje większa kwota odliczenia
    :param months: ilość miesięcy która przysługuje do odliczenia
    :return: kwotę odliczenia na jedno dziecko
    '''
    kid1and2 = 92.67
    kid3 = 166.67
    kid4plus = 225.00
    if kid <= 2:
        return round((kid1and2 * months), 2)
    elif kid == 3:
        return round((kid3 * months), 2)
    else:
        return round((kid4plus * months), 2)

