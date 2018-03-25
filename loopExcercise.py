radiuscounter=1
rads = []
while radiuscounter<6:
    radius=input("Enter radius")
    radius=float(radius)

    rads.append(radius)

    radiuscounter+=1

for rad in rads:
    rad=float(rad)

    area=3.142*rad*rad

    print(area)



