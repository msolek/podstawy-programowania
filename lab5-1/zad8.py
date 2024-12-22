import keyword

slowa_kluczowe = [ "for", "print", "break", "done", "bad"]

for x in slowa_kluczowe:
    czy_slowo_kluczowe = keyword.iskeyword(x)
    print(f"czy {x} jest slowem kluczowym: {czy_slowo_kluczowe} ")
