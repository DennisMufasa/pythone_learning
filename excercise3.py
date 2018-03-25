items=[]
prices=[]
quants=[]
counter=1
while counter<=3:
    item=input("Enter the item")
    items.append(item)

    price=input("Enter items price")
    prices.append(price)

    quant=input("Enter item's quantity")
    quants.append(quant)

    counter+=1

count=0
while count< len(items):
    total=float(quants[count])*float(prices[count])

    print("Item:",items[count]," Cost:",prices[count]," Quantity",quants[count],'\n'" Total",total)

    count+=1


