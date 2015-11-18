from flask import Flask, request, render_template

app = Flask(__name__)

def replace(value):
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

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/panel/')
def panel():
  return render_template('panel.html')

@app.route('/pit37', methods=['GET', 'POST'])
def pit11():

  sposob = request.form['sposob']
  pit11_ilosc = int(request.form['pit11_ilosc'])
  pit11_ilosc_m = int(request.form['pit11_ilosc_m'])

  jeden_procent = request.form['jeden_procent']
  cel = request.form['cel']
  dzieci = int(request.form['dzieci'])
  internet = replace(request.form['internet'])
  kto_internet = request.form['kto_internet']

  kto_dzieci_1 = request.form['kto_dzieci_1']
  kto_dzieci_2 = request.form['kto_dzieci_2']
  kto_dzieci_3 = request.form['kto_dzieci_3']
  kto_dzieci_4 = request.form['kto_dzieci_4']

  ile_miesiecy_1 = int(request.form['ile_miesiecy_1'])
  ile_miesiecy_2 = int(request.form['ile_miesiecy_2'])
  ile_miesiecy_3 = int(request.form['ile_miesiecy_3'])
  ile_miesiecy_4 = int(request.form['ile_miesiecy_4'])


  kwota_na_dziecko_1i2 = 92.67
  kwota_na_dziecko_3i4 = 166.67

  kwota_na_dzieci_podatnik = 0.0
  kwota_na_dzieci_malzonek = 0.0
  if dzieci >= 1:
    if kto_dzieci_1 == 'dz_podatnik':
      kwota_na_dzieci_podatnik += round((kwota_na_dziecko_1i2 * ile_miesiecy_1), 2)
    elif kto_dzieci_1 == 'dz_malzonek':
      kwota_na_dzieci_malzonek += round((kwota_na_dziecko_1i2 * ile_miesiecy_1), 2)
  if dzieci >= 2:
    if kto_dzieci_2 == 'dz_podatnik':
      kwota_na_dzieci_podatnik += round((kwota_na_dziecko_1i2 * ile_miesiecy_2), 2)
    elif kto_dzieci_2 == 'dz_malzonek':
      kwota_na_dzieci_malzonek += round((kwota_na_dziecko_1i2 * ile_miesiecy_2), 2)
  if dzieci >= 3:
    if kto_dzieci_3 == 'dz_podatnik':
      kwota_na_dzieci_podatnik += round((kwota_na_dziecko_3i4 * ile_miesiecy_3), 2)
    elif kto_dzieci_3 == 'dz_malzonek':
      kwota_na_dzieci_malzonek += round((kwota_na_dziecko_3i4 * ile_miesiecy_3), 2)
  if dzieci == 4:
    if kto_dzieci_4 == 'dz_podatnik':
      kwota_na_dzieci_podatnik += round((kwota_na_dziecko_3i4 * ile_miesiecy_4), 2)
    elif kto_dzieci_4 == 'dz_malzonek':
      kwota_na_dzieci_malzonek += round((kwota_na_dziecko_3i4 * ile_miesiecy_4), 2)


  urzad5 = request.form['urzad5']
  identyfikator10 = request.form['identyfikator10']
  nazwisko11 = request.form['nazwisko11']
  imie12 = request.form['imie12']
  data13 = request.form['data13']
  kraj14 = request.form['kraj14']
  wojewodztwo15 = request.form['wojewodztwo15']
  powiat16 = request.form['powiat16']
  gmina17 = request.form['gmina17']
  ulica18 = request.form['ulica18']
  dom19 = request.form['dom19']
  lokal20 = request.form['lokal20']
  miejscowosc21 = request.form['miejscowosc21']
  kod22 = request.form['kod22']
  poczta23 = request.form['poczta23']

  przychod25 = replace(request.form['przychod25'])
  przychod26 = replace(request.form['przychod26'])
  przychod27 = replace(request.form['przychod27'])
  przychod28 = replace(request.form['przychod28'])
  przychod29 = replace(request.form['przychod29'])
  przychod30 = replace(request.form['przychod30'])

  przychod31 = replace(request.form['przychod31'])
  przychod32 = replace(request.form['przychod32'])
  przychod33 = replace(request.form['przychod33'])
  przychod34 = replace(request.form['przychod34'])
  przychod35 = replace(request.form['przychod35'])
  przychod36 = replace(request.form['przychod36'])
  przychod37 = replace(request.form['przychod37'])
  przychod38 = replace(request.form['przychod38'])
  przychod39 = replace(request.form['przychod39'])
  przychod40 = replace(request.form['przychod40'])

  przychod41 = replace(request.form['przychod41'])
  przychod42 = replace(request.form['przychod42'])
  przychod43 = replace(request.form['przychod43'])
  przychod44 = replace(request.form['przychod44'])
  przychod45 = replace(request.form['przychod45'])
  przychod46 = replace(request.form['przychod46'])
  przychod47 = replace(request.form['przychod47'])
  przychod48 = replace(request.form['przychod48'])
  przychod49 = replace(request.form['przychod49'])

  przychod50 = replace(request.form['przychod50'])
  przychod51 = replace(request.form['przychod51'])
  przychod52 = replace(request.form['przychod52'])
  przychod53 = replace(request.form['przychod53'])
  przychod54 = replace(request.form['przychod54'])
  przychod55 = replace(request.form['przychod55'])
  przychod56 = replace(request.form['przychod56'])
  przychod57 = replace(request.form['przychod57'])
  przychod58 = replace(request.form['przychod58'])
  przychod59 = replace(request.form['przychod59'])

  przychod60 = replace(request.form['przychod60'])
  przychod61 = replace(request.form['przychod61'])
  przychod62 = replace(request.form['przychod62'])
  przychod63 = replace(request.form['przychod63'])
  przychod64 = replace(request.form['przychod64'])
  przychod65 = replace(request.form['przychod65'])

  skladki66 = replace(request.form['skladki66'])
  skladki67 = replace(request.form['skladki67'])
  zdrowotna68 = replace(request.form['zdrowotna68'])
  zdrowotna69 = replace(request.form['zdrowotna69'])


  suma_1_przychod = round(przychod25, 2)
  suma_1_koszty = round(przychod26, 2)
  suma_1_przychod_50 = round(przychod30, 2)
  suma_1_koszty_50 = round(przychod31, 2)
  suma_1_dochod = round(suma_1_przychod - suma_1_koszty, 2)
  suma_1_zaliczka = round(przychod29, 2)

  suma_2_przychod = round(przychod35, 2)
  suma_2_dochod = suma_2_przychod
  suma_2_zaliczka = round(przychod38, 2)

  suma_3_przychod = round(przychod45, 2)
  suma_3_koszty = round(przychod46, 2)
  suma_3_dochod = round(suma_3_przychod - suma_3_koszty, 2)
  suma_3_zaliczka = round(przychod48, 2)

  suma_4_przychod_20 = round(przychod53, 2)
  suma_4_przychod_50 = round(przychod56, 2)
  suma_4_koszty = round(przychod57, 2)
  suma_4_dochod = round(suma_4_przychod_20 + suma_4_przychod_50 - suma_4_koszty, 2)
  suma_4_zaliczka = round(przychod55, 2)

  suma_5_przychod = round(przychod32 + przychod39 + przychod42 + przychod49 + przychod58 + przychod62, 2)
  suma_5_koszty = round(przychod50 + przychod59, 2)
  suma_5_dochod = round(suma_5_przychod - suma_5_koszty, 2)
  suma_5_zaliczka = round(przychod34 + przychod41 + przychod44 + przychod52 + przychod61 + przychod65, 2)

