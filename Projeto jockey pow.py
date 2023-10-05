j1 = 0
j2 = 0
empate = 0
for x in range(3):
    jogador1 = input("JOGADOR 1: [Pedra,Papel ou tesoura]:  ")
    jogador2 = input("JOGADOR 2: [Pedra,Papel ou tesoura]:  ")
    if jogador1 == "pedra" and jogador2 == "pedra" or jogador1 == "tesoura" and jogador2 == "tesoura" or jogador1 == "papel" and jogador2 == "papel":
        print("EMPATE")
        empate += 1
    elif jogador1 == "pedra" and jogador2 == "tesoura" or jogador1 == "papel" and jogador2 == "pedra" or jogador1 == "tesoura" and jogador2 == "papel":
        print("Jogador 1 VENCEU O ROUND")
        j1 += 1

    else:
        print("Jogador 2 VENCEU O ROUND")
        j2 += 1


if empate > j1 and empate > j2:
    print("PARTIDA EMPATADA!")
elif j2 > j1:
    print("JOGADOR 2 GANHOU A PARTIDA, PARABENS")
else:
    print("JOGADOR 1 GANHOU A PARTIDA, PARABENS")
