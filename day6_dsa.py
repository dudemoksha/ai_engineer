def mat():
    a=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    sum1=0
    
    for i in range(len(a)):
        for j in range(len(a[i])):
            sum1+=a[j][i]
        print("Sum of" ,i+1," column elements:", sum1)
        sum1=0
mat()
def linear():
    a=[1,2,3,45,6]
    k=6
    for i in range(len(a)):
        if a[i]==k:
            print("Element found at index:", i)
            return
    print("Element not found")
linear()


def binary(a, k):
    l=0
    h=len(a)-1
    a.sort()
    while l<=h:
        m=(l+h)//2
        if a[m]==k:
            print("found at",m)
            return
        elif a[m]>k:
            h=m-1
        else:
            l=m+1
    print("no eleement detected")
binary(a=[81,29,93,42,25,66,7,81,19], k=19)
   


def max():
    a=[1,2,3,4,5,6,7,8,9,10,66,12,9897,3589767,24]
    b=0
    for i in a:
        if b<i:
            b=i
    print(b)
max()

def repeat_and_not_repeat():
    a=[1,2,3,4,5,6,67,3,2,1,2,3,4,43,2,2,1,2,3,4]
    b=[]
    c=[]
    for i in a:
        if i not in b and b.count(i)==0:
            b.append(i)
        if i in b and a.count(i)>1:
            if i not in c and c.count(i)==0:
                c.append(i)
    print(b,c)
repeat_and_not_repeat()
def countu():
    a=[1,2,3,4,4,4,4,5,87,6,2,2,3,4,4,6,4,7,6]
    b=list(set(a))
    for i in b:
        print(i,":",a.count(i))
countu()