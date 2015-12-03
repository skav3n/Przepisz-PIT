# -*- coding: utf-8 -*-
def replace(value):
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
        return 0

def odliczeniaOdPrzychodu(kwota, odliczenia):
    '''
    :param kwota: kwota odliczenia np. za internet
    :param odliczenia: dochód po odliczeniu składek społecznych
    :return: kwota internetu do odliczenia
    '''
    #sprawdzenie czy użytkownik nie wpisał większej kwoty niż 760
    if kwota > 760:
        kwota = 760
    #sprawdzenie czy kwota za internet nie przekracza dochodu po odliczeniu składek społecznych
    if kwota > odliczenia:
        kwota = odliczenia
    return kwota

def liczPodatek(sposob, dochod, zaliczki, zdrowotna, ulgiNaDzieci=0):
    '''
    :param sposob: sposób rozliczenia:
        "1.0" indywidualnie
        "2.0" wspólnie z małżonkiem
        "3.0" wspólnie ze zmarłym małżonkiem
        "4.0" osoba samotnie wychowująca dziecko
    :param dochod: dochód podatnika po odjęciu odliczeń
    :param zaliczki: zaliczki odprowadzone przez podatnika
    :param ulgiNaDzieci: kwota zmniejszająca podatek
    :return: listę różnych podatków
    '''
    kwotaWolna = 556.02
    obliczaniePodatku = []
    #Podstawa obliczania podatku [0]
    if sposob == 1.0:
        obliczaniePodatku.append(round(dochod))
    else:
        obliczaniePodatku.append(round((dochod / 2), 2))
    #obliczanie podatku [1]
    if obliczaniePodatku[0] <= 85528:
        podatek = round((obliczaniePodatku[0] * 0.18 - kwotaWolna),2)
        if podatek < 0:
            podatek = 0.0
        if sposob == 1.0:
            obliczaniePodatku.append(podatek)
        else:
            obliczaniePodatku.append(podatek * 2)
    else:
        podatek = round(((obliczaniePodatku[0] * 0.18 - kwotaWolna) + (obliczaniePodatku[0] - 85528) * 0.32), 2)
        if podatek < 0:
            podatek = 0.0
        if sposob == 1.0:
            obliczaniePodatku.append(podatek)
        else:
            obliczaniePodatku.append(podatek * 2)
    #doliczenia do podatku [2]
    doliczeniaDoPodatku = 0.0
    obliczaniePodatku.append(doliczeniaDoPodatku)
    #"surowy" Podatek [3]
    obliczaniePodatku.append(obliczaniePodatku[1] + obliczaniePodatku[2])
    #Podatek minus składki zdrowotne i ulgi na dzieci [4]
    obliczaniePodatku.append(round((obliczaniePodatku[3] - zdrowotna - ulgiNaDzieci), 2))
    #Podatek należny [5]
    obliczaniePodatku.append(round(obliczaniePodatku[4]))
    #Podatek DO ZAPŁATY [6]
    if (obliczaniePodatku[5] - zaliczki) > 0:
        obliczaniePodatku.append(round(obliczaniePodatku[5] - zaliczki))
    else:
        obliczaniePodatku.append(0.0)
    #Podatek NADPŁATA [7]
    if (zaliczki - obliczaniePodatku[5]) > 0:
        obliczaniePodatku.append(round(zaliczki - obliczaniePodatku[5]))
    else:
        obliczaniePodatku.append(0.0)
    return obliczaniePodatku

def liczUlgeNaDziecko(ktoreDzecko, ileMiesiecy):
    '''
    :param ktoreDzecko: od 3 dziecka przysługuje większa kwota odliczenia
    :param ileMiesiecy: ilość miesięcy która przysługuje do odliczenia
    :return: kwotę odliczenia na jedno dziecko
    '''
    kwotaNaDziecko1i2 = 92.67
    kwotaNaDziecko3i4 = 166.67
    if ktoreDzecko <= 2:
        return round((kwotaNaDziecko1i2 * ileMiesiecy), 2)
    else:
        return round((kwotaNaDziecko3i4 * ileMiesiecy), 2)

