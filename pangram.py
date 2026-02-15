#pangram using list
import string 
sentence=input("please enter the sentence here").lower()
print(sentence)
alpha=[]
for i in sentence:
    print(i)
    if i.isalpha() and i not in alpha:
        alpha.append(i)

if len(alpha)==26:
    print("pangram")
else:
    print("not pangram")

alpha=set()
for i in sentence:
    print(i)
    if i.isalpha():
        alpha.add(i)

if len(alpha)==26:
    print("pangram")
else:
    print("not pangram")