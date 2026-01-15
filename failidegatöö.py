import os
import glob


def otsi_faile_laiendi_jargi():
    laiend = input("Sisesta faililaiend (nt txt või .txt): ").strip()

    if not laiend.startswith("."):
        laiend = "." + laiend

    failid = glob.glob(f"*{laiend}")

    if not failid:
        print("Faile ei leitud.")
    else:
        print("\nLeitud failid:")
        for fail in failid:
            print("-", fail)


def analuusi_fail():
    failitee = input("Sisesta failinimi koos laiendiga (nt test.py): ").strip()

    ridade_koguarv = 0
    tyhjade_ridade_arv = 0
    todo_esinemised = 0
    fixme_esinemised = 0

    try:
        with open(failitee, "r", encoding="utf-8", errors="ignore") as f:
            for rida in f:
                ridade_koguarv += 1

                if rida.strip() == "":
                    tyhjade_ridade_arv += 1

                rida_upper = rida.upper()
                todo_esinemised += rida_upper.count("TODO")
                fixme_esinemised += rida_upper.count("FIXME")

    except FileNotFoundError:
        print(f"Faili '{failitee}' ei leitud.")
        return

    print("\n--- FAILI ANALÜÜSI TULEMUS ---")
    print(f"Ridade koguarv: {ridade_koguarv}")
    print(f"Tühjade ridade arv: {tyhjade_ridade_arv}")
    print(f"TODO esinemisi: {todo_esinemised}")
    print(f"FIXME esinemisi: {fixme_esinemised}")


def loo_raporti_kataloog():
    nimi = "Analyysi_Raportid"

    if not os.path.exists(nimi):
        os.mkdir(nimi)
        print("Raporti kataloog loodi.")
    else:
        print("Raporti kataloog on juba olemas.")


def otsi_faile_algustahega():
    taht = input("Sisesta faili algustäht: ").strip()

    if not taht:
        print("Algustäht ei tohi olla tühi.")
        return

    failid = glob.glob(f"{taht}*.*")

    if not failid:
        print("Faile ei leitud.")
    else:
        print("\nLeitud failid:")
        for fail in failid:
            print("-", fail)


def otsi_faili(otsingu_tee="."):
    faili_nimi = input("Sisesta otsitava faili nimi (nt minu_fail.txt): ").strip()

    for juur, kaustad, failid in os.walk(otsingu_tee):
        if faili_nimi in failid:
            print("Fail leitud:")
            print(os.path.join(juur, faili_nimi))
            return

    print("Faili ei leitud.")
