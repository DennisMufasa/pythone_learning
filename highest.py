scores=[{"name":"John","math":77,"eng":65},{"name":"Dennis","math":80,"eng":85},{"name":"Evi","math":75,"eng":65},{"name":"Felistus","math":85,"eng":52}]
name=""
marks=0

for score in scores:

    math = score["math"]
    eng = score["eng"]
    total=math+eng

    if total>marks:
        marks=total
        name=score["name"]

print(name,marks)