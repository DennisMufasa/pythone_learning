scores=[{"name":"John","math":77,"eng":65},{"name":"Dennis","math":80,"eng":85},{"name":"Evi","math":75,"eng":65},{"name":"Felistus","math":85,"eng":52}]

name=""
math=0
eng=0
total=0

for score in scores:
    name=score["name"]
    math=score["math"]
    eng=score["eng"]
    total=math+eng
    print("name:",name,"Maths:",math,"eng:",eng,'\n',"Total:",total)