############################################################################

  if pit11_ilosc == 2 or pit11_ilosc == 3:
    przychod25b = replace(request.form['przychod25b'])
    przychod26b = replace(request.form['przychod26b'])
    przychod27b = replace(request.form['przychod27b'])
    przychod28b = replace(request.form['przychod28b'])
    przychod29b = replace(request.form['przychod29b'])
    przychod30b = replace(request.form['przychod30b'])

    przychod31b = replace(request.form['przychod31b'])
    przychod32b = replace(request.form['przychod32b'])
    przychod33b = replace(request.form['przychod33b'])
    przychod34b = replace(request.form['przychod34b'])
    przychod35b = replace(request.form['przychod35b'])
    przychod36b = replace(request.form['przychod36b'])
    przychod37b = replace(request.form['przychod37b'])
    przychod38b = replace(request.form['przychod38b'])
    przychod39b = replace(request.form['przychod39b'])
    przychod40b = replace(request.form['przychod40b'])

    przychod41b = replace(request.form['przychod41b'])
    przychod42b = replace(request.form['przychod42b'])
    przychod43b = replace(request.form['przychod43b'])
    przychod44b = replace(request.form['przychod44b'])
    przychod45b = replace(request.form['przychod45b'])
    przychod46b = replace(request.form['przychod46b'])
    przychod47b = replace(request.form['przychod47b'])
    przychod48b = replace(request.form['przychod48b'])
    przychod49b = replace(request.form['przychod49b'])

    przychod50b = replace(request.form['przychod50b'])
    przychod51b = replace(request.form['przychod51b'])
    przychod52b = replace(request.form['przychod52b'])
    przychod53b = replace(request.form['przychod53b'])
    przychod54b = replace(request.form['przychod54b'])
    przychod55b = replace(request.form['przychod55b'])
    przychod56b = replace(request.form['przychod56b'])
    przychod57b = replace(request.form['przychod57b'])
    przychod58b = replace(request.form['przychod58b'])
    przychod59b = replace(request.form['przychod59b'])

    przychod60b = replace(request.form['przychod60b'])
    przychod61b = replace(request.form['przychod61b'])
    przychod62b = replace(request.form['przychod62b'])
    przychod63b = replace(request.form['przychod63b'])
    przychod64b = replace(request.form['przychod64b'])
    przychod65b = replace(request.form['przychod65b'])

    skladki66 += replace(request.form['skladki66b'])
    skladki67 += replace(request.form['skladki67b'])
    zdrowotna68 += replace(request.form['zdrowotna68b'])
    zdrowotna69 += replace(request.form['zdrowotna69b'])

    suma_1_przychod += round(przychod25b, 2)
    suma_1_koszty += round(przychod26b, 2)
    suma_1_przychod_50 += round(przychod30b, 2)
    suma_1_koszty_50 += round(przychod31b, 2)
    suma_1_dochod = round(suma_1_przychod - suma_1_koszty, 2)
    suma_1_zaliczka += round(przychod29b, 2)

    suma_2_przychod += round(przychod35b, 2)
    suma_2_dochod = suma_2_przychod
    suma_2_zaliczka += round(przychod38b, 2)

    suma_3_przychod += round(przychod45b, 2)
    suma_3_koszty += round(przychod46b, 2)
    suma_3_dochod = round(suma_3_przychod - suma_3_koszty, 2)
    suma_3_zaliczka += round(przychod48b, 2)

    suma_4_przychod_20 += round(przychod53b, 2)
    suma_4_przychod_50 += round(przychod56b, 2)
    suma_4_koszty += round(przychod57b, 2)
    suma_4_dochod = round(suma_4_przychod_20 + suma_4_przychod_50 - suma_4_koszty, 2)
    suma_4_zaliczka += round(przychod55b, 2)

    suma_5_przychod += round(przychod32b + przychod39b + przychod42b + przychod49b + przychod58b + przychod62b, 2)
    suma_5_koszty += round(przychod50b + przychod59b, 2)
    suma_5_dochod = round(suma_5_przychod - suma_5_koszty, 2)
    suma_5_zaliczka += round(przychod34b + przychod41b + przychod44b + przychod52b + przychod61b + przychod65b, 2)

