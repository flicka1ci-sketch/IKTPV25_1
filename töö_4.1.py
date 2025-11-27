# esimene ülesanne
# Sisesta sõna või lause.
# Loenda:
#     mitu täishäälikut 
#     mitu kaashäälikut 
#     kui sisestati lause – loenda ka tühikud ja kirjavahemärgid 
# from re import M
# import string
# t=['a','e','i','o','u','õ','ä','ö','ü']
# k=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','š','z','ž','t','v','w','x','y']
# sõna_lause=input("Sisesta sõna või lause: ").lower()
# täishäälikud=0
# kaashäälikud=0
# märgid=0
# for taht in sõna_lause:
#     if char in t:
#         täishäälikud+=1
#     elif char in k:
#         kaashäälikud+=1
#     elif char in M
#     märgid+=1
# print(f"Sõnas/lausees on {täishäälikud} täishäälikut, {kaashäälikud} kaashäälikut ja {märgid} märki.")




# teine ülesanne 
# Küsi kasutajalt viis nime.
# Salvesta nimed loendisse ja kuva need tähestikulises järjekorras.
# Kuva viimane lisatud nimi.
# Lisa võimalus nimekirjas olevaid nimesid muuta
# names = []
# for i in range(5):
#     ask = input(f"Sisesta {i+1}. nimi: ")
#     names.append(ask)
# print(names)
# viimane_nimi = names[-1]
# names.sort()
# print(names)
# print(viimane_nimi)
# muuda = input("Kas soovid mõnda nime muuta? (jah/ei): ").lower()
# if muuda == "jah":
#     vana_nimi = input("Sisesta vana nimi: ")
#     if vana_nimi in names:
#         uus_nimi = input("Sisesta uus nimi: ")
#         find = names.index(vana_nimi)
#         names[find] = uus_nimi
#         print(names)

# kolmas ülesanne
#Koosta vanuste loend ja leia:
# suurim
# väikseim
# kogusumma
# keskmine

# vanused = [25, 32, 45, 65, 22, 16, 54, 52, 98]
# suurim = max(vanused)
# väikseim = min(vanused)
# kogusumma = sum(vanused)
# keskmine = kogusumma / len(vanused)
# print(f"Suurim vanus on {suurim}")
# print(f"Väikseim vanus on {väikseim}")
# print(f"Kogusumma on {kogusumma}")
# print(f"Keskmine vanus on {keskmine:.2f}")


# neljas ülesanne
# Kasuta loendis olevaid arve ja joonista tärnidega diagramm.

# ******************
# *******************
# ********************************
# *****************************************
# ****************************************************
# ************

# arvud = [10, 45, 9, 15, 3, 6, 5]
# for arv in arvud:
# print('*' * arv)

#viies ülesanne
#Postiindeks 📮
# Eestis koosnevad postiindeksid 5 numbrist, millest esimene number tähistab maakonda:
# 1 – Tallinn 
# 2 – Narva, Narva-Jõesuu 
# 3 – Kohtla-Järve 
# 4 – Ida-Virumaa, Lääne-Virumaa, Jõgevamaa 
# 5 – Tartu linn 
# 6 – Tartumaa, Põlvamaa, Võrumaa, Valgamaa 
# 7 – Viljandimaa, Järvamaa, Harjumaa, Raplamaa 
# 8 – Pärnumaa 
# 9 – Läänemaa, Hiiumaa, Saaremaa
# Kontrolli kasutaja sisestatud postiindeksit.
# Näita, millisesse maakonda see kuulub.
# Erireegel:
# Tallinn, Narva, Kohtla-Järve → „Mine merre!”
# Teised → „Mine metsa!”
# indexid=[tallinn, narva, kohtla_järve, ida_virumaa, tartu, tartumaa, viljandimaa, pärnumaa, läänemaa]
# while True: 
#     try:
#         index=int(input("Sisesta oma postiindeks (5-kolaine arv): "))
#         if 10000 <= index <= 99999: #len(str(index))==5
#             break
#         else:
#             print("Postiindeks peab olema viie numbri pikkune.")
#     except:
#         print("viigane andmetüüp")
#         index_list=list(index) #index=37521 > list("37521") = ['3','7','5','2','1'])
#         n1=int(index_list[0])#esimene number > "3" > int("3")=3
#         print(f"sinu postiindeks {index} kuulud piirkonda {indexid[n1-1]}")")
#         if n1 in [0,1,2,7]:
#             print("Mine merre!")
#         else:
#             print("Mine metsa!")

