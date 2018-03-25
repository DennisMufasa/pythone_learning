class Person:
    def __init__(self,name,height,weight):
        self.name=name
        self.height=height
        self.weight=weight

    def bmi(self,height,weight):

        bmi=(weight/(height*height))

        if bmi < 15:
            print("Your bmi is very Severly underweight. with a bmi of", bmi)
        elif bmi >= 15 and bmi < 16:
            print("Your bmi is Severly underweight. with a bmi of", bmi)
        elif bmi >= 16 and bmi < 18.5:
            print("Your bmi is underweight. with a bmi of", bmi)
        elif bmi >= 18.5 and bmi < 24.99:
            print("Your bmi is normal. with a bmi of", bmi)
        elif bmi >= 24.99 and bmi < 30:
            print("Your bmi is overweight. with a bmi of", bmi)
        elif bmi >= 30 and bmi < 34.99:
            print("Your bmi is obese class I. with a bmi of", bmi)
        elif bmi >= 34.99 and bmi < 39.99:
            print( "Your bmi is obese class II. with a bmi of", bmi)
        else:
            print("Your bmi is obese class III. with a bmi of", bmi)

Person.bmi('Dennis',1.85,68)
Person.bmi('wanyama',1.89,75)