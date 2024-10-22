def Funkca_Laczenia(list1: list, list2: list) -> list:
    Polaczona_lista = list(set(list1 + list2))
    Wynik = [x ** 3 for x in Polaczona_lista]
    return Wynik

list_a = [1, 2, 3, 4]
list_b = [3, 4, 5, 6]
result = Funkca_Laczenia(list_a, list_b)
print(result)