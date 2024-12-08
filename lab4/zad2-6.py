import math

try:
    a = float(input("Podaj bok a: "))
    b = float(input("Podaj bok b: "))
    c = float(input("Podaj bok c: "))

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Boki musza byc dluzsze od 0!")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Podane boki nie tworza trojkata")

    # polobwod
    s = (a + b + c) / 2

    # pole za pomoca wzoru herona
    pole = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print(f"Pole trojkata wynosi : {pole:.2f}")

except ValueError as e:
    print(f"Blad: {e}")
except Exception as e:
    print(f"Nieoczekiwany blad: {e}")