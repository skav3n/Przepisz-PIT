# -*- coding: utf-8 -*-
from flask import Flask, request, render_template
from functions import replace, OdliczeniaOdPrzychodu, liczPodatek, liczUlgeNaDziecko

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
        danePanel[element] = replace(request.form[danePanel[element]])
    ktoDzieci = ['kto_dzieci_1', 'kto_dzieci_2', 'kto_dzieci_3', 'kto_dzieci_4']
    for element in range(len(ktoDzieci)):
        ktoDzieci[element] = replace(request.form[ktoDzieci[element]])
    ileMiesiecy = ['ile_miesiecy_1', 'ile_miesiecy_2', 'ile_miesiecy_3', 'ile_miesiecy_4']
    for element in range(len(ileMiesiecy)):
        ileMiesiecy[element] = replace(request.form[ileMiesiecy[element]])

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
        pitUZ = False
        przyslugujacaKwata = 0

        def __init__(self, kto):
            self.kto = kto
            # Przychody Koszty Zaliczki Skladki Dochody
            self.pkzds = []
            self.straty = []
            # przychód razem, koszt razem, zaliczka razem i dochód razem
            self.razemPKZD = []
            # odliczenia od dochodu[0:4] [0] doch.po odlicz.skł.społ. [1] doch.po odlicz.internetu [2] doch.po odliczeniach
            self.odliczenia = []
            # Ulga na dzieci
            self.kwotaUlgi = 0
            self.kwotaUlgiNaDzieci = 0

        def dodajWartosci(self, names, number):
            '''
            :param names: lista nazw inputów z pitu11
            :param number: ilość pitów11 podatnika
            :return: lista w kolejności Przychody[0:12], Koszty[12:18], Zaliczki[18:28], Składki[28:30] i Dochody[30:35]
            :return: lista zsumowanych Przychodów[0], Kosztów[1], Zaliczek[2] i Dochodów[3]
            :return: lista poniesionych strat przez podatnika [0:5]
            '''
            for element in range(len(names)):
            #Tworzy listę zależną od ilości formularzy zadeklarowanych przez żytkownika
                lista = []
                for item in range(int(number)):
                    lista.append(names[element] + 'p{}'.format(item))
                self.pkzds.append(lista)
            else:
                for element2 in range(len(self.pkzds)):
                #Przypisanie wartości użytkownika, domyślna i błędna wartość == 0
                    for item2 in range(len(self.pkzds[element2])):
                        self.pkzds[element2][item2] = replace(request.form[self.pkzds[element2][item2]])
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
            self.razemPKZD.append(round(sum(self.pkzds[:12]), 2))
            self.razemPKZD.append(round(sum(self.pkzds[12:18]), 2))
            self.razemPKZD.append(round(sum(self.pkzds[18:28])))
            self.razemPKZD.append(round((sum(self.pkzds[30:35]) - sum(self.straty)), 2))

        def odliczeniaOdDochodu(self, kwotaInternet, kto_internet):
            '''
            :param kwotaInternet: suma wydana na internet przez podatnika w ciągu roku
            :param kto_internet: kto płacił za internet
            :return: tworzy listę z trzema wartościami:
            [0] dochód po odlicz.skł.społ.
            [1] doch po odliczeniu internetu
            [2] dochód po wszystkich odliczeniach
            '''
            #[0] dochód po odliczeniu składek społecznych
            dochodPoOdliczeniuSkladek = round((self.razemPKZD[3] - self.pkzds[28]), 2)
            self.odliczenia.append(dochodPoOdliczeniuSkladek)
            #odliczenie internetu i może później innych odliczeń
            #[1] doch po odliczeniu internetu
            if self.kto == "Podatnik" and kto_internet == 1.0:
                self.odliczenia.append(OdliczeniaOdPrzychodu(kwotaInternet, dochodPoOdliczeniuSkladek))
                Podatnik.pitO = True
            elif self.kto == "Małżonek" and kto_internet == 2.0:
                self.odliczenia.append(OdliczeniaOdPrzychodu(kwotaInternet, dochodPoOdliczeniuSkladek))
                Podatnik.pitO = True
            else:
                self.odliczenia.append(0.0)
            #[2] dochód po wszystkich odliczeniach
            dochodPoOdliczeniach = round((self.odliczenia[0] - self.odliczenia[1]), 2)
            self.odliczenia.append(dochodPoOdliczeniach)

        def odliczeniaOdPodatku(self, sposob, ileDzieci, ktoDziecko, ileMiesiecy):
            '''
            :param sposob: sposób rozliczenia "1" indywidualnie, "4" samotnie wych.dziecko
            :param ileDzieci: Ilość dzieci
            :param ktoDziecko: Kto odlicza ulgę na dziecko od podatku
            :param ileMiesiecy: Ilość miesięcy która przysługuje odliczeniu
            :return: kwota ulgi na dzieci
            '''
            # ulga na dzieci
            for element in range(int(ileDzieci)):
                if self.kto == "Podatnik" and ktoDziecko[element] == 1.0:
                    self.kwotaUlgiNaDzieci += liczUlgeNaDziecko((element+1), ileMiesiecy[element])
                    self.kwotaUlgi += liczUlgeNaDziecko((element+1), ileMiesiecy[element])
                if self.kto == "Małżonek" and ktoDziecko[element] == 2.0 and sposob >= 2 and sposob < 4:
                    self.kwotaUlgiNaDzieci += liczUlgeNaDziecko((element+1), ileMiesiecy[element])
                    self.kwotaUlgi += liczUlgeNaDziecko((element+1), ileMiesiecy[element])
                Podatnik.pitO = True
            # sprawdzanie możliwość odliczenia ulgi na dzieci
            if self.kto == "Podatnik":
                if self.kwotaUlgiNaDzieci > (obliczaniePodatku[3] - self.pkzds[29] - malzonek.pkzds[29]):
                    self.kwotaUlgiNaDzieci = obliczaniePodatku[3]
                    Podatnik.pitUZ = True
                    Podatnik.przyslugujacaKwata += round((self.kwotaUlgi - self.kwotaUlgiNaDzieci), 2)
                    if Podatnik.przyslugujacaKwata > self.pkzds[28] + self.pkzds[29]:
                        Podatnik.przyslugujacaKwata = round((self.pkzds[28] + self.pkzds[29]), 2)
            else:
                if (self.kwotaUlgiNaDzieci + podatnik.kwotaUlgiNaDzieci) > (obliczaniePodatku[3] - self.pkzds[29] - podatnik.pkzds[29]):
                    self.kwotaUlgiNaDzieci = round((obliczaniePodatku[3] - podatnik.kwotaUlgiNaDzieci), 2)
                    Podatnik.pitUZ = True
                    Podatnik.przyslugujacaKwata += round((self.kwotaUlgi - self.kwotaUlgiNaDzieci), 2)
                    if Podatnik.przyslugujacaKwata > self.pkzds[28] + self.pkzds[29]:
                        Podatnik.przyslugujacaKwata = round((self.pkzds[28] + self.pkzds[29]), 2)


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

    podatnik.dodajWartosci(listaPodatnik, danePanel[1])
    malzonek.dodajWartosci(listaMalzonek, danePanel[2])

    podatnik.odliczeniaOdDochodu(danePanel[4], danePanel[3])
    malzonek.odliczeniaOdDochodu(danePanel[4], danePanel[3])

    # wspólne odliczenia od podatku
    # [0] podstawa podatku, [1] obliczenie podatku, [2] doliczenia do podatku, [3] "surowy" podatek
    obliczaniePodatku = liczPodatek(danePanel[0], (podatnik.odliczenia[2] + malzonek.odliczenia[2]),
                                    (podatnik.razemPKZD[2] + malzonek.razemPKZD[2]), ulgiNaDzieci=0)

    podatnik.odliczeniaOdPodatku(danePanel[0], danePanel[5], ktoDzieci, ileMiesiecy)
    malzonek.odliczeniaOdPodatku(danePanel[0], danePanel[5], ktoDzieci, ileMiesiecy)

    # wspólne odliczenia od podatku
    # [4] podatek minus ulgi na dzieci, [5] podatek należny, [6] podatek DO ZAPŁATY, [7] NADPŁATA
    obliczaniePodatku = liczPodatek(danePanel[0], (podatnik.odliczenia[2] + malzonek.odliczenia[2]),
                                    (podatnik.razemPKZD[2] + malzonek.razemPKZD[2]),
                                    (podatnik.kwotaUlgiNaDzieci + malzonek.kwotaUlgiNaDzieci))

    return render_template('pit37.html', danePanel=danePanel, jedenProcent=jedenProcent, daneOsobowe=daneOsobowe,
                           ktoDzieci=ktoDzieci, ileMiesiecy=ileMiesiecy,
                           pkzds_P=podatnik.pkzds, straty_P=podatnik.straty, razemPKZD_P=podatnik.razemPKZD,
                           pkzds_M=malzonek.pkzds, straty_M=malzonek.straty, razemPKZD_M=malzonek.razemPKZD,
                           odliczenia_P=podatnik.odliczenia, odliczenia_M=malzonek.odliczenia,
                           obliczaniePodatku=obliczaniePodatku,
                           kwotaUlgiNaDzieci_P=podatnik.kwotaUlgiNaDzieci, kwotaUlgiNaDzieci_M=malzonek.kwotaUlgiNaDzieci,
                           kwotaUlgi_P=podatnik.kwotaUlgi, kwotaUlgi_M=malzonek.kwotaUlgi,
                           przyslugajacaKwota=Podatnik.przyslugujacaKwata,
                           pitUZ=Podatnik.pitUZ, pitO=Podatnik.pitO)

if __name__ == '__main__':
    app.run(debug=True)