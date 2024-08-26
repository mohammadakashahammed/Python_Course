a = 10
b = 0

try:
    result = a / b
except ZeroDivisionError:
    print("Sorry ! You are dividing by zero ")
else:
    print("Yeah ! Your answer is :", result)

finally:
    print('This is always executed')