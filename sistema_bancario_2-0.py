def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\nUsuário criado com sucesso!")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe seu CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, verifique seu CPF ou crie um usuário!")

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\nDeposito realizado com sucesso!")
    else:
        print("\nValor de deposito inválido, tente novamente!")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    while numero_saques < limite_saques:
        if valor > 0 and valor <= limite and valor <= saldo:
            saldo -= valor
            print("\nSaque realizado com sucesso!")
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            break
        elif valor <= 0:
            print("\nVocê deve digitar um valor maior que R$0 para saque.")
            break
        elif valor > limite:
            print(f"\nOperação inválida! Só é permitido R${limite} por saque.")
            break
        elif valor > saldo:
            print("\nSaldo insuficiente!")
            break
    else:
        print("\nLimite de saques excedido, tente novamente amanhã!")
    return saldo, extrato, numero_saques

def extrato_conta(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

menu = """

[u] Criar Usuário
[c] Criar conta
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

usuarios = []
contas = []
AGENCIA = "0001"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("\nDigite o valor a depositar: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("\nDigite o valor para saque: "))
        saldo, extrato, numero_saques = sacar(
            saldo= saldo,
            valor= valor,
            extrato= extrato,
            limite= limite,
            numero_saques= numero_saques,
            limite_saques= LIMITE_SAQUES
        )

    elif opcao == "e":
        extrato_conta(saldo, extrato= extrato)

    elif opcao == "u":
        criar_usuario(usuarios)

    elif opcao == "c":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)
    
    elif opcao == "q":
        print("\nObrigado por utilizar nosso banco! Volte sempre! =D")
        break
else:
    print("\nOperação inválida, por favor selecione novamente a operação desejada.")