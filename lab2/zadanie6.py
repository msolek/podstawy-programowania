litera = input("Podaj litere: ")

if litera.isalpha(): # sprawdzenie czy jest to litera
    if litera.isupper(): # sprawdzenie czy jest to duza litera
        print("Litera jest duza")
    else:
        print("Litera jest mala")
else: 
    print("Wprowadzony znak nie jest litera")
