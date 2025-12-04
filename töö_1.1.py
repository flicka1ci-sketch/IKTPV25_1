 

# 2.
#Mis tüüpi on järgnevad muutujad:

# a) vanus = 18
# b) eesnimi = "Jaak"
# c) pikkus = 1.65
# d) kas_käib_koolis = True
# Mis võimalus veel peale True oleks viimast muutujat väärtustada? Kuidas võiks nende muutujate väärtusi koodis kontrollida?
# kood tüüpide kontrollimiseks.
#vanus = 18 #int
#eesnimi = "Jaak" #str
#pikkus = 1.65 #float
#kas_käib_koolis = True #bool

#print(f"vanus {vanus} on: {type(vanus)}")
#print(f"eesnimi {eesnimi} on: {type(eesnimi)}")
#print(f"pikkus {pikkus} on: {type(pikkus)}")
#print(f"kas_käib_koolis {kas_käib_koolis} on: {type(kas_käib_koolis)}")

#1.Kirjuta enda esimene programm, mis väljastab käsureale teksti: “Tere, maailm!”. 
#Küsi kasutaja nimi ja muuda tekst, et ta näeks välja nii: “Tere, maailm! Tervitan sind Mati”, kui kasutaja nimi on Mati.
#Küsi kasutajalt sisend tema vanuse kohta ning väljasta see ekraanile:
#“Tere, maailm! Tervitan sind Mati! Sa oled N aastat vana.”



#Küsi kahe inimese nimed. Kui nimed koosnevad
# ainult tähedest siis teavita kasutajat,
# kas nad on täna pinginaabrid või ei mitte.
#nimi1 = input("Sisesta nimi=> ")
#nimi2 = input("Sisesta nimi=> ")
#if nimi1.isalpha():nimi2.isalpha():
   # if nimi1=="Sofia" and nimi2=="Kostja" or nimi1=="Sofia" and nimi2=="Kostja":
      #  print(f"{nimi1} ja {nimi2} on täna pinginaabrid")
#else:
    #print("Palus sisesta ainult tähed")


    
    #Küsi ristkülikukujulise toa seinte pikkused ning arvuta põranda pindala.
    # Küsi kasutajalt remondi tegemise soov, kui ta on positiivne, 
    # siis küsi kui palju maksab ruutmeeter ja leia põranda vahetamise hind

   # pikkus = int(input("Sisestage pikkus: "))
    #laius = int(input("Sisestage laius: "))
    #pindala = pikkus * laius 
    #print(f"pindala suurus on {pindala} ")
   #user = input("Kas soovite remondi teha? ").capitalize()
   # if user.isalpha() and user == "Jah":
      #  hind = float(input("Ruut meetri hind? "))
       # remondi_hind = hind * pindala 
       # print(f"remondi summa on {remondi_hind} ")
       # kes = input("Kes teeb remondi(ise/töötaja)? ").capitalize()
           # if kes.isalpha() and kes== "ise":
            #print("Siis summa on {remondi_hind} ") 





  #Küsi ristkülikukujulise toa seinte pikkused ning arvuta põranda pindala.
    # Küsi kasutajalt remondi tegemise soov, kui ta on positiivne, 
    # siis küsi kui palju maksab ruutmeeter ja leia põranda vahetamise hind

    #pikkus = int(input("Sisestage pikkus: "))
#laius = int(input("Sisestage laius: "))
#if pikkus>0 and laius>0:
                #pindala = pikkus * laius 
                #print(f"pindala suurus on {pindala} ")
                #user = input("Kas soovite remondi teha? ").capitalize()
                #if user.isalpha() and user == "Jah":
                  #  hind = float(input("Ruut meetri hind? "))
                   #remondi_hind = hind * pindala 
                    #print(f"remondi summa on {remondi_hind} ")
                    #kes = input("Kes teeb remondi(ise/töötaja)? ").capitalize()
                    #if kes.isalpha() and kes== "ise":
                        #print("Siis summa on {remondi_hind} ") 
#else:
  #  print("Arvud peavad olema suurem kui 0")


  
#Allahindus
# Leia 30% soodustusega hinna,
# kui alghind on suurem kui 700
#hind = input("hind: ")
#if hind.isdigit(): 
    #hind= float(hind)
    #if hind > 700: 
       # hind *= 0.7
       # print(f"soodus hind on {hind}")  
