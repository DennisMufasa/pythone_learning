name = input("Enter your name")
score = input("Enter student score")

score=int(score)

if score < 40:
    print(name, "scored grade E")
elif score >= 40 and score<50:
    print(name, "Scored grade D")
elif score >= 50 and score<60:
    print(name, "scored grade C")
elif score >= 60 and score<70:
    print(name, "scored grade B")
else:
    print(name, "scored grade A")