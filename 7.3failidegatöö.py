def kirjuta_failisse(failinimi:str,loend:list):
    while True:
        reziim=input("sisesta fauli avamise reziim (w - kirjutamine, a - lisamine): ")
        if reziim not in ["w", "a"]:
            print("vale reziim! proovi uuesti. ")
        else:
                break
    for i in range(5):
        element=input("sisesta info,mida failisi lisada:")
        loend.append(element)
    with open(failinimi+"txt", reziim,encoding="utf-8") as f:
        for rida in loend:
            f.write(rida+"\n")
def loe_failist(failinimi:str)->list:
    """
    loeb faili read ja tagastab need listina
    """
    loend=[]
    with open(failinimi+".txt","r", encoding="utf-8") as f:
        for rida in f:
            loend.append(rida.strip())
    return loend

loend=["rida 1", "rida 2"]
failinimi=input("sisesta faili nimi (ilma laiendita): ")
kirjuta_failisse(failinimi, loend)
sisu=loe_failist(failinimi)
print("faili sisu: ")
# 1. variant 
print(sisu)
# 2. variant
for rida in sisu:
    print(rida)
    #1