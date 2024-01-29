saldo = 0
extrato = []
saques_diarios = 0

def depositar(valor):
    global saldo
    global extrato
    saldo += valor
    extrato.append(('Depósito', valor))

def sacar(valor):
    global saldo
    global extrato
    global saques_diarios
    if saques_diarios >= 3:
        return "Limite de saques diários atingido."
    elif valor > 500:
        return "Limite máximo de saque é R$ 500,00."
    elif saldo < valor:
        return "Saldo insuficiente."
    else:
        saldo -= valor
        extrato.append(('Saque', -valor))
        saques_diarios += 1

def visualizar_extrato():
    global saldo
    global extrato
    if not extrato:
        return "Não foram realizadas movimentações."
    else:
        extrato_formatado = ""
        for operacao, valor in extrato:
            extrato_formatado += f"{operacao}: R$ {valor:.2f}\n"
        extrato_formatado += f"Saldo atual: R$ {saldo:.2f}"
        return extrato_formatado

def menu():
    while True:
        print("========================")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Visualizar Extrato")
        print("4. Sair")
        print("========================")
        opcao = input("Escolha a operação: ")
        if opcao == '1':
            valor = float(input("Digite o valor a depositar: "))
            depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor a sacar: "))
            print(sacar(valor))
        elif opcao == '3':
            print(visualizar_extrato())
        elif opcao == '4':
            break
        else:
            print("Opção inválida.")

menu()