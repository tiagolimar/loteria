import os
from random import choice
import itertools

arquivo_entrada = 'jogos.csv'
arquivo_saída = 'sortudo.csv'
num_conjunto_jogos = 1
num_dezena_por_conjunto = 19
jogos = []
cabecalho = ';'.join(['DEZ' + str(i) for i in range(1,num_dezena_por_conjunto + 1)]) + ';PONT12;PONT13\n'

with open(arquivo_entrada,'r') as arq:
	conteudo = arq.readlines()

for i in conteudo:
	jogo = []
	for k in i.strip().split('\t'):
		jogo.append(int(k))
	if len(jogo)> 2:
		jogo.sort()
		jogos.append(jogo[:])
		
def obter_um_conjunto(quantidade_dezenas, jogos, verificador, total):
	jogo = []
	dezenas = [i for i in range(1,25)]
	condicao = True
	verificador = [i[:-2] for i in verificador]
	
	while condicao:
		for i in range(quantidade_dezenas):
			escolha = choice(dezenas)
			jogo.append(escolha)
			dezenas.remove(escolha)
		
		jogo.sort()
		
		if jogo in verificador:
			jogo = []
			dezenas = [i for i in range(1,25)]
			continue
		else:
			condicao = False

		combinacoes = list(itertools.combinations(jogo,25))
		total_combinacoes = len(combinacoes)
		
		for num,combinacao in enumerate(combinacoes):
			pontuou12 = 0
			pontuou13 = 0
			
			os.system('cls')
			print(f'{len(verificador)+1} de {total} conjunto de dezenas sendo gerado...\n')
			print(f'{num} de {total_combinacoes} comparações realizadas...')

			for jogatina in jogos:
				pontuacao = 0
				for dezena_combinacao in combinacao:
					if dezena_combinacao in jogatina:
						pontuacao += 1
				if pontuacao == 12:
					pontuou12 += 1
				elif pontuacao == 13:
					pontuou13 += 1
		
	jogo.append(pontuou12)
	jogo.append(pontuou13)
	
	return jogo

conjuntos = []

for i in range(num_conjunto_jogos):
	conjunto = obter_um_conjunto(num_dezena_por_conjunto, jogos, conjuntos, num_conjunto_jogos)
	conjuntos.append(conjunto[:])

saida = '\n'.join([';'.join([str(dezena) for dezena in conjunto])for conjunto in conjuntos])

with open(arquivo_saída,'w') as arq:
	arq.writelines(cabecalho + saida)

input('Concluído...')