##############################################################################################

    if pit11_ilosc == 3:
      przychod25c = replace(request.form['przychod25c'])
      przychod26c = replace(request.form['przychod26c'])
      przychod27c = replace(request.form['przychod27c'])
      przychod28c = replace(request.form['przychod28c'])
      przychod29c = replace(request.form['przychod29c'])
      przychod30c = replace(request.form['przychod30c'])

      przychod31c = replace(request.form['przychod31c'])
      przychod32c = replace(request.form['przychod32c'])
      przychod33c = replace(request.form['przychod33c'])
      przychod34c = replace(request.form['przychod34c'])
      przychod35c = replace(request.form['przychod35c'])
      przychod36c = replace(request.form['przychod36c'])
      przychod37c = replace(request.form['przychod37c'])
      przychod38c = replace(request.form['przychod38c'])
      przychod39c = replace(request.form['przychod39c'])
      przychod40c = replace(request.form['przychod40c'])

      przychod41c = replace(request.form['przychod41c'])
      przychod42c = replace(request.form['przychod42c'])
      przychod43c = replace(request.form['przychod43c'])
      przychod44c = replace(request.form['przychod44c'])
      przychod45c = replace(request.form['przychod45c'])
      przychod46c = replace(request.form['przychod46c'])
      przychod47c = replace(request.form['przychod47c'])
      przychod48c = replace(request.form['przychod48c'])
      przychod49c = replace(request.form['przychod49c'])

      przychod50c = replace(request.form['przychod50c'])
      przychod51c = replace(request.form['przychod51c'])
      przychod52c = replace(request.form['przychod52c'])
      przychod53c = replace(request.form['przychod53c'])
      przychod54c = replace(request.form['przychod54c'])
      przychod55c = replace(request.form['przychod55c'])
      przychod56c = replace(request.form['przychod56c'])
      przychod57c = replace(request.form['przychod57c'])
      przychod58c = replace(request.form['przychod58c'])
      przychod59c = replace(request.form['przychod59c'])

      przychod60c = replace(request.form['przychod60c'])
      przychod61c = replace(request.form['przychod61c'])
      przychod62c = replace(request.form['przychod62c'])
      przychod63c = replace(request.form['przychod63c'])
      przychod64c = replace(request.form['przychod64c'])
      przychod65c = replace(request.form['przychod65c'])

      skladki66 += replace(request.form['skladki66c'])
      skladki67 += replace(request.form['skladki67c'])
      zdrowotna68 += replace(request.form['zdrowotna68c'])
      zdrowotna69 += replace(request.form['zdrowotna69c'])

      suma_1_przychod += round(przychod25c, 2)
      suma_1_koszty += round(przychod26c, 2)
      suma_1_przychod_50 += round(przychod30c, 2)
      suma_1_koszty_50 += round(przychod31c, 2)
      suma_1_dochod = round(suma_1_przychod - suma_1_koszty, 2)
      suma_1_zaliczka += round(przychod29c, 2)

      suma_2_przychod += round(przychod35c, 2)
      suma_2_dochod = suma_2_przychod
      suma_2_zaliczka += round(przychod38c, 2)

      suma_3_przychod += round(przychod45c, 2)
      suma_3_koszty += round(przychod46c, 2)
      suma_3_dochod = round(suma_3_przychod - suma_3_koszty, 2)
      suma_3_zaliczka += round(przychod48c, 2)

      suma_4_przychod_20 += round(przychod53c, 2)
      suma_4_przychod_50 += round(przychod56c, 2)
      suma_4_koszty += round(przychod57c, 2)
      suma_4_dochod = round(suma_4_przychod_20 + suma_4_przychod_50 - suma_4_koszty, 2)
      suma_4_zaliczka += round(przychod55c, 2)

      suma_5_przychod += round(przychod32c + przychod39c + przychod42c + przychod49c + przychod58c + przychod62c, 2)
      suma_5_koszty += round(przychod50c + przychod59c, 2)
      suma_5_dochod = round(suma_5_przychod - suma_5_koszty, 2)
      suma_5_zaliczka += round(przychod34c + przychod41c + przychod44c + przychod52c + przychod61c + przychod65c, 2)

