from datetime import datetime


from datetime import date

#ostatnie_laby =  "12-12-2024"
#data_kolokwium = "25-12-2024"


data_teraz = date.today()
# domyslne formatowanie to 2024-12-22 yyyy-mm-dd

data_teraz_str = data_teraz.strftime("%d/%m/%Y")
print(f"dzisiejsza data: {data_teraz_str}")

ostatnie_laby = "12/12/2024"

## zeby odjac od siebie daty, strptime() argument 1 must be str, not datetime.date
data_teraz_dt = datetime.strptime(data_teraz_str, "%d/%m/%Y")
ostatnie_laby_dt = datetime.strptime(ostatnie_laby, "%d/%m/%Y")

# subtract dates to get timedelta
ostatnie_laby_dni = (data_teraz_dt - ostatnie_laby_dt).days
print(f" {ostatnie_laby_dni} dni minelo od ostatnich labow")


#### kolokwium 
data_kolokwium = "25/12/2024"
kolokwium_dt = datetime.strptime(data_kolokwium, "%d/%m/%Y")
dni_do_kolokwium = (kolokwium_dt - data_teraz_dt).days

print(f" {dni_do_kolokwium} dni zostało do najblizszego kolokwium")



