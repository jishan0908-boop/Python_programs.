# WAP to accept a number "n" to compute the following
# a. Cheeckif 'n' is prime
def prime(n):
    flag=0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            flag=1
            break
        else:
            flag=0
    if flag==0:
        print("The number is prime")

    else:
        print("The number is not the prime number")
n=int(input("enter the number to check the number is prime or not"))
prime(n)