# kuues ülesanne
# from math import e
# from random import *
# Vahetus ↔️
# Vaheta loendis esimene ja viimane element, teine ja eelviimane jne.
# Küsi kasutajalt, mitu paari vahetada. loendis on min 2 elem.
# loend_arvud=[]
# loend_tähed=[]
# loend_kääshäälikud=[]
# mitu = randint(2,20)
# for i in range(mitu):
#     loend_arvud.append(randint(0,100))
#     loend_tähed.append(chr(randint(65,90)))
#     loend_kääshäälikud.append(choice(['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','š','z','ž','t','v','w','x','y' ]))
# valik = input("Millist loendit soovid vahetada? 1-Arvud, 2-Tähed, 3-Kaashäälikud: ")
# if valik == "1":
#     loend = loend_arvud
#     print(loend)
#     paarid = input(f"Sisesta mitu paari soovid vahetada (max {len(loend)//2}): ")
#     print(loend)
# elif valik == "2": 
#     loend = loend_tähed
#     print(loend)
#     paarid = input(f"Sisesta mitu paari soovid vahetada (max {len(loend)//2}): ")
#     print(loend)
# elif valik == "3":
#     loend = loend_kääshäälikud
#     print(loend)            
#     paarid = input(f"Sisesta mitu paari soovid vahetada (max {len(loend)//2}): ")
#     print(loend)

    

# seitsmes ülesanne
# „Arvud“ 🤷‍♂️
# Leia loendi suurim arv, jaga see loendi pikkusega ja asenda see tulemusena.
# from random import * 

# loend_arvud = []
# mitu = randint(2,20)
# for i in range(mitu):
#     elem = randint(0,100)
#     loend_arvud.append(elem)
#     print(f"alguses loend: {loend_arvud} ")
# suurim = max(loend_arvud)
# kus_asub=loend_arvud.index(suurim)
# suurim_muudatud = suurim / mitu
# loend_arvud[kus_asub] = round(suurim_muudatud,2)
# print(f"muutmise järel: {loend_arvud} ")





# kaheksas ülesanne
# Sorteeri nimekiri numbreid absoluutväärtuse järgi
#kasvavalt ⬆️
#või kahanevalt ⬇️
# l = [-10, 5, -30, 15, 20, -25, 50, -2, 3, -70, 90]
# l.sort(key=abs)
# print(f"Absoluutväärtuse järgi kasvavalt sorteeritud nimekiri: {l}")
# l.sort(key=abs, reverse=True)
# print(f"Absoluutväärtuse järgi kahanevalt sorteeritud nimekiri: {l}")

# üheksas ülesanne
# Võrdse pikkusega sõned 🧱
# Muuda kõik sõned loendis sama pikkusega, täites lühemad alakriipsudega _.
# Järjekorda ei tohi muuta.
# On antud:
# ['tamm', 'taevas', 'elevant'] 
# ['a', 'aa', 'aaa', 'aaaa', 'aaaaa'] 
# ['qweasdqweas', 'q', 'rteww', 'ewqqqqq']
# Tulemus:
# ['tamm___', 'taevas_', 'elevant'] 
# ['a____', 'aa___', 'aaa__', 'aaaa_', 'aaaaa'] 
# ['qweasdqweas', 'q__________', 'rteww______', 'ewqqqqq____']

