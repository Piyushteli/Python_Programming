"""
Map(),filter(),and sorted() function in python
"""
# Map
Marks=[70,75,60,85,95,91,90,80]
def grade(Marks):
    if Marks>=90 :
        return "A"
    elif Marks>=80 or Marks<90:
        return "B"
    elif Marks>=70 or Marks<80:
        return "C"
    elif Marks>=60 or Marks<70:
        return "D"
    else:
        return "fail"

grades=map(grade,Marks)

print("Exam Score:",Marks)
print("Grades:",list(grades))
print("---------------------------------------")

Mark=[54,90,89,87,76,67,89,97,90,85,35,48,59]
def failing(Mark):
    return Mark<60

print("Marks: ",Mark)
Mark=filter(failing,Mark)

print("failing Marks: ",list(Mark))
print("---------------------------------------")

city=["jaipur","Kota","chandigarh","delhi","Muzaffarpur"]

def length(city):
    return len(city)

sort=sorted(city,key=length)
print("sorted list is ",sort)
print("--------------------------------------")

#use map()function with lambda function
numbers=[1,2,3,4,5,6,7,8,9,10]
doubled=map(lambda x:x*2,numbers)
print(list(doubled))
print("--------------------------------------")


#use filter()function with lambda function
number=[1,2,3,4,5,6,7,8,9,10]
even=filter(lambda n:n%2==0,number)
print(list(even))
print("------------------------------------------")
#use sorted()function with lambda function
city=["jaipur","Kota","chandigarh","delhi","Muzaffarpur"]
sort=sorted(city,key=lambda x:len(x))
print(sort)
