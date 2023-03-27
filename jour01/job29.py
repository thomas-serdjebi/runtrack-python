import math

rates = []

for i in range(20):
    rate = int(input("Enter the rates of your twenty students : "))
    if rate >= 40 :
        rate.append(rates)
    elif rate % 5 >= 3:
        arroundedRate = math.ceil(rate/5)*5
        arroundedRate.append(rates)
    else:
        rate.append(rates)

rates.sort()

print("here are the arrounded rates :")
for rate in rates:
    print(rates)