"""
Walrus Operator in Python  (:=)
    It allows you to assign a value to a variable within an expression
"""
a=False
print(a:=True)
print("---------------------")
numbers=[1,2,3,4,5]
while(n:=len(numbers)>0):
    numbers.pop()
    print(numbers)
print("---------------------")
foods=[]
while True:
    food=input("What food do you like?: ")
    if food =="Quite":
        break
    foods.append(food)

print(foods)

#Using Walrus Operator
foods=list()
while(food:=input("What food do you like?: ")!="quite"):
    foods.append(food)
print(foods)
