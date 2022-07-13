num = 2
if num <=3: 
    print('num e 3')
    print(num - 3)
else:
    print('num nao e 3')
    print(num - 3)

num1 = int(input("Digite um numero: "))
num2 = int(input("Digite outro numero"))

if num1 > num2: 
    print(f'{num1}  e maior do que {num2}')
elif num1 < num2:
    print(f'{num1} e menor do que {num2}')
else:
    print(f'{num1} e igual a {num2}')