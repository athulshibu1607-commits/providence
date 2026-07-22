m = int(input("enter m:"))
n = int(input("enter n:"))
even_squared = {i*i for i in range (m,n+1) if i%2==0}
print(even_squared)