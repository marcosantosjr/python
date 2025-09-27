import random
from os import system, name

# Função para limar a tela a cada execução
def limpa_tela():
    # Windows
    if name == 'nt':
        _ = system('cls')

    # Mac ou Linux
    else:
        _ = system('clear')

def game():
    limpa_tela()

    # Lista de estágios da forca
    stages = [  # estágio 6 (final)
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # estágio 5
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # estágio 4
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # estágio 3
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # estágio 2
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # estágio 1
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # estágio 0
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]

    palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

    letras_adv = []

    letras_err = []

    palavra = random.choice(palavras)

    adivinha = ["_" for i in palavra]

    tentativas = 6

    def display():
        print("Letras adivinhadas:" + " ".join(letras_adv))
        print("Letras erradas:" + " ".join(letras_err))
        print("Tentativas restantes: " + str(tentativas))
        print(stages[tentativas])

    while tentativas > 0:

        if "_" in adivinha:

            letra = input("Insira uma letra: ")

            if letra not in letras_adv or letras_err:
                if letra in palavra:
                    for i in range(len(adivinha)):
                        if letra == palavra[i]:
                            adivinha[i] = letra
                            if letra not in letras_adv:
                                letras_adv.append(letra)
                                display()
                                print(letra)

                else:
                    tentativas = tentativas - 1

                    if letra not in letras_err:
                        letras_err.append(letra)

                    display()

                    if tentativas == 0:
                        print("Falhouu. A palavra era: " + palavra)
                        break
            else:
                print("Você já tentou essa letra, tente uma outra")

            print("".join(adivinha))

        else:
            display()
            break



# Bloco main
if __name__ == "__main__":
    game()
    print("\nParabéns\n")