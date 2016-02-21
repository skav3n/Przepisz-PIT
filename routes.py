# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
from functions import replaceValue, internet, kidsBenefit

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/panel/')
def panel():
    return render_template('panel.html')

@app.route('/pit37', methods=['GET', 'POST'])
def pit11():
    danePanel = ['sposob', 'pit11_ilosc', 'pit11_ilosc_m', 'kto_internet', 'internet', 'dzieci']
    for element in range(len(danePanel)):
        danePanel[element] = replaceValue(request.form[danePanel[element]])
    ktoDzieci = ['kto_dzieci_1', 'kto_dzieci_2', 'kto_dzieci_3', 'kto_dzieci_4']
    for element in range(len(ktoDzieci)):
        ktoDzieci[element] = replaceValue(request.form[ktoDzieci[element]])
    ileMiesiecy = ['ile_miesiecy_1', 'ile_miesiecy_2', 'ile_miesiecy_3', 'ile_miesiecy_4']
    for element in range(len(ileMiesiecy)):
        ileMiesiecy[element] = replaceValue(request.form[ileMiesiecy[element]])

    jedenProcent = ['jeden_procent', 'cel']
    for element in range(len(jedenProcent)):
        jedenProcent[element] = request.form[jedenProcent[element]]

    daneOsobowe = [['urzad5', 'identyfikator10', 'nazwisko11', 'imie12', 'data13', 'kraj14', 'wojewodztwo15',
                    'powiat16', 'gmina17', 'ulica18', 'dom19', 'lokal20', 'miejscowosc21', 'kod22', 'poczta23'],
                   ['urzad5m', 'identyfikator10m', 'nazwisko11m', 'imie12m', 'data13m', 'kraj14m', 'wojewodztwo15m',
                    'powiat16m', 'gmina17m', 'ulica18m', 'dom19m', 'lokal20m', 'miejscowosc21m', 'kod22m', 'poczta23m']]
    for element in range(len(daneOsobowe)):
        for item in range(len(daneOsobowe[element])):
            daneOsobowe[element][item] = request.form[daneOsobowe[element][item]]

    class Podatnik(object):

        # kiedy PIT-UZ i PIT-O
        pitO = False

        def __init__(self, kto):
            self.kto = kto
            # Przychody Koszty Zaliczki Skladki Dochody
            self.pkzds = []
            self.straty = []
            # przychód razem, koszt razem, zaliczka razem i dochód razem
            self.razemPKZD = {
                'przychod': 0,
                'koszt': 0,
                'dochod': 0,
                'zaplaconyPodatek': 0
            }
            self.spolecznaIzdrowotna = {
                'spoleczna': 0,
                'zdrowotna': 0
            }
            # odliczenia od dochodu[0:3] [0] doch.po odlicz.skł.społ. [1] doch.po odlicz.internetu [2] doch.po odliczeniach
            #self.odliczenia = []
            self.dochod = {
                'dochMinSpol103i104': 0,
                'dochMinInternet105i106': 0,
                'dochPoOdliczeniach111': 0
            }
            # Ulga na dzieci
            self.kwotaUlgiNaDzieci = 0

        def sectionC(self, names, number):
            '''
            :param names: lista nazw inputów z pitu11
            :param number: ilość pitów11 podatnika
            :return: lista 'pkzds': Przychody[0:12], Koszty[12:18], Zaliczki[18:28], Składki[28:30] i Dochody[30:35]
            :return: slownik: razemPKZD['przychod'], razemPKZD['koszt'], razemPKZD['dochod'], razemPKZD['zaplaconyPodatek']
            :return: lista 'straty' poniesionych przez podatnika [0:4]
            '''
            for element in range(len(names)):
            #Tworzy listę zależną od ilości formularzy zadeklarowanych przez użytkownika
                lista = []
                for item in range(int(number)):
                    lista.append(names[element] + 'p{}'.format(item))
                self.pkzds.append(lista)
            else:
                for element2 in range(len(self.pkzds)):
                #Przypisanie wartości użytkownika (domyślna i błędna wartość == 0)
                    for item2 in range(len(self.pkzds[element2])):
                        self.pkzds[element2][item2] = replaceValue(request.form[self.pkzds[element2][item2]])
                    self.pkzds[element2] = round(sum(self.pkzds[element2]), 2)
                else:
                #dodanie dochodu oraz straty (jeżeli występuje)
                    kwoty = []
                    kwoty.append(round(sum(self.pkzds[0:2]) - sum(self.pkzds[12:14]), 2))
                    kwoty.append(self.pkzds[2])
                    kwoty.append(round((self.pkzds[3] - self.pkzds[14]), 2))
                    kwoty.append(round((sum(self.pkzds[4:6]) - self.pkzds[15]), 2))
                    kwoty.append(round(sum(self.pkzds[6:12]) - sum(self.pkzds[16:18]), 2))
                    for element in range(len(kwoty)):
                        if kwoty[element] < 0:
                            self.pkzds.append(0.0)
                            self.straty.append(kwoty[element] * -1)
                        else:
                            self.pkzds.append(kwoty[element])
                            self.straty.append(0.0)
            #zsumowanie wszystkich przychodów, kosztów, zaliczek i dochodów
            self.razemPKZD['przychod'] = round(sum(self.pkzds[:12]), 2)
            self.razemPKZD['koszt'] = round(sum(self.pkzds[12:18]), 2)
            self.razemPKZD['zaplaconyPodatek'] = round(sum(self.pkzds[18:28]))
            self.razemPKZD['dochod'] = round((sum(self.pkzds[30:35]) - sum(self.straty)), 2)

            self.spolecznaIzdrowotna['spoleczna'] = round(self.pkzds[28], 2)
            self.spolecznaIzdrowotna['zdrowotna'] = round(self.pkzds[29], 2)

        def sectionD(self, kwotaInternet, kto_internet):
            '''
            :param kwotaInternet: suma wydana na internet przez podatnika w ciągu roku
            :param kto_internet: kto płacił za internet
            :return: tworzy slownik 'dochod'
            '''
            # dochód po odliczeniu składek społecznych
            self.dochod['dochMinSpol103i104'] = round((self.razemPKZD['dochod'] - self.spolecznaIzdrowotna['spoleczna']), 2)

            #odliczenie internetu i może później innych odliczeń
            if (self.kto == "Podatnik" and kto_internet == 1.0) or (self.kto == "Małżonek" and kto_internet == 2.0):

                self.dochod['dochMinInternet105i106'] = internet(kwotaInternet, self.dochod['dochMinSpol103i104'])
                if self.dochod['dochMinInternet105i106'] > 0:
                    Podatnik.pitO = True

            self.dochod['dochPoOdliczeniach111'] = round((self.dochod['dochMinSpol103i104'] - self.dochod['dochMinInternet105i106']), 2)

        def children(self, sposob, ileDzieci, ktoDziecko, ileMiesiecy):
            '''
            :param sposob: sposób rozliczenia "1" indywidualnie, "4" samotnie wych.dziecko
            :param ileDzieci: Ilość dzieci
            :param ktoDziecko: Kto odlicza ulgę na dziecko od podatku
            :param ileMiesiecy: Ilość miesięcy która przysługuje odliczeniu
            :return: kwota ulgi na dzieci
            '''
            for element in range(int(ileDzieci)):
                if self.kto == "Podatnik" and ktoDziecko[element] == 1.0:
                    self.kwotaUlgiNaDzieci += kidsBenefit((element+1), ileMiesiecy[element])
                if self.kto == "Małżonek" and ktoDziecko[element] == 2.0 and sposob >= 2 and sposob < 4:
                    self.kwotaUlgiNaDzieci += kidsBenefit((element+1), ileMiesiecy[element])
                Podatnik.pitO = True

    class Podatek(object):

        def __init__(self):
            self.podatek = {
                'podstawaOblPodatu112': 0,
                'obliczonyPodatek113': 0,
                'podatek115': 0,
                'odliczOdPod120': 0,
                'odliczOdPod121': 0,
                'podatekPoOdlicz122': 0,
                'podatekNalezny126': 0,
                'doZaplaty128': 0,
                'nadplata129': 0
            }
            self.pitUZ = False
            self.dodatkowyZwrot = {
                'roznica132': 0,
                'roznica133': 0,
                'przyslugujacaKwota134': 0,
                'lacznaKwotaZwrotu135': 0
            }

        def sectionE(self, sposob, dochodPoOdl111):
            if sposob == 1.0:
                self.podatek['podstawaOblPodatu112'] = round(dochodPoOdl111)
            else:
                self.podatek['podstawaOblPodatu112'] = round(dochodPoOdl111 / 2)

        def sectionF(self, sposob, dochodPoOdl111, zdrowotna, ulgaNaDzieci_P, ulgaNaDzieci_M):
            kwotaWolna = 556.02
            if self.podatek['podstawaOblPodatu112'] <= 85528:
                obliczonyPodatek = round((dochodPoOdl111 * 0.18 - kwotaWolna), 1)
                if obliczonyPodatek < 0:
                    obliczonyPodatek = 0
                if self.podatek['obliczonyPodatek113'] < 0:
                    self.podatek['obliczonyPodatek113'] = 0.0
                if sposob == 1.0:
                    self.podatek['obliczonyPodatek113'] = obliczonyPodatek
                else:
                    self.podatek['obliczonyPodatek113'] = obliczonyPodatek * 2
            else:
                obliczonyPodatek = round(((dochodPoOdl111 * 0.18 - kwotaWolna) + (dochodPoOdl111 - 85528) * 0.32), 2)
                if obliczonyPodatek < 0:
                    obliczonyPodatek = 0.0
                if sposob == 1.0:
                    self.podatek['obliczonyPodatek113'] = obliczonyPodatek
                else:
                    self.podatek['obliczonyPodatek113'] = obliczonyPodatek * 2

            self.podatek['podatek115'] = self.podatek['obliczonyPodatek113']

            kwotaMaxUlgi = round((self.podatek['podatek115'] - zdrowotna), 2)
            if ulgaNaDzieci_P > 0 and ulgaNaDzieci_P > kwotaMaxUlgi:
                self.podatek['odliczOdPod120'] = kwotaMaxUlgi
            else:
                self.podatek['odliczOdPod120'] = ulgaNaDzieci_P
                kwotaMaxUlgi -= ulgaNaDzieci_P
            if ulgaNaDzieci_M > 0 and ulgaNaDzieci_M > kwotaMaxUlgi:
                self.podatek['odliczOdPod121'] = kwotaMaxUlgi
            else:
                self.podatek['odliczOdPod121'] = ulgaNaDzieci_M
                kwotaMaxUlgi -= ulgaNaDzieci_M

            self.podatek['podatekPoOdlicz122'] = round((self.podatek['podatek115'] - zdrowotna -
                                                        self.podatek['odliczOdPod120'] - self.podatek['odliczOdPod121']), 2)

        def sectionG(self, podatekZaplacony):
            self.podatek['podatekNalezny126'] = self.podatek['podatekPoOdlicz122']

            if self.podatek['podatekNalezny126'] - podatekZaplacony < 0:
                self.podatek['doZaplaty128'] = 0
            else:
                self.podatek['doZaplaty128'] = round(self.podatek['podatekNalezny126'] - podatekZaplacony)

            if podatekZaplacony - self.podatek['podatekNalezny126'] < 0:
                self.podatek['nadplata129'] = 0
            else:
                self.podatek['nadplata129'] = round(podatekZaplacony - self.podatek['podatekNalezny126'])

        def sectionH(self, spoleczne, zdrowotne, ulgaNaDzieci_P, ulgaNaDzieci_M):
            self.dodatkowyZwrot['roznica132'] = round((ulgaNaDzieci_P - self.podatek['odliczOdPod120']), 2)
            self.dodatkowyZwrot['roznica133'] = round((ulgaNaDzieci_M - self.podatek['odliczOdPod121']), 2)

            if self.dodatkowyZwrot['roznica132'] > 0 or self.dodatkowyZwrot['roznica133'] > 0:
                self.pitUZ = True

            self.dodatkowyZwrot['przyslugujacaKwota134'] = round((self.dodatkowyZwrot['roznica132'] + self.dodatkowyZwrot['roznica133']), 2)

            if self.dodatkowyZwrot['przyslugujacaKwota134'] > (spoleczne + zdrowotne):
                self.dodatkowyZwrot['przyslugujacaKwota134'] = spoleczne + zdrowotne

            self.dodatkowyZwrot['lacznaKwotaZwrotu135'] = round(self.podatek['nadplata129'] + self.dodatkowyZwrot['przyslugujacaKwota134'])


    #przychody 0-11 #koszty 12-17 #zaliczki 18-27 #skladki 28-29 (28 społeczna, 29 zdrowotna)
    listaPodatnik = ['przychod25', 'przychod30', 'przychod35', 'przychod45', 'przychod53', 'przychod56',
                     'przychod32', 'przychod39', 'przychod42', 'przychod49', 'przychod58', 'przychod62',

                     'koszt26', 'koszt31', 'koszt46', 'koszt57', 'koszt50', 'koszt59',

                     'zaliczka29', 'zaliczka38', 'zaliczka48', 'zaliczka55', 'zaliczka34', 'zaliczka41',
                     'zaliczka44', 'zaliczka52', 'zaliczka61', 'zaliczka65',

                     'skladki66', 'zdrowotna68']

    listaMalzonek = []
    for element in listaPodatnik:
        listaMalzonek.append(element+'m')

    podatnik = Podatnik("Podatnik")
    malzonek = Podatnik("Małżonek")
    #danePanel[1] - ilosc pitow podatnik, danePanel[2] - ilosc pitow malzonek
    podatnik.sectionC(listaPodatnik, danePanel[1])
    malzonek.sectionC(listaMalzonek, danePanel[2])
    #danePanel[3] - kto internet, danePanel[4] - internet
    podatnik.sectionD(danePanel[4], danePanel[3])
    malzonek.sectionD(danePanel[4], danePanel[3])


    podatnik.children(danePanel[0], danePanel[5], ktoDzieci, ileMiesiecy)
    malzonek.children(danePanel[0], danePanel[5], ktoDzieci, ileMiesiecy)

    podatek = Podatek()
    podatek.sectionE(danePanel[0], (podatnik.dochod['dochPoOdliczeniach111'] + malzonek.dochod['dochPoOdliczeniach111']))
    podatek.sectionF(danePanel[0], (podatnik.dochod['dochPoOdliczeniach111'] + malzonek.dochod['dochPoOdliczeniach111']),
                     (podatnik.spolecznaIzdrowotna['zdrowotna'] + malzonek.spolecznaIzdrowotna['zdrowotna']),
                     podatnik.kwotaUlgiNaDzieci, malzonek.kwotaUlgiNaDzieci)
    podatek.sectionG((podatnik.razemPKZD['zaplaconyPodatek'] + malzonek.razemPKZD['zaplaconyPodatek']))
    podatek.sectionH((podatnik.spolecznaIzdrowotna['spoleczna'] + malzonek.spolecznaIzdrowotna['spoleczna']),
                     (podatnik.spolecznaIzdrowotna['zdrowotna'] + malzonek.spolecznaIzdrowotna['zdrowotna']),
                     podatnik.kwotaUlgiNaDzieci, malzonek.kwotaUlgiNaDzieci)

    return render_template('pit37.html', danePanel=danePanel, jedenProcent=jedenProcent, daneOsobowe=daneOsobowe,
                           ktoDzieci=ktoDzieci, ileMiesiecy=ileMiesiecy,
                           pkzds_P=podatnik.pkzds, straty_P=podatnik.straty, razemPKZD_P=podatnik.razemPKZD,
                           pkzds_M=malzonek.pkzds, straty_M=malzonek.straty, razemPKZD_M=malzonek.razemPKZD,
                           odliczenia_P=podatnik.dochod, odliczenia_M=malzonek.dochod,
                           obliczaniePodatku=podatek.podatek, dodatkowyZwrot=podatek.dodatkowyZwrot,
                           pitUZ=podatek.pitUZ, pitO=Podatnik.pitO)

if __name__ == '__main__':
    app.run(debug=True)