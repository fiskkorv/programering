def division(äpplen, personer):
    if personer==0:
        print("försök inte")
        return
    else:
        return int(äpplen/personer)

def dela_frukter(äpplen, personer):
    äpplen_per_person = division(äpplen, personer)
    äpplen_kvar = äpplen % personer
    print("äpplen per person " + str(äpplen_per_person))
    print("äpplen kvar " + str(äpplen_kvar))


personer=int(input("skriv in hur många personer "))
äpplen=int(input("skriv in hur många äpplen "))

dela_frukter(äpplen, personer)