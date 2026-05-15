# 1. Solicita os números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# 2. Realiza os cálculos matemáticos
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

# 3. Trata a divisão para evitar erro por zero
if num2 != 0:
    divisao = num1 / num2
else:
    divisao = "Erro! Divisão por zero."

# 4. Exibe os resultados na tela
print(f"\nResultados para {num1} e {num2}:")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
