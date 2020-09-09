from random import randint

def division(äpplen,personer):
    if personer==0:
        print("försök inte")
        return
    else:
        return int(äpplen/personer)

personer=int(randint(1, 10))
print("personer " + str(personer))
äpplen=int(randint(10, 50))
print("äpplen " + str(äpplen))
äpplen_per_person=division(äpplen,personer)
print("äpplen per person " + str(äpplen_per_person))

utdelade_äpplen = äpplen_per_person * personer
äpplen_kvar = äpplen - utdelade_äpplen

print("äpplen kvar " + str(äpplen_kvar))