# d. Calculate sum pf first 'n' natural number:
def sum(n):
    sum=0
    if n<=0:
        print("Not possible")
    else:
        for i in range(1,n+1):
            sum+=i
        print("sum is :", sum)

n=int(input("enter the number till which you want to get the sum : "))
sum(n)   