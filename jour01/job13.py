numbers = []

for i in range(5):
    number = int(input("Enter an integer : "))
    numbers.append(number)

numbers.sort()

print("here are the numbers ordered from smallest to largest :")
for number in numbers:
    print(number)