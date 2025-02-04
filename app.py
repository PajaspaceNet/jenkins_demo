def add_numbers(a, b):
    """
    Funkce pro součet dvou čísel.
    """
    return a + b

if __name__ == "__main__":
    num1 = int(input("Zadejte první číslo: "))
    num2 = int(input("Zadejte druhé číslo: "))
    print(f"Součet: {add_numbers(num1, num2)}")
