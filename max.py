scores=[{"name":"John","math":77,"eng":65},{"name":"Dennis","math":80,"eng":85},{"name":"Evi","math":75,"eng":65},{"name":"Felistus","math":85,"eng":52}]

max=0
name=""

for score in scores:
    if score["math"]>max:
        max=score["math"]
        name=score["name"]

print(name,max)