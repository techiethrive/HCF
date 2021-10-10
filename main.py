a = int(input('Enter First Integer: '))
b = int(input('Enter Second Integer: '))
num = a and b
for i in range(num,1,-1):
    if a % i == 0 and b % i == 0 :
        print(f"HCF of {a} and {b} is {i}")
        break
else:
    print(f'HCF of {a} and {b} is 1, So They are Co-Prime.')
