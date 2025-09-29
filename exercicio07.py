nome = input("\nDigite o nome do estudante: ")
nota1 = float(input("\nDigite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
#entrada de dados

soma = nota1 + nota2 + nota3
media = soma / 3
#processamento de dados

print(f"\n O estudante {nome} obteve a média de {media}\n")
#saída de dados