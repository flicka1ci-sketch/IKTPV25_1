import random
valikud = ["kivi", "paber", "käärid"]
kasutaja_kaigud = []
arvuti_kaigud = []
tulemused = []
kasutaja_punktid = 0
arvuti_punktid = 0

while True:
    arvuti_valik = random.choice(valikud)
    kasutaja_valik = input("Vali kivi, paber või käärid: ").lower()

    if kasutaja_valik not in valikud:
        print("Viga! Palun vali kivi, paber või käärid.")
        continue

    print(f"Arvuti valis: {arvuti_valik}")
    print(f"Sina valisid: {kasutaja_valik}")

    kasutaja_kaigud.append(kasutaja_valik)
    arvuti_kaigud.append(arvuti_valik)

    if kasutaja_valik == arvuti_valik:
        print("Viik!")
        tulemused.append("Viik")
    elif (kasutaja_valik == "kivi" and arvuti_valik == "käärid") or \
         (kasutaja_valik == "paber" and arvuti_valik == "kivi") or \
         (kasutaja_valik == "käärid" and arvuti_valik == "paber"):
        print("Sina võitsid!")
        kasutaja_punktid += 1
        tulemused.append("Võit")
    else:
        print("Arvuti võitis!")
        arvuti_punktid += 1
        tulemused.append("Kaotus")

    print(f"Skoor - Sina: {kasutaja_punktid}, Arvuti: {arvuti_punktid}")

    jätka = input("Kas soovid veel mängida? (jah/ei): ").lower()
    if jätka == "ei":
        print("Mäng lõppes!")
        print("Mängu kokkuvõte:")
        for i in range(len(kasutaja_kaigud)):
            print(f"Ring {i+1}: Sina - {kasutaja_kaigud[i]}, Arvuti - {arvuti_kaigud[i]}, Tulemus - {tulemused[i]}")
        break
