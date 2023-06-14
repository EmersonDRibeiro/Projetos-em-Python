import random

def criar_baralho():
    naipes = ['Copas', 'Espadas', 'Ouros', 'Paus']
    valores = ['Ás', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valete', 'Dama', 'Rei']
    baralho = []
    for naipe in naipes:
        for valor in valores:
            baralho.append((valor, naipe))
    random.shuffle(baralho)
    return baralho

def contar_pontos(mao):
    total = 0
    ases = 0
    for carta in mao:
        if carta[0] in ['Valete', 'Dama', 'Rei']:
            total += 10
        elif carta[0] == 'Ás':
            total += 11
            ases += 1
        else:
            total += int(carta[0])
    while total > 21 and ases > 0:
        total -= 10
        ases -= 1
    return total

def mostrar_mao(mao):
    for carta in mao:
        print(f"{carta[0]} de {carta[1]}")

def jogar_blackjack():
    baralho = criar_baralho()
    mao_jogador = []
    mao_crupie = []

    for _ in range(2):
        mao_jogador.append(baralho.pop())
        mao_crupie.append(baralho.pop())

    while True:
        print("Sua mão:")
        mostrar_mao(mao_jogador)
        print("Pontuação:", contar_pontos(mao_jogador))
        print("\nMão do crupié:")
        print(f"{mao_crupie[0][0]} de {mao_crupie[0][1]}")
        print("-------------")

        if contar_pontos(mao_jogador) == 21:
            print("Blackjack! Você venceu!")
            break

        if contar_pontos(mao_jogador) > 21:
            print("Estourou! Você perdeu!")
            break

        opcao = input("Digite 'p' para 'Parar' ou 'a' para 'Acertar (para mais uma carta)': ")

        if opcao.lower() == 'p':
            while contar_pontos(mao_crupie) < 17:
                mao_crupie.append(baralho.pop())
            print("\nMão do crupié:")
            mostrar_mao(mao_crupie)
            print("Pontuação:", contar_pontos(mao_crupie))

            if contar_pontos(mao_crupie) > 21 or contar_pontos(mao_jogador) > contar_pontos(mao_crupie):
                print("Você venceu!")
            elif contar_pontos(mao_jogador) < contar_pontos(mao_crupie):
                print("Você perdeu!")
            else:
                print("Empate!")
            break

        elif opcao.lower() == 'a':
            mao_jogador.append(baralho.pop())

        else:
            print("Opção inválida. Digite 's' ou 'h'.")

if __name__ == "__main__":
    print("Bem-vindo ao Blackjack!")
    print("-----------------------")
    jogar_blackjack()
