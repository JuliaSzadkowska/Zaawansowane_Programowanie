import requests
from typing import Optional

class Browar:
    def __init__(
        self,
        id: str,
        nazwa: str,
        typ_browaru: str,
        ulica: Optional[str],
        miasto: str,
        stan: Optional[str],
        kod_pocztowy: str,
        kraj: str,
        dlugosc_geograficzna: Optional[float],
        szerokosc_geograficzna: Optional[float],
        telefon: Optional[str],
        strona_www: Optional[str],
    ):
        self.id = id
        self.nazwa = nazwa
        self.typ_browaru = typ_browaru
        self.ulica = ulica
        self.miasto = miasto
        self.stan = stan
        self.kod_pocztowy = kod_pocztowy
        self.kraj = kraj
        self.dlugosc_geograficzna = dlugosc_geograficzna
        self.szerokosc_geograficzna = szerokosc_geograficzna
        self.telefon = telefon
        self.strona_www = strona_www

    def __str__(self):
        return (
            f"Browar: {self.nazwa}\n"
            f"Typ: {self.typ_browaru}\n"
            f"Lokalizacja: {self.ulica}, {self.miasto}, {self.stan}, {self.kod_pocztowy}, {self.kraj}\n"
            f"Współrzędne: ({self.szerokosc_geograficzna}, {self.dlugosc_geograficzna})\n"
            f"Telefon: {self.telefon}\n"
            f"Strona WWW: {self.strona_www}\n"
        )

def pobierz_browary():
    url = "https://api.openbrewerydb.org/breweries"
    params = {"per_page": 20}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print("Nie udało się pobrać danych browarów.")
        return []

def main():
    dane_browarow = pobierz_browary()
    browary = [
        Browar(
            id=dane.get("id"),
            nazwa=dane.get("name"),
            typ_browaru=dane.get("brewery_type"),
            ulica=dane.get("street"),
            miasto=dane.get("city"),
            stan=dane.get("state"),
            kod_pocztowy=dane.get("postal_code"),
            kraj=dane.get("country"),
            dlugosc_geograficzna=dane.get("longitude", None),
            szerokosc_geograficzna=dane.get("latitude", None),
            telefon=dane.get("phone", None),
            strona_www=dane.get("website_url", None),
        )
        for dane in dane_browarow
    ]

    for browar in browary:
        print(browar)

if __name__ == "__main__":
    main()
