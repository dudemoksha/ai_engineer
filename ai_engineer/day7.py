def word():
    a="this is the best lion in the world and it is having a baby lion with in it stomach and it has father lion and sister lion"
    b=a.split()
    c=set(b)
    for i in c:
        print(i,":",b.count(i))
word()

def  special():
    a="this is me and mt bro*&^%$!@#$%^&*()_+{}|:<>?~`hi bro\n/n\t"
    for i in a:
        if i.isalnum() or i.isspace():
            print(i, end=" ")
special()
        
def zop():
    a=[1,2,3,4,5]
    b=["a","b","c","d","e"]
    c=[]
    for i,j in zip(a,b):print(i,j)
zop()
def sum():
    a="moksha sai is the name of a goat who sacrificed his life for the sake of his family he left all his goals and dreams and went to the forest to live a life of a goat he is a vegetarian goat and he loves to eat grass and leaves"
    b=a.split()
    c=""
    for i in b:
        if len(i)>len(c):
            c=i
    print("Longest word:", c)
sum()
def all_sub_strings():
    a="moksha"
    for i in range(len(a)):
        for j in range(i+1, len(a)+1):
            print(a[i:j])
all_sub_strings()

def cii():
    row=int(input("Enter a number: "))
    col=int(input("Enter a number: "))
    c=[]
    for i in range(row):
        j=list(map(int,input("Enter a number of rows : ").split()))
        c.append(j)
    print(c)
def mat():
    c=0
    a=[[1,2,3],[4,5,6],[7,8,9]]
    for i in range(len(a)):
        print("row",i+1)
        for j in range(len(a[i])):
            if c<3:
                print(a[i][j], end=" ")
                c+=1
        print("\n")
        c=0
    for i in range(len(a)):
        print("column",i+1)
        for j in range(len(a[i])):
            if c<3:
                print(a[j][i], end=" ")
                c+=1
        print("\n")
        c=0
    for i in range(len(a)):
        for j in range(len(a[i])):
            if i==j:
                print("Diagonal",i+1,"element:", a[i][len(a)-i-1])
mat()
def sumof():
    sumu,c=0,0
    a=[[1,2,3],[4,5,6],[7,8,9]]
    for i in range(len(a)):
        print("row",i+1)
        for j in range(len(a[i])):
            if c<3:
                sumu+=a[i][j]
                c+=1
        print("Sum of row", i+1, "elements:", sumu)
        sumu=0
        print("\n")
        c=0
    for i in range(len(a)):
        print("column",i+1)
        for j in range(len(a[i])):
            if c<3:
                sumu+=a[j][i]
                c+=1
        print("Sum of column", i+1, "elements:", sumu)
        sumu=0
        print("\n")
        c=0
sumof()
def trans():
    a=[[1,2,3],[4,5,6],[7,8,9]]
    b=[]
    for i in range(len(a)):
        c=[]
        for j in range(len(a[i])):
            c.append(a[j][i])
        b.append(c)
        print(c)
trans() 
