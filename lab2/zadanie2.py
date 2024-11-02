x = float(input("Podaj x: "))
y = float(input("Podaj y: "))
z = float(input("Podaj z: "))

# Porzadkowaie liczb
if x > y:
    x,y = y,x # zamiana x i y, jesli x jest wieksze od y
if x > z:
    x,z = z,x # zamiana x i z, jesli x jest wieksze od z
if y > z:
    y,z = z,y # zamiana y i z, jesli y jest wieksze od z

print(f"Uporzadkowany wynik jest nastepujacy: x: {x}, y: {y}, z: {z}")