######################################################################################################
######################################################################################################

  urzad5m = ''
  identyfikator10m = ''
  nazwisko11m = ''
  imie12m = ''
  data13m = ''
  kraj14m = ''
  wojewodztwo15m = ''
  powiat16m = ''
  gmina17m = ''
  ulica18m = ''
  dom19m = ''
  lokal20m = ''
  miejscowosc21m = ''
  kod22m = ''
  poczta23m = ''

  suma_1_przychodm = 0.0
  suma_1_kosztym = 0.0
  suma_1_przychod_50m = 0.0
  suma_1_koszty_50m = 0.0
  suma_1_dochodm = 0.0
  suma_1_zaliczkam = 0.0

  suma_2_przychodm = 0.0
  suma_2_dochodm = 0.0
  suma_2_zaliczkam = 0.0

  suma_3_przychodm = 0.0
  suma_3_kosztym = 0.0
  suma_3_dochodm = 0.0
  suma_3_zaliczkam = 0.0

  suma_4_przychod_20m = 0.0
  suma_4_przychod_50m = 0.0
  suma_4_kosztym = 0.0
  suma_4_dochodm = 0.0
  suma_4_zaliczkam = 0.0

  suma_5_przychodm = 0.0
  suma_5_kosztym = 0.0
  suma_5_dochodm = 0.0
  suma_5_zaliczkam = 0.0

  skladki66m = 0.0
  skladki67m = 0.0
  zdrowotna68m = 0.0
  zdrowotna69m = 0.0

  if (sposob == 'wspolnie' or sposob == 'wspolnie2') and (pit11_ilosc_m == 1 or pit11_ilosc_m == 2 or pit11_ilosc_m == 3):
    urzad5m = request.form['urzad5m']
    identyfikator10m = request.form['identyfikator10m']
    nazwisko11m = request.form['nazwisko11m']
    imie12m = request.form['imie12m']
    data13m = request.form['data13m']
    kraj14m = request.form['kraj14m']
    wojewodztwo15m = request.form['wojewodztwo15m']
    powiat16m = request.form['powiat16m']
    gmina17m = request.form['gmina17m']
    ulica18m = request.form['ulica18m']
    dom19m = request.form['dom19m']
    lokal20m = request.form['lokal20m']
    miejscowosc21m = request.form['miejscowosc21m']
    kod22m = request.form['kod22m']
    poczta23m = request.form['poczta23m']

    przychod25m = replace(request.form['przychod25m'])
    przychod26m = replace(request.form['przychod26m'])
    przychod27m = replace(request.form['przychod27m'])
    przychod28m = replace(request.form['przychod28m'])
    przychod29m = replace(request.form['przychod29m'])
    przychod30m = replace(request.form['przychod30m'])

    przychod31m = replace(request.form['przychod31m'])
    przychod32m = replace(request.form['przychod32m'])
    przychod33m = replace(request.form['przychod33m'])
    przychod34m = replace(request.form['przychod34m'])
    przychod35m = replace(request.form['przychod35m'])
    przychod36m = replace(request.form['przychod36m'])
    przychod37m = replace(request.form['przychod37m'])
    przychod38m = replace(request.form['przychod38m'])
    przychod39m = replace(request.form['przychod39m'])
    przychod40m = replace(request.form['przychod40m'])

    przychod41m = replace(request.form['przychod41m'])
    przychod42m = replace(request.form['przychod42m'])
    przychod43m = replace(request.form['przychod43m'])
    przychod44m = replace(request.form['przychod44m'])
    przychod45m = replace(request.form['przychod45m'])
    przychod46m = replace(request.form['przychod46m'])
    przychod47m = replace(request.form['przychod47m'])
    przychod48m = replace(request.form['przychod48m'])
    przychod49m = replace(request.form['przychod49m'])

    przychod50m = replace(request.form['przychod50m'])
    przychod51m = replace(request.form['przychod51m'])
    przychod52m = replace(request.form['przychod52m'])
    przychod53m = replace(request.form['przychod53m'])
    przychod54m = replace(request.form['przychod54m'])
    przychod55m = replace(request.form['przychod55m'])
    przychod56m = replace(request.form['przychod56m'])
    przychod57m = replace(request.form['przychod57m'])
    przychod58m = replace(request.form['przychod58m'])
    przychod59m = replace(request.form['przychod59m'])

    przychod60m = replace(request.form['przychod60m'])
    przychod61m = replace(request.form['przychod61m'])
    przychod62m = replace(request.form['przychod62m'])
    przychod63m = replace(request.form['przychod63m'])
    przychod64m = replace(request.form['przychod64m'])
    przychod65m = replace(request.form['przychod65m'])

    skladki66m = replace(request.form['skladki66m'])
    skladki67m = replace(request.form['skladki67m'])
    zdrowotna68m = replace(request.form['zdrowotna68m'])
    zdrowotna69m = replace(request.form['zdrowotna69m'])

    suma_1_przychodm += round(przychod25m, 2)
    suma_1_kosztym += round(przychod26m, 2)
    suma_1_przychod_50m += round(przychod30m, 2)
    suma_1_koszty_50m += round(przychod31m, 2)
    suma_1_dochodm = round(suma_1_przychodm - suma_1_kosztym, 2)
    suma_1_zaliczkam += round(przychod29m, 2)

    suma_2_przychodm += round(przychod35m, 2)
    suma_2_dochodm = suma_2_przychodm
    suma_2_zaliczkam += round(przychod38m, 2)

    suma_3_przychodm += round(przychod45m, 2)
    suma_3_kosztym += round(przychod46m, 2)
    suma_3_dochodm = round(suma_3_przychodm - suma_3_kosztym, 2)
    suma_3_zaliczkam += round(przychod48m, 2)

    suma_4_przychod_20m += round(przychod53m, 2)
    suma_4_przychod_50m += round(przychod56m, 2)
    suma_4_kosztym += round(przychod57m, 2)
    suma_4_dochodm = round(suma_4_przychod_20m + suma_4_przychod_50m - suma_4_kosztym, 2)
    suma_4_zaliczkam += round(przychod55m, 2)

    suma_5_przychodm += round(przychod32m + przychod39m + przychod42m + przychod49m + przychod58m + przychod62m, 2)
    suma_5_kosztym += round(przychod50m + przychod59m, 2)
    suma_5_dochodm = round(suma_5_przychodm - suma_5_kosztym, 2)
    suma_5_zaliczkam += round(przychod34m + przychod41m + przychod44m + przychod52m + przychod61m + przychod65m, 2)

    ######################################################################################################

    if pit11_ilosc_m == 2 or pit11_ilosc_m == 3:
      przychod25mb = replace(request.form['przychod25mb'])
      przychod26mb = replace(request.form['przychod26mb'])
      przychod27mb = replace(request.form['przychod27mb'])
      przychod28mb = replace(request.form['przychod28mb'])
      przychod29mb = replace(request.form['przychod29mb'])
      przychod30mb = replace(request.form['przychod30mb'])

      przychod31mb = replace(request.form['przychod31mb'])
      przychod32mb = replace(request.form['przychod32mb'])
      przychod33mb = replace(request.form['przychod33mb'])
      przychod34mb = replace(request.form['przychod34mb'])
      przychod35mb = replace(request.form['przychod35mb'])
      przychod36mb = replace(request.form['przychod36mb'])
      przychod37mb = replace(request.form['przychod37mb'])
      przychod38mb = replace(request.form['przychod38mb'])
      przychod39mb = replace(request.form['przychod39mb'])
      przychod40mb = replace(request.form['przychod40mb'])

      przychod41mb = replace(request.form['przychod41mb'])
      przychod42mb = replace(request.form['przychod42mb'])
      przychod43mb = replace(request.form['przychod43mb'])
      przychod44mb = replace(request.form['przychod44mb'])
      przychod45mb = replace(request.form['przychod45mb'])
      przychod46mb = replace(request.form['przychod46mb'])
      przychod47mb = replace(request.form['przychod47mb'])
      przychod48mb = replace(request.form['przychod48mb'])
      przychod49mb = replace(request.form['przychod49mb'])

      przychod50mb = replace(request.form['przychod50mb'])
      przychod51mb = replace(request.form['przychod51mb'])
      przychod52mb = replace(request.form['przychod52mb'])
      przychod53mb = replace(request.form['przychod53mb'])
      przychod54mb = replace(request.form['przychod54mb'])
      przychod55mb = replace(request.form['przychod55mb'])
      przychod56mb = replace(request.form['przychod56mb'])
      przychod57mb = replace(request.form['przychod57mb'])
      przychod58mb = replace(request.form['przychod58mb'])
      przychod59mb = replace(request.form['przychod59mb'])

      przychod60mb = replace(request.form['przychod60mb'])
      przychod61mb = replace(request.form['przychod61mb'])
      przychod62mb = replace(request.form['przychod62mb'])
      przychod63mb = replace(request.form['przychod63mb'])
      przychod64mb = replace(request.form['przychod64mb'])
      przychod65mb = replace(request.form['przychod65mb'])

      skladki66m += replace(request.form['skladki66mb'])
      skladki67m += replace(request.form['skladki67mb'])
      zdrowotna68m += replace(request.form['zdrowotna68mb'])
      zdrowotna69m += replace(request.form['zdrowotna69mb'])

      suma_1_przychodm += round(przychod25mb, 2)
      suma_1_kosztym += round(przychod26mb, 2)
      suma_1_przychod_50m += round(przychod30mb, 2)
      suma_1_koszty_50m += round(przychod31mb, 2)
      suma_1_dochodm = round(suma_1_przychodm - suma_1_kosztym, 2)
      suma_1_zaliczkam += round(przychod29mb, 2)

      suma_2_przychodm += round(przychod35mb, 2)
      suma_2_dochodm = suma_2_przychodm
      suma_2_zaliczkam += round(przychod38mb, 2)

      suma_3_przychodm += round(przychod45mb, 2)
      suma_3_kosztym += round(przychod46mb, 2)
      suma_3_dochodm = round(suma_3_przychodm - suma_3_kosztym, 2)
      suma_3_zaliczkam += round(przychod48mb, 2)

      suma_4_przychod_20m += round(przychod53mb, 2)
      suma_4_przychod_50m += round(przychod56mb, 2)
      suma_4_kosztym += round(przychod57mb, 2)
      suma_4_dochodm = round(suma_4_przychod_20m + suma_4_przychod_50m - suma_4_kosztym, 2)
      suma_4_zaliczkam += round(przychod55mb, 2)

      suma_5_przychodm += round(przychod32mb + przychod39mb + przychod42mb + przychod49mb + przychod58mb + przychod62mb, 2)
      suma_5_kosztym += round(przychod50mb + przychod59mb, 2)
      suma_5_dochodm = round(suma_5_przychodm - suma_5_kosztym, 2)
      suma_5_zaliczkam += round(przychod34mb + przychod41mb + przychod44mb + przychod52mb + przychod61mb + przychod65mb, 2)

      ####################################################################################################
      if pit11_ilosc_m == 3:
        przychod25mc = replace(request.form['przychod25mc'])
        przychod26mc = replace(request.form['przychod26mc'])
        przychod27mc = replace(request.form['przychod27mc'])
        przychod28mc = replace(request.form['przychod28mc'])
        przychod29mc = replace(request.form['przychod29mc'])
        przychod30mc = replace(request.form['przychod30mc'])

        przychod31mc = replace(request.form['przychod31mc'])
        przychod32mc = replace(request.form['przychod32mc'])
        przychod33mc = replace(request.form['przychod33mc'])
        przychod34mc = replace(request.form['przychod34mc'])
        przychod35mc = replace(request.form['przychod35mc'])
        przychod36mc = replace(request.form['przychod36mc'])
        przychod37mc = replace(request.form['przychod37mc'])
        przychod38mc = replace(request.form['przychod38mc'])
        przychod39mc = replace(request.form['przychod39mc'])
        przychod40mc = replace(request.form['przychod40mc'])

        przychod41mc = replace(request.form['przychod41mc'])
        przychod42mc = replace(request.form['przychod42mc'])
        przychod43mc = replace(request.form['przychod43mc'])
        przychod44mc = replace(request.form['przychod44mc'])
        przychod45mc = replace(request.form['przychod45mc'])
        przychod46mc = replace(request.form['przychod46mc'])
        przychod47mc = replace(request.form['przychod47mc'])
        przychod48mc = replace(request.form['przychod48mc'])
        przychod49mc = replace(request.form['przychod49mc'])

        przychod50mc = replace(request.form['przychod50mc'])
        przychod51mc = replace(request.form['przychod51mc'])
        przychod52mc = replace(request.form['przychod52mc'])
        przychod53mc = replace(request.form['przychod53mc'])
        przychod54mc = replace(request.form['przychod54mc'])
        przychod55mc = replace(request.form['przychod55mc'])
        przychod56mc = replace(request.form['przychod56mc'])
        przychod57mc = replace(request.form['przychod57mc'])
        przychod58mc = replace(request.form['przychod58mc'])
        przychod59mc = replace(request.form['przychod59mc'])

        przychod60mc = replace(request.form['przychod60mc'])
        przychod61mc = replace(request.form['przychod61mc'])
        przychod62mc = replace(request.form['przychod62mc'])
        przychod63mc = replace(request.form['przychod63mc'])
        przychod64mc = replace(request.form['przychod64mc'])
        przychod65mc = replace(request.form['przychod65mc'])

        skladki66m += replace(request.form['skladki66mc'])
        skladki67m += replace(request.form['skladki67mc'])
        zdrowotna68m += replace(request.form['zdrowotna68mc'])
        zdrowotna69m += replace(request.form['zdrowotna69mc'])

        suma_1_przychodm += round(przychod25mc, 2)
        suma_1_kosztym += round(przychod26mc, 2)
        suma_1_przychod_50m += round(przychod30mc, 2)
        suma_1_koszty_50m += round(przychod31mc, 2)
        suma_1_dochodm = round(suma_1_przychodm - suma_1_kosztym, 2)
        suma_1_zaliczkam += round(przychod29mc, 2)

        suma_2_przychodm += round(przychod35mc, 2)
        suma_2_dochodm = suma_2_przychodm
        suma_2_zaliczkam += round(przychod38mc, 2)

        suma_3_przychodm += round(przychod45mc, 2)
        suma_3_kosztym += round(przychod46mc, 2)
        suma_3_dochodm = round(suma_3_przychodm - suma_3_kosztym, 2)
        suma_3_zaliczkam += round(przychod48mc, 2)

        suma_4_przychod_20m += round(przychod53mc, 2)
        suma_4_przychod_50m += round(przychod56mc, 2)
        suma_4_kosztym += round(przychod57mc, 2)
        suma_4_dochodm = round(suma_4_przychod_20m + suma_4_przychod_50m - suma_4_kosztym, 2)
        suma_4_zaliczkam += round(przychod55mc, 2)

        suma_5_przychodm += round(przychod32mc + przychod39mc + przychod42mc + przychod49mc + przychod58mc + przychod62mc, 2)
        suma_5_kosztym += round(przychod50mc + przychod59mc, 2)
        suma_5_dochodm = round(suma_5_przychodm - suma_5_kosztym, 2)
        suma_5_zaliczkam += round(przychod34mc + przychod41mc + przychod44mc + przychod52mc + przychod61mc + przychod65mc, 2)

