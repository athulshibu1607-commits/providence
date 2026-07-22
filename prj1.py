n = int(input("enter the number of elements needed :"))
s = []
for i in range [n]:
    a = input("enter a character:")
    b = input("enter a number :")
    s.append((a,b))
print("the elements entered are :")
print(s)
s.sort(key=lambda x:x[1])
print("the sorted elements are :")
print(s)