# Exercise 3: Calculate the sum of all numbers from 1 to a given number

number = int(input("Enter the number: "))

sum = 0

for i in range(1, number+1):
    sum += i
print(sum)