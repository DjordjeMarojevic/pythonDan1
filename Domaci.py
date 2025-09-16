from functools import reduce,wraps
import time
from datetime import datetime


#17

def mjeracVremena(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Funkcija '{func.__name__}' je trajala {end - start} sekundi")
        return result
    return wrapper

#Date su dvije liste, jedna sa imenima studenata, a druga sa njihovim prosjecnim ocjenama.
#Napisati funkciju koja pronalazi studente sa prosjecnom ocjenom iznad 8.5 i vraća listu torki (ime,
#ocjena) za te studente.

def prvi(imena, ocjene):

    torke = zip(imena,ocjene)
    rj = []

    for torka in torke:
        if torka[1] > 8.5:
          rj.append(torka)  

    return rj

#print(prvi(["Djordje", "Ivan", 'Marko', 'Milos'], [8.5,9.2, 7.2,9.5]))

#Data je lista torki oblika [(ime, ocjena, predmet), ...]. Napisati funkciju koja koristi filter, map, i
#reduce da izracuna prosjecnu ocjenu po predmetu.

def drugi(lista):
   
    predmeti = set(map(lambda x: x[2], lista))
    
    rezultat = {}
    for predmet in predmeti:

        ocjene = list(map(lambda x: x[1], filter(lambda x: x[2] == predmet, lista)))    
        zbir = reduce(lambda a, b: a + b, ocjene)  
        rezultat[predmet] = zbir / len(ocjene)
    
    return rezultat


podaci = [
    ("Ana", 8, "Matematika"),
    ("Marko", 10, "Matematika"),
    ("Jelena", 9, "Fizika"),
    ("Milan", 7, "Matematika"),
    ("Ivana", 8, "Fizika")
]

#print(drugi(podaci))


#14

def append_to_file(data):
    
    with open("students.txt", "w", encoding="utf-8") as f:
        for student in data:
            line = f"{student['ime']},{student['prezime']},{student['godina']},{student['prosjek']}\n"
            f.write(line)



@mjeracVremena
def get_students_with_greater_grade(year,grade):

    if grade == "A":
        g = 9.5
    elif grade == "B":
        g = 8.5
    elif grade == "C":
        g = 7.5
    elif grade == "D":
        g = 6.5
    elif grade == "E":
        g = 6.0

    studenti = []
    with open("students.txt", "r", encoding="utf-8") as f:
        for linija in f:
            ime, prezime, godina, prosjek = linija.strip().split(",")
            if int(godina) == year and float(prosjek) > g:
                studenti.append({
                    "ime": ime,
                    "prezime": prezime,
                    "godina": int(godina),
                    "prosjek": float(prosjek)
                })
    return studenti

data1 = [{'ime': 'Marko', 'prezime':'Markovic', 'godina': 2, 'prosjek': 8.6 }, {'ime': 'Boris',
'prezime':'Boricic', 'godina': 3, 'prosjek': 7.9 }, {'ime': 'Novak', 'prezime': 'Novovic',
'godina': 3, 'prosjek': 6.9 }]

data2 = [
    {'ime': 'Ana', 'prezime': 'Anić', 'godina': 1, 'prosjek': 9.4},
    {'ime': 'Jelena', 'prezime': 'Jelić', 'godina': 2, 'prosjek': 8.2},
    {'ime': 'Milan', 'prezime': 'Milić', 'godina': 4, 'prosjek': 7.1}
]


#print(get_students_with_greater_grade(2,'C'))
#append_to_file(data2)


#16

def dodaj_igru_u_fajl(igra, file_path="igrice.txt"):
    with open(file_path, "a", encoding="utf-8") as f:
        linija = f"{igra['naziv']};{igra['ocjena']};{igra['godina']};{igra['izdavac']};{' '.join(igra['zanrovi'])}\n"
        f.write(linija)

def unesi_igru():
    TRENT_GODINA = datetime.now().year
    while True:
        print("\nUnesite novu igru (ili 'prekini' za kraj):")
        naziv = input("Naziv (2-50 karaktera): ")
        if naziv.lower() == "prekini":
            return None
        if not (2 <= len(naziv) <= 50):
            print("Greska: naziv mora biti između 2 i 50 karaktera.")
            continue

        ocjena_input = input("Ocjena (1.00 - 10.00): ")
        
        ocjena = round(float(ocjena_input), 2)
        if not (1 <= ocjena <= 10):
            print("Greska: ocjena mora biti između 1 i 10.")
            continue

        godina_input = input(f"Godina (>1950 i <{TRENT_GODINA}): ")
        
        godina = int(godina_input)
        if not (1950 < godina < TRENT_GODINA):
            print(f"Greska: godina mora biti između 1950 i {TRENT_GODINA-1}.")
            continue
       

        izdavac = input("Izdavac (2-40 karaktera, opcionalno): ")
        if izdavac and not (2 <= len(izdavac) <= 40):
            print("Greska: izdavac mora biti između 2 i 40 karaktera.")
            continue

        zanrovi_input = input("Žanrovi (maks. 3, razdvojeni razmakom): ")
        zanrovi_lista = zanrovi_input.split()
        if len(zanrovi_lista) > 3 or len(zanrovi_lista) == 0:
            print("Greska: maksimalno 3 žanra, najmanje 1.")
            continue

        igra = {
            "naziv": naziv,
            "ocjena": ocjena,
            "godina": godina,
            "izdavac": izdavac,
            "zanrovi": zanrovi_lista
        }

        dodaj_igru_u_fajl(igra)

    
def sacuvaj_samo_validne(file_path="igrice.txt"):
    validne_igre = []
    trenutna_godina = datetime.now().year
    zanrovi = ['Action', 'Crime', 'Adventure', 'RPG', 'Fantasy', 'Adventure', 'Sandbox', 'Survival', 'Adventure', 'Shooter', 'Action']

    
    with open(file_path, "r", encoding="utf-8") as f:
        for linija in f:
            delovi = linija.strip().split(";")
            if len(delovi) != 5:
                continue
            
            naziv, ocjena, godina, izdavac, zanrovi = delovi

            if not (2 <= len(naziv) <= 50):
                continue
            
            ocjena = round(float(ocjena), 2)
            if not (1 <= ocjena <= 10):
                continue
            
            godina = int(godina)
            if not (1950 < godina < trenutna_godina):
                continue
            if izdavac:
                if not (2 <= len(izdavac) <= 40):
                    continue
            zanrovi_lista = zanrovi.split()
            if len(zanrovi_lista) > 3:
                continue
    
            validne_igre.append(linija.strip())
    

    with open(file_path, "w", encoding="utf-8") as f:
        for linija in validne_igre:
            print(linija)
            f.write(linija + "\n")

def filtriraj_igre_interaktivno(igre):
    while True:
        print("1 - Po nazivu (igre koje pocinju sa terminom)")
        print("2 - Po ocjeni (veća od zadate)")
        print("3 - Po godini (prije ili nakon zadate godine)")
        print("4 - Po izdavacu (pocinje sa terminom)")
        print("5 - Po zanru (1, 2 ili 3 zanra)")
        print("0 - Kraj filtriranja")

        izbor = input("Izaberite opciju: ").strip()

        if izbor == "0":
            print("Kraj filtriranja.")
            break

        if izbor == "1":
            termin = input("Unesite pocetak naziva: ").lower()
            rezultat = [igra for igra in igre if igra['naziv'].lower().startswith(termin)]

        elif izbor == "2":
            try:
                min_ocjena = float(input("Unesite minimalnu ocjenu: "))
                rezultat = [igra for igra in igre if igra['ocjena'] > min_ocjena]
            except ValueError:
                print("Greska: unesite broj za ocjenu.")
                continue

        elif izbor == "3":
            try:
                godina = int(input("Unesite godinu: "))
                smjer = input("Prije ili nakon godine? (prije/nakon): ").strip().lower()
                if smjer == "prije":
                    rezultat = [igra for igra in igre if igra['godina'] < godina]
                elif smjer == "nakon":
                    rezultat = [igra for igra in igre if igra['godina'] > godina]
                else:
                    print("Greska: unesite 'prije' ili 'nakon'.")
                    continue
            except ValueError:
                print("Greska: unesite cijeli broj za godinu.")
                continue

        elif izbor == "4":
            termin = input("Unesite pocetak izdavaca: ").lower()
            rezultat = [igra for igra in igre if igra['izdavac'].lower().startswith(termin)]

        elif izbor == "5":
            zanrovi_input = input("Unesite žanr(e) razdvojene razmakom (max 3): ").split()
            if 0 < len(zanrovi_input) <= 3:
                rezultat = [igra for igra in igre if all(z.lower() in map(str.lower, igra['zanrovi']) for z in zanrovi_input)]
            else:
                print("Greska: unesite 1 do 3 žanra.")
                continue

        else:
            print("Nepoznata opcija. Pokusajte ponovo.")
            continue

        if rezultat:
            print("\nRezultati filtriranja")
            for igra in rezultat:
                print(f"{igra['naziv']};{igra['ocjena']};{igra['godina']};{igra['izdavac']};{' '.join(igra['zanrovi'])}")
        else:
            print("Nema igara koje zadovoljavaju kriterijum.")


def ucitaj_igre(file_path="igrice.txt"):
    igre = []
    with open(file_path, "r", encoding="utf-8") as f:
        for linija in f:
            delovi = linija.strip().split(";")
            if len(delovi) != 5:
                continue  
            
            naziv, ocjena, godina, izdavac, zanrovi = delovi
            
            igra_dict = {
                "naziv": naziv,
                "ocjena": round(float(ocjena), 2),
                "godina": int(godina),
                "izdavac": izdavac,
                "zanrovi": zanrovi.split()  
                }
            igre.append(igra_dict)
            
    return igre
    


unesi_igru()

