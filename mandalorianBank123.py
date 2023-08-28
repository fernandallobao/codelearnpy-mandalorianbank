from datetime import datetime

menu = """
----------------------------------
Seja bem vindo ao Mandalorian Bank
----------------------------------
Digite a opção desejada:
[d]Depositar
[s]Sacar
[e]Extrato
[q]Sair
----------------------------------

"""
data_atual = datetime.now()
saldo = 0
limite_diario = 500
extrato = ""
qnt_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Inforque o valor que deseja depositar: "))

        if valor > 0 :
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Valor inválido para depósito. Por favor, digite o valor positivo ou 0 para sair!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_diario
        excedeu_saque = qnt_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação inválida! Não há saldo suficiente em conta!")
    
        elif excedeu_limite:
            print("Operação inválida! O valor do saque excede o limite diário!")

        elif excedeu_saque:
            print("Operação inválida! Numero de saque diários excedido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            qnt_saques += 1

        else:
            print("Operação inválida! Informe um valor positivo!")
    
    elif opcao == "e":
        print("\n--------- Extrato ----------") 
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f} {data_atual}")
        print("----------------------------")

    elif opcao == "q":
        print("Obrigado por usar o Mandalorian Bank como deve ser!")
        break

    else:
        print("Operação inválida!")
