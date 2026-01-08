import email
import smtplib, ssl
from email.message import EmailMessage

def saada_email(saaja_email):
    print("Kirjuta oma sõnum või kood, lõpeta sõnaga END")
    rida_list = []
    while True:
        rida = input()
        if rida == "END":
            break
        rida_list.append(rida)
    kiri = "\n".join(rida_list)

    teema="test e-kiri pythonist"
    saatja_email="flicka1ci@gmail.com"
    parool=input("sisesta rakenduse parool: ")
    smtp_server="smtp.gmail.com"
    port=587 #465
    context=ssl.create_default_context()

    msg=EmailMessage()
    msg.set_content(kiri)
    msg["subject"]=teema
    msg["from"]=saatja_email
    msg["to"]=saaja_email

    with open(r"C:\Users\opilane\source\repos\PNG.PNG", "rb") as f: #png.png or any another name mida te meeldivad
        image_data = f.read()

    msg.add_attachment(
        image_data,
        maintype="image",
        subtype="png",
        filename="PNG.PNG"
    )

    try:
        with smtplib.SMTP(smtp_server,port) as server:
            server.starttls(context=context)
            server.login(saatja_email,parool)
            server.send_message(msg)
        print("e-kiri saadetud")
    except Exception as e:
        print(f"midagi läks valesti..{e}")

kellele=input("sisesta saaja e-posti address: ")
saada_email(kellele)