########################################################################################################

  suma_przychodow = round((suma_1_przychod + suma_1_przychod_50 + suma_2_przychod +
                           suma_3_przychod + suma_4_przychod_20 + suma_4_przychod_50 + suma_5_przychod), 2)
  suma_kosztow = round((suma_1_koszty + suma_1_koszty_50 + suma_3_koszty + suma_4_koszty + suma_5_koszty), 2)
  suma_dochodow = round((suma_1_dochod + suma_2_dochod + suma_3_dochod + suma_4_dochod + suma_5_dochod), 2)
  suma_zaliczek = round((suma_1_zaliczka + suma_2_zaliczka + suma_3_zaliczka + suma_4_zaliczka + suma_5_zaliczka), 2)

  suma_przychodow_M = round((suma_1_przychodm + suma_1_przychod_50m + suma_2_przychodm + suma_3_przychodm +
                             suma_4_przychod_20m + suma_4_przychod_50m + suma_5_przychodm), 2)
  suma_kosztow_M = round((suma_1_kosztym + suma_1_koszty_50m + suma_3_kosztym + suma_4_kosztym + suma_5_kosztym), 2)
  suma_dochodow_M = round((suma_1_dochodm + suma_2_dochodm + suma_3_dochodm + suma_4_dochodm + suma_5_dochodm), 2)
  suma_zaliczek_M = round((suma_1_zaliczkam + suma_2_zaliczkam + suma_3_zaliczkam + suma_4_zaliczkam + suma_5_zaliczkam), 2)

