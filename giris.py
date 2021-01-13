import json
import datetime
import os

if os.name == "nt":  # Windows
    os.system("cls")
elif os.name == "posix":  # Linux
    os.system("clear")

tarihsaat = datetime.datetime.now()
kayitSaat = str(tarihsaat.strftime("%x")) + " " + str(tarihsaat.strftime("%X"))

while True:
    database = open(
        "alldata.json",
    )
    # Writen by Mert Şişmanoğlu
    data = json.load(database)
    if len(data["allusers"]) == 0:
        print("Kullanıcı Girişi")
        print("Kayıtlı kimse bulunmuyor yeni bir kullanıcı oluşturulacak.")
        newusername = input("Yeni kullanıcı adınızı girin: ")
        newpassword = input("Yeni şifrenizi girin: ")
        newdata = {}
        newdata["allusers"] = {}
        # Writen by Mert Şişmanoğlu
        newdata["allusers"].update(
            {
                newusername: {
                    "password": newpassword,
                    "roles": ["admin"],
                    "registerDate": kayitSaat,
                }
            }
        )
        with open("alldata.json", "w") as outfile:
            json.dump(newdata, outfile)
        print(
            f"{newusername} adıyla giriş yaptınız.\nArtık bu programın tüm kontrolü size ait."
        )
        # Writen by Mert Şişmanoğlu
        break
    ad = input("Kullanıcı Adı: ")
    parola = input("Parola: ")
    if ad in data["allusers"]:
        kullaniciSifresi = data["allusers"][ad]["password"]
        # Writen by Mert Şişmanoğlu
        if parola == kullaniciSifresi:
            print(f"{ad} Olarak giriş yapıldı")
            database.close()
            # Kullanıcı giriş yapınca çalışacak kodlar
            break
        else:
            print("Erişim Reddedildi")
            # Yanlış şifre girilince çalışacak kodlar

    else:
        print("Erişim Reddedildi")
        # Kayıtlı olmayan kullanıcı adı girilince çalışacak kodlar
    database.close()