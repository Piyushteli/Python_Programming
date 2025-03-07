"""
Kauan Banega Crorepati
"""
questions=[["1)Who is the prime minister of India","Narendra Modi","Rahul Gandhi","Eknath Shinde","Sharad pawar",1],["2)What is the capital of Maharastra","Mumbai","pune","Banglore","Kolkata",1],["3)How many states in India",28,29,36,38,1],["4)Who is the prime minister of India","Narendra Modi","Rahul Gandhi","Eknath Shinde","Sharad pawar",1],["5)Who is the prime minister of India","Narendra Modi","Rahul Gandhi","Eknath Shinde","Sharad pawar",1],["Who is the prime minister of India","Narendra Modi","Rahul Gandhi","Eknath Shinde","Sharad pawar",1],["Who is the prime minister of India","Narendra Modi","Rahul Gandhi","Eknath Shinde","Sharad pawar",1],["Who is the prime minister of India","Narendra Modi","Rahul Gandhi","Eknath Shinde","Sharad pawar",1]]
level=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]

money=0
for i in range(0,len(questions)):
    question=questions[i]
    print(f"\n\n question for Rs.{level[i]}")
    print(f"{question[0]}")
    print(f"a.{question[1]}          b.{question[2]}")
    print(f"c.{question[3]}          d.{question[4]}")

    reply=int(input("Enter your answer (1-4) or 0 to quit:\n"))
    if reply==0:
        money=level[i-1]
        break
    if reply==1:
        print(f"Correct answer,You have won Rs.{level[i]}")

        if i==4:
            money=10000
        elif i==9:
            money=320000
        elif i==12:
            money=10000000
    else:
        print("Wrong answer!")
        break

print(f"Your take home money is {level[i-1]}")