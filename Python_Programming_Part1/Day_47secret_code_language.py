"""
Secret Code Language
"""

st=input("Enter the message: ")
words=st.split(" ")
Coding=input("1 for coding or 0 for Decoding: ")
Coding=True if Coding == "1" else False
print(Coding)

if Coding:
    nwords=[]
    for word in words:
        if (len(word)>=3):
            r1="dsf"
            r2="cdw"
            stnew=r1+word[1:]+word[0]+r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
        print(" ".join(nwords))



else:
    nwords=[]
    for word in words:
        if (len(word)>=3):
            stnew=word[3:-3]
            stnew=stnew[-1]+stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
        print(" ".join(nwords))