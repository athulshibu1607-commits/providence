l = []
a = int (input("enter number of elements to be added in the list:"))
for i in range(a):
    b = int(input("enter number:"))
    l.append(b)
uniques_set = set(l)
print(uniques_set)