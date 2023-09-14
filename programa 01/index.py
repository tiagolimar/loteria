import itertools as iter
import os


def ler_arquivo(nome_do_arquivo):
    with open(nome_do_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo_arquivo = arquivo.readlines()

    return conteudo_arquivo


def obter_jogos(conteudo_arquivo):
    lista_de_jogos = []
    for linha in conteudo_arquivo:
        lista_de_dezenas = tuple([int(i) for i in linha.strip().split()])
        lista_de_jogos.append(lista_de_dezenas)

    return lista_de_jogos


def listar_jogos(nome_do_arquivo):
    conteudo_arquivo = ler_arquivo(nome_do_arquivo)
    lista_de_jogos = obter_jogos(conteudo_arquivo)

    return lista_de_jogos


def obter_combinacoes(lista_dezenas):
    NUM_DEZ_POR_JOGO = 15
    combinacoes = iter.combinations(lista_dezenas, NUM_DEZ_POR_JOGO)
    return list(combinacoes)


def gerar_palpites(lista_de_palpites):
    palpites = {}
    for lista_dezenas in lista_de_palpites:
        palpites[lista_dezenas] = obter_combinacoes(lista_dezenas)
    return palpites


def analisar(palpites, historico_de_jogos):
    palpites_nunca_sorteados = []
    lista_de_palpites = palpites.keys()

    for num, palpite in enumerate(lista_de_palpites):
        quant_palpite_sorteado = 0
        for combinacao_palpite in palpites[palpite]:
            for jogo in historico_de_jogos:
                if combinacao_palpite == jogo:
                    quant_palpite_sorteado += 1
                    break

        os.system('cls')
        print(f'analisando {num}/{len(lista_de_palpites)} palpites.')

        if quant_palpite_sorteado == 0:
            palpites_nunca_sorteados.append(palpite)

    os.system('cls')
    print(f'Nº de palpites nunca sorteados = {len(palpites_nunca_sorteados)}')

    return palpites_nunca_sorteados


def salvar_palpites(palpites):
    linhas = ['\t'.join([str(i) for i in palpite]) for palpite in palpites]
    conteudo = '\n'.join(linhas)

    with open('palpites_nunca_sorteados.csv', 'w') as arquivo:
        arquivo.writelines(conteudo)


def principal():
    lista_de_palpites = listar_jogos('palpites de jogos.csv')
    historico_de_jogos = listar_jogos('históricos de jogos.csv')

    palpites = gerar_palpites(lista_de_palpites)

    palpites_nunca_sorteados = analisar(palpites, historico_de_jogos)

    salvar_palpites(palpites_nunca_sorteados)

    print('\nArquivo "palpites_nunca_sorteados.csv" está atualizado!')
    input()


principal()
