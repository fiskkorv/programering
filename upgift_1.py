def division(nummer1,nummer2):
    if nummer2==0:
        print("försök inte")
        return
    else:
        return nummer1/nummer2

nummer2=int(input("skriv in hur många personer "))
nummer1=int(input("skriv in hur många äpplen "))
resultat=division(nummer1,nummer2)
print("resultatet är " + str(resultat))