#else:
    #print("On vaja numbri sissestada")

#5 Temperatuur
#Küsi temperatuur ning teata, 
#kas see on üle 18 kraadi (soovitav toasoojus talvel)
#try:
#t=float(input("Siseta temperatuur: "))
#if t>0:
    #print("Soovitatav toasoojus talvel")
   # else:
      #  print("Võib olla jahe")
#except:
    #print("Palun sisesta temperatuur ujukomaarvuna!")

#6 Pikkus
#Küsi inimese pikkus ning teata
#, kas ta on lühike, keskmine või pikk 
#(piirid pane ise paika)
#pikkus = int(input("Sisesta oma pikkus sentimeetrites: "))
#if pikkus <160:
    #print("Sa oled lühike. ")
#elif 160 <0 and pikkus <=180:
    #print("Sul on keskmine pikkus. ")
#else:
    #print("Sa oled pikk.")

#7 Pikkus ja sugu
#Küsi inimeselt pikkus ja sugu ning teata,
# kas ta on lühike, keskmine või pikk 
# (mitu tingimusplokki võib olla üksteise sees).
# pikkus_input = input("Sisesta oma pikkus sentimeetrites: ")
# if not pikkus_input.isdigit():   
# else: 
# pikkus = int(pikkus_input)
# sugu= input("sisesta oma sugu (mees/naine): ")
# if not sugu.isalpha():
    #print("Palun sisesta ainult tähti sugu jaoks.")
    #elif sugu != "mees" and sugu != "naine":
    #print("Palun vali (mees/naine). ")
#else:
    #if sugu == "mees":
   # if pikkus <170:
        #print("Oled lühike mees.")
    #elif 170 <= pikkus <= 180: 
        #print("Oled keskmise pikkusega mees")
    #else: 
        #print("Oled pikk mees")
#else: 
#if: sugu== "naine":
    #if pikkus <160
    #print("oled lühike naine. ")
    #elif 160 <= pikkus <= 175:
#print("oled keskmise pikkusega naine. ")
#else:
#print("oled pikk naine")





#Ülesanne: Kehamassiindeksi (KMI) kalkulaator
#Koosta programm, mis täidab järgmised tegevused:

#print("Tere! Olen sinu uus sõber - Python!")
#nimi = input("Mis sinu nimi on?")
#print(f"{nimi}, oi kui ilus nimi!")
#try: 
    #soov=int(input(f"{nimi}! Kas leian Sinu keha indeksi? 0-ei 1-jah => "))
    #if soov==1:
        #print("Indeksi leidmine")
        #while True:
           # try:
                #pikkus = int(input("Sisesta oma pikkus sentimeetrites: "))
                #if 0 < pikkus <= 250:
                    #break
                #else:
                    #print("Pikkus peab olema vahemikus 0 kuni 250 cm! ")
            #except:
                #print("Vale pikkuse formaat! Palun sisesta täisarv")
        #while True:
            #try:
                #mass = float(input("Sisesta oma kehakaal kilogrammides: "))
                #if 0 < mass <= 200:
                    #break
                #else:
                    #print("Kaal peab olema vahemikus 0 kuni 200 kg!")
            #except:
                       #print("Vale kaalu formaat! Palun sisesta arv. ")

        #Arvuta kehamassiindeks (Kmi)
        #indeks = round(mass / (0.01 * pikkus) ** 2, 2)
        #print(f"{nimi}! Sinu keha indeks on: {indeks}")
        #if indeks < 16:
            #hinnang = "Tervisele ohtlik alakaal"
        #elif 16 <= indeks <= 19:
            #hinnang = "Alakaal"
        #elif 20 <= indeks <= 25:
           # hinnang = "Normaalkaal"
        #elif 26 <= indeks <= 30:
            #hinnang = "Ülekaal"
        #elif 31 <= indeks <= 35:
            #hinnang = "Rasvumine"
        #elif 36 <= indeks <= 40:
            #hinnang = "Tugev rasvumine"
        #else:
            #hinnang = "Tervisele ohtlik rasvumine"
        #print("Hinnang:", hinnang) 
    #elif soov==0:
        #print("Kahju! See on väga kasulik info")
    #else:
       # print("Vale valik. Saab valida ainult 1 või 0")
#except:
    #print("Vale soov!")
#print(f"Kohtumiseni, {nimi}, Igavesti Sinu, Python!")
# maja rabota 
