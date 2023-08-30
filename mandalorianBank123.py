from datetime import datetime
import textwrap

def menu():
    menu = """\n
    ----------------------------------
    Seja bem vindo ao Mandalorian Bank
    
    ------Digite a opção desejada-----
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    ----------------------------------
    => """
    return input(textwrap.dedent(menu))

def depositar(salario, valor, extrato, /):
    if valor > 0 :
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("\n--- Depósito realizado com sucesso --- ")
    
    else:
        print("\n --- Valor inválido para depósito. Por favor, digite o valor positivo! ---")
        return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite_diario
    excedeu_saque = qnt_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("--- Operação inválida! Não há saldo suficiente em conta! ---")
    
    elif excedeu_limite:
        print("--- Operação inválida! O valor do saque excede o limite diário! ---")

    elif excedeu_saque:
        print("--- Operação inválida! Numero de saque diários excedido! ---")

    elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            qnt_saques += 1
            print("\n--- Saque realizado com sucesso! ---")

    else:
        print("--- Operação inválida! Informe um valor positivo! ---")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n--------- Extrato ----------") 
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f} {data_atual}")
    print("----------------------------")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n--- Já existe usuário com esse CPF! ---")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("--- Usuário criado com sucesso! ---")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n--- Conta criada com sucesso! Bem vindo ao clã ---")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n--- Usuário não encontrado, criação de conta encerrada! ---")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 34)
        print(textwrap.dedent(linha))

data_atual = datetime.now()



def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite_diario = 500
    extrato = ""
    qnt_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "d":
            valor = float(input("Inforque o valor que deseja depositar: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite_diario,
                numero_saques=qnt_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
             exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("--- Obrigado por usar o Mandalorian Bank, como deve ser! ---")
            break

        else:
            print("Operação inválida!")

main()