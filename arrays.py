scores=[77,45,63,45,96,75,85,90,14]

print(scores[0])
print(scores[0:3])
x=input("Enter your score: ")
scores.append(x)

print("length is ",len(scores))

for score in scores:
    print(score)

scores.pop(3)

print(scores)