################### INTERNET ################################################
  if internet > 760:
    internet = 760
  razem_odliczenia_od_dochodu_B_podatnik = 0.0
  razem_odliczenia_od_dochodu_B_malzonek = 0.0
  if sposob == 'indywidualnie' or sposob == 'samotnie':
    if kto_internet == 'int_podatnik':
      razem_odliczenia_od_dochodu_B_podatnik += internet
      if razem_odliczenia_od_dochodu_B_podatnik > suma_dochodow - skladki66:
        razem_odliczenia_od_dochodu_B_podatnik = suma_dochodow - skladki66
    else:
      razem_odliczenia_od_dochodu_B_podatnik = 0.0
  else:
    if kto_internet == 'int_podatnik':
      razem_odliczenia_od_dochodu_B_podatnik += internet
      if razem_odliczenia_od_dochodu_B_podatnik > suma_dochodow - skladki66:
        razem_odliczenia_od_dochodu_B_podatnik = suma_dochodow - skladki66
    else:
      razem_odliczenia_od_dochodu_B_malzonek += internet
      if razem_odliczenia_od_dochodu_B_malzonek > suma_dochodow - skladki66:
        razem_odliczenia_od_dochodu_B_malzonek = suma_dochodow - skladki66

########################################################################################################


################################# PODATEK ###############################################################

  dochod_po_odliczeniach111 = round((suma_dochodow - skladki66 + suma_dochodow_M - skladki66m - razem_odliczenia_od_dochodu_B_podatnik -
                                     razem_odliczenia_od_dochodu_B_malzonek), 2)
  kwota_wolna_od_podatku = 1668.06

  dochod_po_odliczeniach112 = 0
  obliczony_podatek113 = 0
  if sposob == 'indywidualnie':
    dochod_po_odliczeniach112 = round(dochod_po_odliczeniach111, 0)
    if dochod_po_odliczeniach112 <= 85528:
      obliczony_podatek113 = round(dochod_po_odliczeniach112 * 0.18 - kwota_wolna_od_podatku, 2)
      if obliczony_podatek113 < 0:
        obliczony_podatek113 = 0.0
    else:
      obliczony_podatek113 = round((dochod_po_odliczeniach112 * 0.18 - kwota_wolna_od_podatku +
                                    (dochod_po_odliczeniach112 - 85528) * 0.18 - kwota_wolna_od_podatku), 2)
      if obliczony_podatek113 < 0:
        obliczony_podatek113 = 0.0
  else:
    dochod_po_odliczeniach112 = round(dochod_po_odliczeniach111 / 2, 0)
    if dochod_po_odliczeniach112 <= 85528:
      obliczony_podatek113 = 2 * (round(dochod_po_odliczeniach112 * 0.18 - kwota_wolna_od_podatku, 2))
      if obliczony_podatek113 < 0:
        obliczony_podatek113 = 0.0
    else:
      obliczony_podatek113 = round(2 * (dochod_po_odliczeniach112 * 0.18 - kwota_wolna_od_podatku) + (dochod_po_odliczeniach112 - 85528) * 0.32, 2)
      if obliczony_podatek113 < 0:
        obliczony_podatek113 = 0.0

