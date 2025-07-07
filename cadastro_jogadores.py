jogadores = list()
jogador = dict()
gols = list()
totgols = 0
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, partidas):
        gol = int(input(f'  Quantos gols na partida {c+1}? '))
        gols.append(gol)
        totgols += gol
    jogador['gols'] = gols[:]
    jogador['total'] = totgols
    jogadores.append(jogador.copy())
    gols.clear()
    totgols = 0
    print('-=' * 30)
    resp = str(input('Deseja continuar? [S/N] ')).upper()[0]
    while resp not in 'SN':
        print(f'ERRO! Responda apenas S ou N. ', end='')
        resp = str(input('Deseja continuar? ')).upper()[0]
    if resp == 'N':
        break
    print('-=' * 30)
print('-=' * 30)
print(f'{"cod":<4}', end='')
print(f'{"nome":<15}', end='')
print(f'{"gols":<20}', end='')
print(f'{"total":>8}')
print('-' * 50)
for c, j in enumerate(jogadores):
    print(f'{c:<4}', end='')
    print(f'{j["nome"]:<15}', end='')
    print(f'{str(j["gols"]):<20}', end='')
    print(f'{j["total"]:>8}')
print('-' * 50)
while True:
    dados = int(input('Deseja mostrar os dados de qual jogador? [999 para interromper] '))
    if dados in range(0, len(jogadores)):
        print('-' * 50)
        print(f'-- Levantamento do jogador {jogadores[dados]["nome"]}:')
        for c, d in enumerate(jogadores[dados]['gols']):
            print(f'    => No jogo {c+1} fez {d} gols.')
    print('-' * 50)
    if dados == 999:
        break
    if dados >= len(jogadores):
        print(f'ERRO! Não existe jogador com o código {dados}.')
        print('-' * 50)
print('>> PROGRAMA ENCERRADO <<')
