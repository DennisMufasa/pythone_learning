name = input("Enter your name")
weight = input("enter your weight in kgs")
height= input("enter your height in meters")

weight = float(weight)
height = float(height)

bmi = (weight/(height*height))

print(bmi)

if bmi < 15:
    print(name, " is very Severly underweight. with a bmi of", bmi)
elif bmi >= 15 and bmi <16:
    print(name, " is Severly underweight. with a bmi of", bmi)
elif bmi >=16 and bmi < 18.5:
    print(name, " is underweight. with a bmi of", bmi)
elif bmi >=18.5 and bmi < 24.99:
    print(name, " is normal. with a bmi of", bmi)
elif bmi >=24.99 and bmi < 30:
    print(name, " is overweight. with a bmi of", bmi)
elif bmi >=30 and bmi < 34.99:
    print(name, " is obese class I. with a bmi of", bmi)
elif bmi >=34.99 and bmi< 39.99:
    print(name, " is obese class II. with a bmi of", bmi)
else : print(name, " is obese class III. with a bmi of", bmi)