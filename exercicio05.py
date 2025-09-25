ano_atual = int(input("\nDigite o ano atual: "))
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
#entrada de dados

idade_anos = ano_atual - ano_nascimento
idade_meses = idade_anos * 12
idade_semanas = idade_anos * 52
idade_dias = idade_anos * 365
#processamento de dados

print(f"\nIdade em meses: {idade_meses}\nIdade em semanas: {idade_semanas}\nIdade em dias: {idade_dias}\n")
#saída de dados