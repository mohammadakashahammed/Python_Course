# Exercise 4: Write a program to print multiplication table of a given number


number = int(input("Enter the number: "))

for i in range(1, 11):
    x = number * i
    print(number,'*',i,'=', x)