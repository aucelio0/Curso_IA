def desenhar_tabuleiro(tabuleiro):
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("--+---+--")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("--+---+--")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")


def verificar_vencedor(tabuleiro, jogador):
    
    vitorias = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  # Linhas
                (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Colunas
                (0, 4, 8), (2, 4, 6)]            # Diagonais
    for vitoria in vitorias:
        if tabuleiro[vitoria[0]] == tabuleiro[vitoria[1]] == tabuleiro[vitoria[2]] == jogador:
            return True
    return False


def verificar_empate(tabuleiro):
    return all([celula != " " for celula in tabuleiro])


def jogar():
    
    tabuleiro = [" "] * 9
    jogador_atual = "X"  

    while True:
        desenhar_tabuleiro(tabuleiro)
        try:

            posicao = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1

            if posicao < 0 or posicao >= 9 or tabuleiro[posicao] != " ":
                print("Posição inválida, tente novamente.")
                continue
        except ValueError:
            print("Entrada inválida! Digite um número entre 1 e 9.")
            continue

        tabuleiro[posicao] = jogador_atual

        if verificar_vencedor(tabuleiro, jogador_atual):
            desenhar_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break

        if verificar_empate(tabuleiro):
            desenhar_tabuleiro(tabuleiro)
            print("Empate!")
            break

        
        jogador_atual = "O" if jogador_atual == "X" else "X"


if __name__ == "__main__":
    jogar()