# sõned = ["circle", "square", "apple", "dog", "cat" ]
# max_pikkus = max(len(sõne) for sõne in sõned)
# uued_sõned = [sõne.ljust(max_pikkus, '_') for sõne in sõned]
# print(uued_sõned)

# Nime kontroll 👤
# Programm peab :
# kontrollima, et nimi sisaldab ainult tähti ✔️
# kuvama nimega tervituse (suur algustäht) 😊
# loendama tähti, täishäälikuid ja kaashäälikuid
# kuvama nime tähed tähestiku järjekorras (ilma kordusteta) 🔤
# nime = input("Sisesta oma nimi: ")
# if not nime.isalpha():
#     print("Nimi peab sisaldama ainult tähti.")
# else:
#     nime = nime.capitalize()
#     print(f"Tere, {nime}!")
#     tähed = len(nime)
#     täishäälikud = sum(1 for täht in nime.lower() if täht in 'aeiouõäöü')
#     kaashäälikud = sum(1 for täht in nime.lower() if täht in 'bcdfghjklmnpqrsštzžtvwxý')
#     print(f"Sinu nime pikkus on {tähed} tähemärki.")
#     print(f"Sinu nimes on {täishäälikud} täishäälikut ja {kaashäälikud} kaashäälikut.")
#     unikaalsed_tähed = sorted(set(nime.lower()))
#     print("Sinu nime tähed tähestiku järjekorras (ilma kordusteta):", ''.join(unikaalsed_tähed))


#Töötajate andmed 💼
# Leia antud andmete põhjal:
# suurima palgaga töötaja
# keskmine palk
# mitu teenib üle keskmise
# keskmine vanus gruppidel: ≤ keskmine ja > keskmine
# töötajad = [
#     {'nimi': 'Artjom', 'palk': 1500, 'vanus': 28},
#     {'nimi': 'Marina', 'palk': 1200, 'vanus': 34},
#     {'nimi': 'Petja', 'palk': 1800, 'vanus': 45},
#     {'nimi': 'Kati', 'palk': 1600, 'vanus': 29},
#     {'nimi': 'Jaan', 'palk': 1100, 'vanus': 18}
# ]
# suurim_palk = max(töötajad, key=lambda x: x['palk'])
# print(f"Suurima palgaga töötaja on {suurim_palk['nimi']} ") 
# keskmine_palk = sum(t['palk'] for t in töötajad) / len(töötajad)
# print(f"Keskmine palk on {keskmine_palk:.2f} ")
# üle_keskmise = sum(1 for t in töötajad if t['palk'] > keskmine_palk)
# print(f"Töötajaid, kes teenivad üle keskmise, on {üle_keskmise} ")
# vanused_keskmine = sum(t['vanus'] for t in töötajad) / len(töötajad)
# nooremad = [t['vanus'] for t in töötajad if t['palk'] <= keskmine_palk]
# vanemad = [t['vanus'] for t in töötajad if t['palk'] > keskmine_palk]
# keskmine_nooremad = sum(nooremad) / len(nooremad) if nooremad else 0
# keskmine_vanemad = sum(vanemad) / len(vanemad) if vanemad else 0
# print(f"Keskmine vanus töötajatel, kes on nooremad või võrdne keskmisega: {keskmine_nooremad:.2f} ")
# print(f"Keskmine vanus töötajatel, kes on vanemad kui keskmine: {keskmine_vanemad:.2f} ")



#Inglise tähestik 🔡
# Koosta:
# loend tähtedest ‘a’, ‘b’, ‘c’ ...
# loend: ‘a’, ‘bb’, ‘ccc’, ‘dddd’ ...

# tähed = [chr(96 + i) for i in range(1, 27)]

# Loend: 'a', 'bb', 'ccc', ...
# loend = [t * (i + 1) for i, t in enumerate(tähed)]
# print("Inglise tähestik:")
# print(tähed)
# print("\nLoend: 'a', 'bb', 'ccc', ...")
# print(loend)











        


