valorA = float(input("\nDigite o valor A: "))
valorB = float(input("Digite o valor B: "))
valorC = float(input("Digite o valor C: "))
#entrada de dados

delta = (valorB ** 2) - (4 * valorA * valorC)
x1 = (-valorB + delta ** 0.5) / (2 * valorA)
x2 = (-valorB - delta ** 0.5) / (2 * valorA)
#processamento de dados

print(f"""\nO resultado do delta é: {delta}
      O valor da raioz x1 é: {x1}
      O valor da raiz x2 é: {x2}\n""")
#saída de dados