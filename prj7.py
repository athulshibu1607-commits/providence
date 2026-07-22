
a = int(input("enter the number of elements that is required to be inputed :"))
b = []
for i in range (a):
    numbers = int(input("enter a number:"))
    b.append(numbers)


even_numbers = []
odd_numbers = []

for num in b:
    if num%2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)
print(b)
print("even numbers are :",even_numbers)
print("odd numbers are :",odd_numbers )