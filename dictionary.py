scores=[{"names":"John","math":77,"eng":65},{"names":"Dennis","math":80,"eng":85},{"name":"Evi","math":75,"eng":65},{"name":"Felistus","math":85,"eng":52}]

total=0

for score in scores:
    print(score["math"])

    total+=score["math"]

average=total/len(scores)
print(average)


