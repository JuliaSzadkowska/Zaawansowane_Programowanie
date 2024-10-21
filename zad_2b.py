#I wersja z for
def Funkcja_1(numbers):
    result = []
    for number in numbers:
        result.append(number * 2)
    return result

numbers = [1, 2, 3, 4, 5]
wynik_for = Funkcja_1(numbers)
print("Wynik z użyciem pętli for:", wynik_for)

#II wersja z listą składową
def Funckja_2(numbers):
    return [number * 2 for number in numbers]

wynik_lista_skladowa = Funckja_2(numbers)
print("Wynik z użyciem listy składanej:", wynik_lista_skladowa)