################### DIECI ################################################
  razem_odliczenia_od_podatku_pit_o_C_podatnik = kwota_na_dzieci_podatnik
  razem_odliczenia_od_podatku_pit_o_C_malzonek = kwota_na_dzieci_malzonek

  if razem_odliczenia_od_podatku_pit_o_C_podatnik + razem_odliczenia_od_podatku_pit_o_C_malzonek > obliczony_podatek113 - zdrowotna68 - zdrowotna68m\
          and (obliczony_podatek113 - zdrowotna68 - zdrowotna68m) >= 0:
    if razem_odliczenia_od_podatku_pit_o_C_podatnik > obliczony_podatek113 - zdrowotna68 - zdrowotna68m:
      razem_odliczenia_od_podatku_pit_o_C_podatnik = obliczony_podatek113 - zdrowotna68 - zdrowotna68m
      razem_odliczenia_od_podatku_pit_o_C_malzonek = 0.0
    else:
      razem_odliczenia_od_podatku_pit_o_C_malzonek = (obliczony_podatek113 - zdrowotna68 - zdrowotna68m) - razem_odliczenia_od_podatku_pit_o_C_podatnik


  if sposob == 'indywidualnie' and suma_dochodow > 56000:
    razem_odliczenia_od_podatku_pit_o_C_podatnik = 0
  elif sposob == 'wspolnie' and suma_dochodow + suma_dochodow_M > 112000:
    razem_odliczenia_od_podatku_pit_o_C_podatnik = 0
    razem_odliczenia_od_podatku_pit_o_C_malzonek = 0
  elif sposob == 'wspolnie2' and suma_dochodow + suma_dochodow_M > 112000:
    razem_odliczenia_od_podatku_pit_o_C_podatnik = 0
    razem_odliczenia_od_podatku_pit_o_C_malzonek = 0
  elif sposob == 'samotnie' and suma_dochodow > 112000:
    razem_odliczenia_od_podatku_pit_o_C_podatnik = 0


  razem_odliczenia_od_podatku_pit_o_C = razem_odliczenia_od_podatku_pit_o_C_podatnik + razem_odliczenia_od_podatku_pit_o_C_malzonek

  podatek_po_doliczeniach122 = round(obliczony_podatek113 - zdrowotna68 - zdrowotna68m - razem_odliczenia_od_podatku_pit_o_C, 2)
  if zdrowotna68 + zdrowotna68m > obliczony_podatek113:
    podatek_po_doliczeniach122 = 0.0

  ########################### KIEDY PIT/UZ #################################################
  pit_uz = 'nie'
  if (kwota_na_dzieci_podatnik + kwota_na_dzieci_malzonek) > (obliczony_podatek113 - zdrowotna68 - zdrowotna68m)\
          and (obliczony_podatek113 - zdrowotna68 - zdrowotna68m) >= 0:
    pit_uz = 'tak'

  pit_uz_14 = (kwota_na_dzieci_podatnik - razem_odliczenia_od_podatku_pit_o_C_podatnik) + (kwota_na_dzieci_malzonek - razem_odliczenia_od_podatku_pit_o_C_malzonek)
  if pit_uz_14 < 0:
    pit_uz_14 = 0.0
  if pit_uz_14 > ((skladki66 + zdrowotna68) + (skladki66m + zdrowotna68m)):
    pit_uz_14 = (skladki66 + zdrowotna68) + (skladki66m + zdrowotna68m)

