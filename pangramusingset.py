sentence=input("type your sentence here").lower()
alpha=set()
for i in sentence:
    if i.isalpha():
        alpha.add(i)

if len(alpha)==26:
    print("its a pangram")
else:
    print("not a pangram")