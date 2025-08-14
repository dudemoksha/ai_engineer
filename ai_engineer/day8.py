from collections import Counter
def uni():
    a={1, 2, 3, 4, 5}
    b={4, 5, 6, 7, 8}
    c=a.update(b)
    print("Union of sets:", c)
uni()
def unit ():
    text = "moksha sai bhai"
    freq = {}
    for char in text:
        if char != " ":
            freq[char] = freq.get(char,0)+1
    print(freq)
unit()
def fre():
    a="this is a heros story whose name is moksha sai bhai and he is a good person  and he is a good person what not he is everything and the god himself is moksha sai bhai eyuu moksha sai bhai eyuu moksha sai bhai"
    b=set(a.split())
    for i in b:
        print(i, ":", a.count(i))
fre()
def count():
    a={
        "name":"hero",
        "age": 25, 
        "city":"hyderabad",
    }
    b={}
    for key, value in a.items():
        b[value]=key
    print(b)
count()
def freequ():
    a=["moksha", "sai", "bhai", "moksha", "sai", "bhai", "moksha", "sai", "bhai","bhai"]
    b=Counter(a)
    c=b.most_common(1)[0]
    print(c)
freequ()
def li():
    a=["moksha", "sai", "bhai", "moksha", "sai", "bhai", "moksha", "sai", "bhai","bhai"]
    
    c={}
    for i in a:
        b=i[0]
        if b not in c:
            c[b]=[]
        c[b].append(i)
    print(c)
li()
def word():
    a={"moksha": 1, "bhai": 2, "sai": 3}
    b={"moksha": 1, "sai": 2, "bhai": 3, "hero": 4} 
    print(Counter(a) + Counter(b))
word()
def sort():
    a=[1,2,7,4,5,6,3]
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    print("Sorted list:", a)
sort()
def sort1():
    a=[1,2,7,8,4,5,6,3]
    for i in range(1,len(a)):
        x=a[i]
        j=i-1
        while j>=0 and x<a[j]:
            a[j+1]=a[j]
            j-=1  
        a[j+1]=x
    print("Sorted list:", a)
sort1()
    

            



    
