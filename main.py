import random

#1
adatok = []
darabszam = 100
for db in range(darabszam):
    adatok.append(random.randint(50,100))
print(adatok)

#összegzés tétele
#sum - határozz meg az adatok lista elemének összegét.
sum = 0 
for item in adatok:
    sum += item

print(f"sum(lista) - {sum}")

#átlag - az adatok lista elemeinek átlagának meghatározása.
sum = 0 
for item in adatok:
    sum += item
átlag = sum / len(adatok)

print(f"átlag(lista) - {átlag}")

#prod - az adatok lista elemeinek szorzatának meghatározása.
prod = 1
for item in adatok:
    prod *= item

print(f"prod(lista) - {prod}")

#min-max tétel
#min - határozza meg az adatok lista elemének legkissebbjét.
min = adatok[0]
for item in adatok:
    if item < min:
        min = item

print(f"min(lista) - {min}")
#max - határozza meg az adatok lista elemének legnagyobbját.
max = adatok[0]
for item in adatok:
    if item > max:
        max = item

print(f"max(lista) - {max}")

#megszámlálás tétele
#határozza meg a 120-nál nagyobb elemek számát.
db1 = 0
for item in adatok:
    if item > 120:
        db1 += 1

print(f"db1(lista) - {db1}")

#határozzuk meg hogy az adatok lista hány darab 100-as elemet tartalmaz
db2 = 0
for item in adatok:
    if item == 100:
        db2 += 1

print(f"db2(lista) - {db2}")

#eldöntés tétele
#legalább egy elem teljesíti a feltételt
#Döntse el, hogy az adott elemek között van-e 50-es értékű elem.
vanE_50 = False
for item in adatok:
    if item == 50:
        vanE_50 = True
        break

if vanE_50:
    print("A lista tartalmaz, legalább egy olyan elemet, amely értéke 50.")
else:
    print("A lista nem tartalmaz, 50-es értékű elemet.")

#minden elem teljesíti
#döntse el, hogy az adatok lista minden eleme kisebb mint 150.
mindenE_kisebb150 = True
for item in adatok:
    if not (item < 150):
        mindenE_kisebb150 = False
        break

if mindenE_kisebb150:
    print("A lista összes eleme kisebb mint 150.")
else:
    print("A list nem összes eleme kisebb mint 150.")

#kiválasztás tétele
#!!!!!!!!!!!!!!!!!!!!!!!! előfordul, hogy amit szeretnénk kiválasztani, olyan nincs is.
#Határozza meg a lista, 50-es érték elemének.
elem50 = None
for item in adatok:
    if item == 50:
        elem50 = item
        break
if elem50 != None:
    print(f"Van megfelelő elem, amely értéke: {elem50}")
else:
    print("Nincs ilyen elem.")

#keresés tétele
#!!!!!!!!!!! ha nincs megfelelő elem akkor nincs is indexe.
#határozza meg, az adatok listában, a százas értékű elem helyét, előfordulását-index
index100 = None
for i in range(len(adatok)):
    if adatok[i] == 100:
        index100 = i
        break
if index100 != None:
    print(f"Van megfelelő elem (100-as értékű), amely indexje: {index100}")
else:
    print("nincs megfelelő elem")

#buborékos rendezés
#rendezzük az adatok listát növekvő sorrendbe.
for i in range(len(adatok)-1, 0, -1):
    for j in range(i):
        if adatok[j] > adatok[j+1]:
            adatok[j], adatok[j+1] = adatok[j], adatok[j+1]

print(adatok)