#prvi

ulaz = int(input("Unesi temepratura"))

if(ulaz > 0 and  ulaz < 100):
    print("tecno")

elif (ulaz <= 0):
    print("cvrsto")

else:
    print("gasovito")


#drugi 

#treci

def brojCifara(broj):

    c = 0

    while(broj > 1):
        broj /= 10
        c = c+1

    return c

def isNarcissistic(broj):

    sum = 0
    bc = brojCifara(broj)
    while(broj > 0):
        cifra = broj%10
        broj //= 10
        sum += (cifra**bc)

    return sum



broj = int(input("Unesi broj: "))

if broj == isNarcissistic(broj):
    print("DA")
else:
    print("NE")


#cetvrti

def resenje(ulaz, razbijac):

    
    duzina = razbijac

    rj = []
    rijec= ""
    i = 0

    for i in range(len(ulaz)):
        if(i < razbijac):
            rijec += ulaz[i]
        else:
            rj.append(rijec)
            rijec = ""
            razbijac += duzina

    print(rj)


resenje("danas polazemo test", 5)
        
    
    
     
    