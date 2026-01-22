#1.  Kirjuta programm, mis küsib kasutaja nime ja vanust ning kuvab selle ekraanile sõnumina:
# while True:
#     nimi = input("Sisesta oma nimi: ").strip()
#     if nimi.isalpha():
#         break
#     else:
#         print("Palun sisesta ainult tähed")
# while True:
#     vanus = input("Sisesta oma vanus: ").strip()
#     if vanus.isdigit():
#         vanus = int(vanus)
#         break
#     else:
#         print("Palun sisesta vanus numbrina")

# print(f"Tere {nimi}, sinu vanus on {vanus} aastat.")

#2. Küsi kasutaja nimi. Kui nimi on tühi või sisaldab numbreid, küsi uuesti
#Väljasta tervitus: "Tere, [nimi]!"
# while True:
#     nimi = input("Sisesta oma nimi: ").strip()
#     if nimi.isalpha():
#         print(f"Tere, {nimi}!")
#         break
#     else:
#         print("Palun sisesta ainult tähed")
#3. Küsi kasutaja vanus. Kui vanus ei ole positiivne täisarv, küsi uuesti
# while True:
#     vanus = input("Sisesta oma vanus: ").strip()
#     if vanus.isdigit() and int(vanus) > 0:
#         vanus = int(vanus)
#         break
#     else:
#         print("Palun sisesta positiivne täisarv")