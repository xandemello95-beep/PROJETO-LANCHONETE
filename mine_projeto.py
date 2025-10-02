print("Bem-vindo à Lanchonete Código Saboroso!")
print("Cardápio")
print("[1] Hambúrguer Simples - R$ 15,00")
print("[2] Hambúrguer Duplo - R$ 20,00")
print("[3] Batata Frita - R$ 8,00")
print("[4] Refrigerante - R$ 5,00")
print("[0] Finalizar Pedido")

x1=0
x2=0
x3=0
x4=0

while True:
    pedido=int(input("Faça o seu pedido colocando o codigo de cada item: "))
    if pedido == 0:
        print("Pedido finalizado")
        break
    elif pedido == 1:
        print("Hambúrguer Simples adicionado ao pedido!")
        x1 += 1
    elif pedido == 2:
        print("Hambúrguer Duplo adicionado ao pedido!")
        x2 += 1
    elif pedido == 3:
        print("Batata Frita adicionada ao pedido!")
        x3 +=1
    elif pedido == 4:
        print("Refrigerante adicionada ao pedido!")
        x4 +=1
    else:
        print("opcao invalida")
       
total=((x1*15)+(x2*20)+(x3*8)+(x4*5))


print(f"{x1} Hambúrguer Simples")
print(f"{x2} Hambúrguer Duplo")
print(f"{x3} Batata Frita")
print(f"{x4} Refrigerante")

print(f"Seu pedido deu R${total}")

print("Qual a forma de pagamento?")

print("[1] Cartão de Crédito (acréscimo de 5%)")
print("[2] PIX (desconto de 10%)")
print("[3] Dinheiro")

PG=int(input())

if PG == 1:
    cartao=(total * 1.05)
    print(f"Forma de pagamento escolhida Cartão de Crédito, seu pedido deu R${cartao},00")
if PG == 2:
    pix=(total * 0.9)
    print(f"Forma de pagamento escolhida PIX, seu pedido deu R${pix},00")
if PG == 3:
    DN=int(input("Quanto você vai pagar agora? "))
    if DN < total:
        print(f"Ainda esta faltando R${total-DN},00")
    if DN > total:
        troco=(DN-total)
        print(f"Voce vai receber um troco de R${troco},00")

print("Obrigado pela preferência! Seu pedido está sendo preparado.")