menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        print("\nDeposito")
        
        deposito = float(input("\nDigite o valor a depositar: "))
        if deposito > 0:
            saldo += deposito
            print("Deposito realizado com sucesso!")
            extrato += f"Depósito: R$ {deposito:.2f}\n"    
        else:
            print("Valor de deposito inválido, tente novamente!")
    
    elif opcao == "s":
        print("\nSaque")
        saque = float(input("\nDigite o valor para saque: "))

        while numero_saques < LIMITE_SAQUES:
            if saque > 0 and saque <= limite and saque <= saldo:
                saldo -= saque
                print("Saque realizado com sucesso!")
                extrato += f"Saque: R$ {saque:.2f}\n"
                numero_saques += 1
                break
            elif saque <= 0:
                print("Você deve digitar um valor maior que R$0 para saque.")
                break
            elif saque > limite:
                print(f"Operação inválida! Só é permitido R${limite} por saque.")
                break
            elif saque > saldo:
                print("Saldo insuficiente!")
                break
        else:
            print("Limite de saques excedido, tente novamente amanhã!")        

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        print("Obrigado por utilizar nosso banco! Volte sempre! =D")
        break

else:
    print("Operação inválida, por favor selecione novamente a operação desejada.")