#############################################################################################

  podatek_nalezny126 = round(podatek_po_doliczeniach122, 0)

  do_zaplaty = round(podatek_po_doliczeniach122 - (suma_zaliczek + suma_zaliczek_M), 0)
  if do_zaplaty < 0: do_zaplaty = 0.0
  nadplata = round((suma_zaliczek + suma_zaliczek_M) - podatek_po_doliczeniach122, 0)
  if nadplata < 0: nadplata = 0.0

  jeden_procent_kwota = 0.01 * podatek_po_doliczeniach122

  return render_template('pit11_action.html', sposob=sposob, kto_internet=kto_internet, internet=internet,
                         jeden_procent=jeden_procent, dzieci=dzieci, ile_miesiecy_1=ile_miesiecy_1,
                         ile_miesiecy_2=ile_miesiecy_2, ile_miesiecy_3=ile_miesiecy_3, ile_miesiecy_4=ile_miesiecy_4,
                         kto_dzieci_1=kto_dzieci_1, kto_dzieci_2=kto_dzieci_2, kto_dzieci_3=kto_dzieci_3, kto_dzieci_4=kto_dzieci_4,
                         kwota_na_dzieci_podatnik=kwota_na_dzieci_podatnik, kwota_na_dzieci_malzonek=kwota_na_dzieci_malzonek,
                         razem_odliczenia_od_podatku_pit_o_C_podatnik=razem_odliczenia_od_podatku_pit_o_C_podatnik,
                         razem_odliczenia_od_podatku_pit_o_C_malzonek=razem_odliczenia_od_podatku_pit_o_C_malzonek,
                         razem_odliczenia_od_dochodu_B_podatnik=razem_odliczenia_od_dochodu_B_podatnik,
                         razem_odliczenia_od_dochodu_B_malzonek=razem_odliczenia_od_dochodu_B_malzonek,
                         pit_uz=pit_uz, pit_uz_14=pit_uz_14,

                         urzad5=urzad5, identyfikator10=identyfikator10,
                         nazwisko11=nazwisko11, imie12=imie12,
                         data13=data13, kraj14=kraj14,
                         wojewodztwo15=wojewodztwo15, powiat16=powiat16,
                         gmina17=gmina17, ulica18=ulica18,
                         dom19=dom19, lokal20=lokal20,
                         miejscowosc21=miejscowosc21, kod22=kod22,
                         poczta23=poczta23,

                         suma_1_przychod=suma_1_przychod, suma_1_koszty=suma_1_koszty,
                         suma_1_dochod=suma_1_dochod, suma_1_zaliczka=suma_1_zaliczka,
                         suma_1_przychod_50=suma_1_przychod_50, suma_1_koszty_50=suma_1_koszty_50,

                         suma_2_przychod=suma_2_przychod, suma_2_dochod=suma_2_dochod,
                         suma_2_zaliczka=suma_2_zaliczka,

                         suma_3_przychod=suma_3_przychod, suma_3_koszty=suma_3_koszty,
                         suma_3_dochod=suma_3_dochod, suma_3_zaliczka=suma_3_zaliczka,

                         suma_4_przychod_20=suma_4_przychod_20, suma_4_przychod_50=suma_4_przychod_50,
                         suma_4_koszty=suma_4_koszty, suma_4_dochod=suma_4_dochod,
                         suma_4_zaliczka=suma_4_zaliczka,

                         suma_5_przychod=suma_5_przychod, suma_5_koszty=suma_5_koszty,
                         suma_5_dochod=suma_5_dochod, suma_5_zaliczka=suma_5_zaliczka,

                         urzad5m=urzad5m, identyfikator10m=identyfikator10m,
                         nazwisko11m=nazwisko11m, imie12m=imie12m,
                         data13m=data13m, kraj14m=kraj14m,
                         wojewodztwo15m=wojewodztwo15m, powiat16m=powiat16m,
                         gmina17m=gmina17m, ulica18m=ulica18m,
                         dom19m=dom19m, lokal20m=lokal20m,
                         miejscowosc21m=miejscowosc21m, kod22m=kod22m,
                         poczta23m=poczta23m,

                         suma_1_przychodm=suma_1_przychodm, suma_1_kosztym=suma_1_kosztym,
                         suma_1_dochodm=suma_1_dochodm, suma_1_zaliczkam=suma_1_zaliczkam,
                         suma_1_przychod_50m=suma_1_przychod_50m, suma_1_koszty_50m=suma_1_koszty_50m,

                         suma_2_przychodm=suma_2_przychodm, suma_2_dochodm=suma_2_dochodm,
                         suma_2_zaliczkam=suma_2_zaliczkam,

                         suma_3_przychodm=suma_3_przychodm, suma_3_kosztym=suma_3_kosztym,
                         suma_3_dochodm=suma_3_dochodm, suma_3_zaliczkam=suma_3_zaliczkam,

                         suma_4_przychod_20m=suma_4_przychod_20m, suma_4_przychod_50m=suma_4_przychod_50m,
                         suma_4_kosztym=suma_4_kosztym, suma_4_dochodm=suma_4_dochodm,
                         suma_4_zaliczkam=suma_4_zaliczkam,

                         suma_5_przychodm=suma_5_przychodm, suma_5_kosztym=suma_5_kosztym,
                         suma_5_dochodm=suma_5_dochodm, suma_5_zaliczkam=suma_5_zaliczkam,

                         suma_przychodow=suma_przychodow, suma_kosztow=suma_kosztow,
                         suma_dochodow=suma_dochodow, suma_zaliczek=suma_zaliczek,

                         suma_przychodow_M=suma_przychodow_M, suma_kosztow_M=suma_kosztow_M,
                         suma_dochodow_M=suma_dochodow_M, suma_zaliczek_M=suma_zaliczek_M,

                         skladki66=skladki66, skladki66m=skladki66m, skladki67=skladki67, skladki67m=skladki67m,
                         zdrowotna68=zdrowotna68, zdrowotna68m=zdrowotna68m, zdrowotna69=zdrowotna69, zdrowotna69m=zdrowotna69m,

                         dochod_po_odliczeniach111=dochod_po_odliczeniach111,
                         dochod_po_odliczeniach112=dochod_po_odliczeniach112, obliczony_podatek113=obliczony_podatek113,
                         podatek_po_doliczeniach122=podatek_po_doliczeniach122, podatek_nalezny126=podatek_nalezny126,
                         do_zaplaty=do_zaplaty, nadplata=nadplata,
                         jeden_procent_kwota=jeden_procent_kwota, cel=cel)


@app.route('/pit_action/', methods=['POST'])
def pit_action():
  return render_template('pit_action.html')

if __name__ == '__main__':
  app.run(debug=True)