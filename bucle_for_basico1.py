# 1 Básico:
for i in range(0,151):
    print(i)
print(" ")

# 2. Múltiplos de cinco:
for i in range(5,1001,5):
    print(i)
print(" ")

# 3. Contar, a la manera del Dojo:
for i in range(1,101):
    valor = i
    if i % 5 == 0:
        valor = "Coding"
        if i % 10 == 0:
            valor += " Dojo"
    print(valor)
print(" ")

# 4. Whoa. Es un gran idiota:
suma = 0
for i in range(1, 500000, 2):
    suma += i
print(suma)
print(" ")

# 5. Cuenta regresiva de a 4:
for i in range(2018, 0, -4):
    print(i)
print(" ")

# 6. Contador flexible:
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)