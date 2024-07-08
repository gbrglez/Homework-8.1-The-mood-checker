

mood = input("Pozdravljen! Kako se počutiš? ")
kontrola = True

while kontrola:

    if mood == "dobro":
        print("Super, kar tako naprej!")
        kontrola = False
    elif mood == "živčno":
        print("Saj bo, trikrat globoko vdihni")
        kontrola = False
    elif mood == "žalostno":
        kontrola = False
        print("Pomisli na lepe trenutke :)")
    elif mood == "sproščeno":
        kontrola = False
        print("Če tako, greva pa na pivo. Jaz častim!")
    else:
        print("Nisem te razmel.")
        kontrola = True
        mood = input("Poskusi z dobro, žalostno, živčno ali sproščeno:")
