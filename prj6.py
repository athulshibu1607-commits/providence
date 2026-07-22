numbers = int(input("enter a number:"))
even_numbers =[]
for num in range (0,numbers):
    if num%2==0:
        even_numbers.append(num)
print("even numbers are :",even_numbers)