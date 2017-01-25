#Git forritun py
#Kolbeinn

#Dæmi 1:
tala1 = int(input("Sláðu inn tölu: "))
tala2 = int(input("Sláðu inn tölu: "))
summa = tala1 + tala2
margf = tala1 * tala2
print(tala1,"+",tala2,"=",summa)
print(tala1,"*",tala2,"=",margf)


#Dæmi 2:
fNafn = input("Fornafn? ")
eNafn = input("Eftirnafn? ")
print("Halló",fNafn,eNafn)

#Dæmi 3:
texti=input("Sláðu inn texta: ")
hastafur=0
lagstafur=0
for e in texti:
    if e.isalpha():
        if e.isupper():
            hastafur=hastafur+1
        if not e.isupper():
            lagstafur=lagstafur+1
print("Í þessum texta eru",hastafur,"hástafir og",lagstafur,"lágstafir")