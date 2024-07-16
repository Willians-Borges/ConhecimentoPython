# nome = input("Nome do dono: ")
# empresa = input("Nome da empresa: ")
# volume = input("Volume do produto: ")
# kcal = float("Qauntas calorias: ")
# sabor = input("Qual o sabor: ")
# receita = input("Quais igredientes: ")
# serial = input(" ")
# validade = input("Qual a validade: ")
# dising = input("Qual estetica da embalagem: ")
# preco = input("Qual o valor: ")



saldo = 1000
senha_cartao = '1234'
limite = 1000

produto = input("Bem vindo a nossa loja, por favor, informe o produto que deseja; ")
preco = float(input("Informe o preço do produto: "))
formapgto = int(input("Forma de pagamaneto \n [1]-Dinheiro\n[2]-credito\n[3]-debito\n[4]-Pix"))

if formapgto ==1:
    din = float(input("Qual o valor dado em especie"))
    if(din > preco):
        print("Parabens pela sua compra, seu troco é de ", din - preco)
    elif(din == preco):
        print("Parabens pela sua compra, ate a proxima ")
    else:
        print("o valor nao é suficiente, sinto muito!")
elif formapgto == 2:
    if(limite >= preco):
        op = input("Deseja parcelar sua compra? S - SIm ou N - NÃO")
        senhaUser = input("Digite sua senha")
        if(op == 'N'):
            print("Parabens pela sua compra")
        elif(op == 'S'):
            nparcela = (input("Em quantas parcelas. O valor deve ser maior que o 0"))
            print("Parabens pela sua compra, a parcela foi de ", preco/nparcela)
        else:
            print("Digite um valor valido")
    else:
        print("O seu saldo é insuficiente")
elif formapgto == 3:
    if (limite >= preco):
        op = input("Deseja completar sua compra? S - SIm ou N - NÃO")
        senhaUser = input("Digite sua senha")
        if (op == 'N'):
            print("Sua compra nao foi aceita")
        elif (op == 'S'):
            nparcela = (input("O valor deve ser maior que o 0"))
            print("Parabens pela sua compra")
        else:
            print("Digite um valor valido")
    else:
        print("O seu saldo é insuficiente")
elif formapgto == 4:
    pix = input("Deseja completar sua compra? S - SIm ou N - NÃO")
    if (pix >= preco):
        print("Sua compra nao foi aceita")
    else:
        print("o valor nao é suficiente, sinto muito!")