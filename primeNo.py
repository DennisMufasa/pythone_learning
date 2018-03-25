primeNos=[]
for i in range(2,101):
    if all(i%p for p in primeNos):
        print(i)

        primeNos.append(i)
