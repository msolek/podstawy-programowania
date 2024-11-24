streets = ['Jagodowa', 'Lipowa', 'Kwiatowa', 'Kasztanowa', 'Polna']
blocks = 5
flats = 10

for street in streets:
    for block in range(1,blocks+1):
        for flat in range(1,flats+1):
            print(f"Ulica: {street}, blok: {block}, apartament: /{flat}.")
