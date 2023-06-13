import random

def jogar_forca():
    palavras = ["python", "programacao", "desenvolvimento", "computador", "algoritmo"]
    palavra_secreta = random.choice(palavras)
    letras_corretas = []
    letras_erradas = []
    tentativas = 6

    print("Bem-vindo ao Jogo da Forca")
    print("A palavra secreta tem", len(palavra_secreta), "letras.")

    while True:
        print("\n")
        for letra in palavra_secreta:
            if letra in letras_corretas:
                print(letra, end=" ")
            else:
                print("_", end=" ")
        
        print("\n\nLetras erradas:", " ".join(letras_erradas))
        
        if tentativas == 0:
            print("Você perdeu! A palavra secreta era:", palavra_secreta)
            break
        
        if "_" not in "".join([letra if letra in letras_corretas else "_" for letra in palavra_secreta]):
            print("Você venceu!")
            break
        
        palpite = input("Digite uma letra: ").lower()
        
        if len(palpite) != 1:
            print("Por favor, digite apenas uma letra.")
            continue
        
        if palpite in letras_corretas or palpite in letras_erradas:
            print("Você já tentou essa letra. Tente outra.")
            continue
        
        if palpite in palavra_secreta:
            letras_corretas.append(palpite)
        else:
            letras_erradas.append(palpite)
            tentativas -= 1

if __name__ == "__main__":
    jogar_forca()
