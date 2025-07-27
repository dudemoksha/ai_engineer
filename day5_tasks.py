def fibo(n):
    a,b=0,1
    for i in range(n+1):
        yield a
        a,b=b,a+b
print("Fibonacci Series:")
print(list(fibo(5)))

def prime(n):
    c=0
    if n<=1:
        print("give correct number")
    elif n==2:
        print("prime")
        return
    for i in range(2,n):
        if n%i!=0:
            c=0
        else:
            c+=1
            break
    if c==0:
        print("prime")  
    else:
        print("not prime")
print("Prime Check:")
prime(9)
def pal(s):
    if s==s[::-1]:
        print("palindrome")
    else:
        print("not palindrome") 
print("Palindrome Check:")
pal("madam") 


def sum(a):
    s=0
    while a>0:
        b=a%10
        a=a//10
        s+=b
    return s
print("Sum of Digits:")
print(sum(12345))
def table(n):
    for i in range(1,11):
        print(f"{n} x {i}={n*i}")
print("Multiplication Table:")
table(5)