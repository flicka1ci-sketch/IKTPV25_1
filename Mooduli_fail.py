#töö 5.1
#esimene ülesanne
# Kirjuta funktsioon arithmetic, mis võtab 3 argumenti: esimesed 2 on arvud,
# kolmas on tehe, mis nende vahel tuleb teha. 
# Kui kolmas argument on +, liida need; kui -, lahuta; 
# kui *, korruta; kui /, jaga (esimene teisega).
# Kõigil muudel juhtudel tagasta string "Tundmatu tehe".
# def float_kontroll(sisend:str)->float:
# 	while True:
# 		try:
# 			arv=float(sisend)
# 			return arv
# 		except ValueError:
# 			sisend=input("palun sisesta arv: ")
			





#1

# def arithmetic(a:float,b:float,tehe:str)->any:
# 	"""lihtne kalkulaator:
# 	+ - liitmine
# 	- - lahutamine
# 	/ - jagamine 
# 	Muul juhul tagastab ""tundmatu tehe" 
# 	:param float a: esimene arv
# 	:param float b: teine arv
# 	:param str tege: tehe mis tuleb teha
# 	:return/rtype: tehte tulemus float või str
# 	"""
# 	if tehe in ["+","-","*","/"]:
# 		if tehe=="/" and b==0:
# 			return "nulliga jagamine pole lubatud"
# 		else:
# 			vastus=eval(f"{a}{tehe}{b}") #tehe teostamine eval funktsiooniga
# 	else: 
# 		vastus="tudmatu tehe"

# 	return vastus


#2
#Kirjuta funktsioon is_year_leap, mis võtab ühe argumendi — aasta, 
#ja tagastab True, kui aasta on liigaasta, ja False muul juhul.
# def is_year_leap(aasta:int) ->bool: # true or false
# 	if (aasta % 4 == 0 and aasta % 100 != 0):
# 		return True 
# 	else:
# 		return False
# def int_kontroll(sisend:str)->int:
# 	while True:
# 		try:
# 			arv=int(sisend)
# 			return arv
# 		except ValueError:
# 			sisend=input("palun sisesta arv: ")

#3
# def square(külg:float)->any:
# 	"""arvutab ruudu ümbermõõdu, pindala ja diagonaali 
# 	:param float külg: ruudu külje pikkus
# 	:return/rtype:ümbermõõt, pindala, diagonaal
# 	"""
# 	ümbermõõt=4*külg
# 	pindala=külg**2 #või külg
# 	diagonaal=külg**0,5*2
# 	return ümbermõõt,pindala,diagonaal
# def float_kontroll(sisend:str)->int:
# 	while True:
# 		try:
# 			arv=int(sisend)
# 			return arv
# 		except ValueError:
# 			sisend=input("palun sisesta arv: ")



#4 
#Kirjuta funktsioon season,
# mis võtab ühe argumendi — kuu number (1 kuni 12),
#  ja tagastab selle kuu vastava aastaaja (talv, kevad, suvi või sügis).
# def season(month: int) -> str:
#     if month in (12, 1, 2):
#         return "talv"
#     elif month in (3, 4, 5):
#         return "kevad"
#     elif month in (6, 7, 8):
#         return "suvi"
#     elif month in (9, 10, 11):
#         return "sügis"
#     else:
#         return "vigane kuu"
# def int_kontroll(sisend:str)->int:
# 	while True:
# 		try:
# 			arv=int(sisend)
# 			return arv
# 		except ValueError:
# 			sisend=input("palun sisesta arv: ")

#5 
#Kasutaja teeb hoiuse summas a eurot years aastaks 10% aastaintressiga 
#(igal aastal suureneb hoiusumma 10%, ka intressile arvestatakse järgmise aasta intress).
#kirjuta funktsioon bank, mis võtab argumendid a ja years, ning tagastab lõppsumma kasutaja kontol.

def bank(a:float,years:int)->float:
	""" arvutab lõppusumma koos intressiga
	:param float a: algsumma
	:param int years:aastate arv
	:return/rtype: lõppsumma float
	"""
	intress=0,1 # see on 10%
	for i in range(years):
		a+=a*intress
	return a 
#6