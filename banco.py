class Banco:
    def __init__(self) -> None:
        self.saldo = 0
        self.extrato = []
        self.saque_atual = 0
        self.LIMITE_SAQUE = 3
        self.VALOR_SAQUE_MAXIMO = 500
        
    def deposito(self, valor: float):
        self.saldo += valor
        self.extrato += { f"Depósito: R$ {valor:.2f}" }
        return self.saldo
        
    def saque(self, valor: float):
        self.saldo -= valor
        self.extrato += { f"Saque: R$ {valor:.2f}" }
        return self.saldo
            
    def get_extrato(self):
        return self.extrato

menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""

banco = Banco()
    
while True:
    opcao = input(menu)
    
    if opcao == '1':
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo_atual = banco.deposito(valor)
            print(f'Saldo atual: R$ {saldo_atual}')
        else:
            print("Operação falhou!\nInforme um valor válido.")
    
    elif opcao == '2':
        valor = float(input("Informe o valor do saque: "))
        
        if valor > 0:
            if valor > banco.VALOR_SAQUE_MAXIMO:
                print("Valor maior que o limite permitido.")
                pass
            elif banco.saque_atual >= banco.LIMITE_SAQUE:
                print("Excedeu o limite de saque diário")
                pass
            elif valor > banco.saldo:
                print("Saldo insuficiente.")
                pass
            else:
                banco.saque_atual += 1
                saldo_atual = banco.saque(valor)
                print(f'Saldo atual: R$ {saldo_atual}')
        else:
            print("Operação falhou!\nInforme um valor válido.")
    elif opcao == '3':
        print("Extrato")
        for item in banco.get_extrato():
            print(item)
        print(f"\nSaldo: {banco.saldo}")
        
    elif opcao == '4':
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a opreação desejada.")