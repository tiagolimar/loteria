import itertools as iter


def ler_arquivo(nome_do_arquivo):
    with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo_arquivo = arquivo.readlines()

    return conteudo_arquivo


def obter_historico(conteudo_arquivo):
    historico_de_jogos = []
    for linha in conteudo_arquivo:
        lista_de_dezenas = [int(i) for i in linha.strip().split()]
        historico_de_jogos.append(lista_de_dezenas[:])

    return historico_de_jogos


def listar_dezenas(nome_do_arquivo):
    conteudo_arquivo = ler_arquivo(nome_do_arquivo)
    lista_de_dezenas = obter_historico(conteudo_arquivo)

    return lista_de_dezenas


def gerar_relatorio(combinacoes_palpites, historico_de_jogos):
    for combinacoes_palpite in combinacoes_palpites:
        palpite_ja_sorteado = 0
        for jogo in historico_de_jogos:
            if combinacoes_palpite == jogo:
                palpite_ja_sorteado += 1
        print(palpite_ja_sorteado)

def exportar_arquivo():
    pass


def principal():
    NUM_DEZ_POR_JOGO = 15
    palpite_de_jogos = listar_dezenas('palpites de jogos.csv')
    historico_de_jogos = listar_dezenas('históricos de jogos.csv')

    combinacoes_palpites = [list(iter.combinations(
        i, NUM_DEZ_POR_JOGO)) for i in palpite_de_jogos]

    print(len(combinacoes_palpites[0]))
    gerar_relatorio(combinacoes_palpites, historico_de_jogos)


principal()
