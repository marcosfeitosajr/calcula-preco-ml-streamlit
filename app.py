import streamlit as st
import numpy as np
import pandas as pd

#Webscraping
import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
page = requests.get('https://www.mercadolivre.com.br/ajuda/Custos-de-frete-gratis-pelo-Mercado-Envios_3362')
conteudo = page.content

soup = BeautifulSoup(conteudo, 'html.parser')

tabelas = soup.find_all('div', attrs={'class': 'faq-item__hidden-content'})



#Extraindo as tabelas


# Gerando a série PESO

peso = []

for i in range(16,206,10):
	lista_peso = soup.find_all('td')[i].text
	peso.append(lista_peso)

#1 Dividindo a série PESO em duas colunas: coluna 1 = peso_inicial

peso_inicial = []

for i in range(0,len(peso)):

	if i == 1:
		b = peso[i].split()
		c = b[1]
		d = float(c)

	elif len(peso[i].split()) == 3:
		c = 0
		d = float(c)

	elif len(peso[i].split()) == 4:
		b = peso[18].split()
		c = b[2]
		d = float(c)
	elif len(peso[i].split()) == 5:
		b = peso[i].split()
		c = b[1] 
		d = float(c)

	elif len(peso[i].split()) == 6:
		b = peso[i].split()
		c = b[1]
		d = float(c)

	peso_inicial.append(d+0.001)
	peso_inicial[0] = 0

#2 Dividindo a série PESO em duas colunas: coluna 2 = peso_final

peso_final = []

for i in range(0,len(peso)):

	if len(peso[i].split()) == 3:
		f = peso[i].split()
		g = f[1] 

	elif len(peso[i].split()) == 4:
		g = '9999'

	elif len(peso[i].split()) == 5:
		f = peso[i].split()
		g = f[3]  

	elif len(peso[i].split()) == 6:
		f = peso[i].split()
		g = f[4]

	peso_final.append(g) 


#1 Gerando a coluna de menos de R$ 79 / Full / Sudeste

vsd_menos_de_79_full = []

for i in range(18,208,10):

	lista_menos_79 = str(soup.find_all('td')[i].get_text())[2:]

	vsd_menos_de_79_full.append(lista_menos_79)

#2 Gerando a coluna de menos de R$ 79 / Outros / Sudeste

vsd_menos_de_79_outros = []

for i in range(19,209,10):

	lista_menos_79 = str(soup.find_all('td')[i].get_text())[2:]
		 
	vsd_menos_de_79_outros.append(lista_menos_79)

#3 Gerando a coluna de > R$ 79 / Full / Sudeste

vsd_mais_de_79_full = []

for i in range(21,211,10):

	lista_mais_79 = str(soup.find_all('td')[i].get_text())[2:]
		 
	vsd_mais_de_79_full.append(lista_mais_79)

#4 Gerando a coluna de > R$ 79 Outros Sudeste

vsd_mais_de_79_outros = []

for i in range(22,212,10):

	lista_mais_79 = str(soup.find_all('td')[i].get_text())[2:]
		 
	vsd_mais_de_79_outros.append(lista_mais_79)

#5 Gerando a coluna de Categorias especiais FULL Sudeste

vsd_categorias_especiais_full = []

for i in range(24,214,10):

	cat_especial_full = str(soup.find_all('td')[i].get_text())[2:]
		 
	vsd_categorias_especiais_full.append(cat_especial_full)

#6 Gerando a coluna de Categorias especiais Outros Sudeste

vsd_categorias_especiais_outros = []

for i in range(25,215,10):

	cat_especial_outros = str(soup.find_all('td')[i].get_text())[2:]
		 
	vsd_categorias_especiais_outros.append(cat_especial_outros)

#1 Gerando a coluna de menos de R$ 79 / Full / Restante do país

vrp_menos_de_79_full = []

for i in range(222,412,10):

	lista_menos_79 = str(soup.find_all('td')[i].get_text())[2:]

	vrp_menos_de_79_full.append(lista_menos_79)

#2 Gerando a coluna de menos de R$ 79 / Outros / Restante do país

vrp_menos_de_79_outros = []

for i in range(223,413,10):

	lista_menos_79 = str(soup.find_all('td')[i].get_text())[2:]
		 
	vrp_menos_de_79_outros.append(lista_menos_79)

#3 Gerando a coluna de > R$ 79 / Full / Restante do país

vrp_mais_de_79_full = []

for i in range(225,415,10):

	lista_mais_79 = str(soup.find_all('td')[i].get_text())[2:]
		 
	vrp_mais_de_79_full.append(lista_mais_79)

#4 Gerando a coluna de > R$ 79 Outros Restante do país

vrp_mais_de_79_outros = []

for i in range(226,416,10):

	lista_mais_79 = str(soup.find_all('td')[i].get_text())[2:]
		 
	vrp_mais_de_79_outros.append(lista_mais_79)

#5 Gerando a coluna de Categorias especiais FULL Restante do país

vrp_categorias_especiais_full = []

for i in range(228,418,10):

	cat_especial_full = str(soup.find_all('td')[i].get_text())[2:]
		 
	vrp_categorias_especiais_full.append(cat_especial_full)

#6 Gerando a coluna de Categorias especiais Outros Restante do país

vrp_categorias_especiais_outros = []

for i in range(229,419,10):

	cat_especial_outros = str(soup.find_all('td')[i].get_text())[2:]
		 
	vrp_categorias_especiais_outros.append(cat_especial_outros)

#1 Gerando a coluna de menos de R$ 79 / Full / Sudeste
asd_menos_de_79_full = []

for i in range(428,618,10):

	lista_menos_79 = str(soup.find_all('td')[i].get_text())[2:]

	asd_menos_de_79_full.append(lista_menos_79)

#2 Gerando a coluna de menos de R$ 79 / Outros / Sudeste

asd_menos_de_79_outros = []

for i in range(429,619,10):

	lista_menos_79 = str(soup.find_all('td')[i].get_text())[2:]
		 
	asd_menos_de_79_outros.append(lista_menos_79)

#3 Gerando a coluna de > R$ 79 / Full / Sudeste

asd_mais_de_79_full = []

for i in range(431,621,10):

	lista_mais_79 = str(soup.find_all('td')[i].get_text())[2:]
		 
	asd_mais_de_79_full.append(lista_mais_79)

#4 Gerando a coluna de > R$ 79 Outros Sudeste

asd_mais_de_79_outros = []

for i in range(432,622,10):

	lista_mais_79 = str(soup.find_all('td')[i].get_text())[2:]
		 
	asd_mais_de_79_outros.append(lista_mais_79)

#5 Gerando a coluna de Categorias especiais FULL Sudeste

asd_categorias_especiais_full = []

for i in range(434,624,10):

	cat_especial_full = str(soup.find_all('td')[i].get_text())[2:]
		 
	asd_categorias_especiais_full.append(cat_especial_full)

#6 Gerando a coluna de Categorias especiais Outros Sudeste

asd_categorias_especiais_outros = []

for i in range(435,625,10):

	cat_especial_outros = str(soup.find_all('td')[i].get_text())[2:]
		 
	asd_categorias_especiais_outros.append(cat_especial_outros)

#1 Gerando a coluna de menos de R$ 79 / Full / Restante do país

arp_menos_de_79_full = []

for i in range(632,822,10):

	lista_menos_79 = str(soup.find_all('td')[i].get_text())[2:]

	arp_menos_de_79_full.append(lista_menos_79)

#2 Gerando a coluna de menos de R$ 79 / Outros / Restante do país
arp_menos_de_79_outros = []

for i in range(633,823,10):

	lista_menos_79 = str(soup.find_all('td')[i].get_text())[2:]
		 
	arp_menos_de_79_outros.append(lista_menos_79)

#3 Gerando a coluna de > R$ 79 / Full / Restante do país

arp_mais_de_79_full = []

for i in range(635,825,10):

	lista_mais_79 = str(soup.find_all('td')[i].get_text())[2:]
		 
	arp_mais_de_79_full.append(lista_mais_79)

#4 Gerando a coluna de > R$ 79 Outros Restante do país

arp_mais_de_79_outros = []

for i in range(636,826,10):

	lista_mais_79 = str(soup.find_all('td')[i].get_text())[2:]
		 
	arp_mais_de_79_outros.append(lista_mais_79)

#5 Gerando a coluna de Categorias especiais FULL Restante do país

arp_categorias_especiais_full = []

for i in range(638,828,10):

	cat_especial_full = str(soup.find_all('td')[i].get_text())[2:]
		 
	arp_categorias_especiais_full.append(cat_especial_full)


#6 Gerando a coluna de Categorias especiais Outros Restante do país

arp_categorias_especiais_outros = []

for i in range(639,829,10):

	cat_especial_outros = str(soup.find_all('td')[i].get_text())[2:]
		 
	arp_categorias_especiais_outros.append(cat_especial_outros)

#1 Gerando a coluna Full / Sudeste

rsd_full = []

for i in range(829,905,4):

	lista_menos_79 = str(soup.find_all('td')[i].get_text())[2:]

	rsd_full.append(lista_menos_79)

#2 Gerando a coluna Outros / Sudeste

rsd_outros = []

for i in range(830,906,4):

	lista_menos_79 = str(soup.find_all('td')[i].get_text())[2:]

	rsd_outros.append(lista_menos_79)

#1 Gerando a coluna Full / Restante do País

rrp_full = []

for i in range(911,987,4):

	lista_menos_79 = str(soup.find_all('td')[i].get_text())[2:]

	rrp_full.append(lista_menos_79)


#2 Gerando a coluna Outros / Restante do País

rrp_outros = []

for i in range(912,988,4):

	lista_menos_79 = str(soup.find_all('td')[i].get_text())[2:]

	rrp_outros.append(lista_menos_79)



# Criando o dataframe

dicionário = {
	    'peso faixa inicial' : peso_inicial,
	    'Peso faixa final' : peso_final,
	    'VSD Full abaixo R$ 79' : vsd_menos_de_79_full,
	    'VSD Outros abaixo R$ 79' : vsd_menos_de_79_outros,
	    'VSD Full a partir R$ 79 com 50% desconto' : vsd_mais_de_79_full,
	    'VSD Outros a partir R$ 79 com 50% desconto' : vsd_mais_de_79_outros,
	    'VSD Categorias especiais 25% desconto FULL' : vsd_categorias_especiais_full,
	    'VSD Categorias especiais 25% desconto outros' : vsd_categorias_especiais_outros,
	    'VRP Full abaixo R$ 79' : vrp_menos_de_79_full,
	    'VRP Outros abaixo R$ 79' : vrp_menos_de_79_outros,
	    'VRP Full a partir R$ 79 com 50% desconto' : vrp_mais_de_79_full,
	    'VRP Outros a partir R$ 79 com 50% desconto' : vrp_mais_de_79_outros,
	    'VRP Categorias especiais 25% desconto FULL' : vrp_categorias_especiais_full,
	    'VRP Categorias especiais 25% desconto outros' : vrp_categorias_especiais_outros,
	    'ASD Full abaixo R$ 79' : asd_menos_de_79_full,
	    'ASD Outros abaixo R$ 79' : asd_menos_de_79_outros,
	    'ASD Full a partir R$ 79 com 50% desconto' : asd_mais_de_79_full,
	    'ASD Outros a partir R$ 79 com 50% desconto' : asd_mais_de_79_outros,
	    'ASD Categorias especiais 25% desconto FULL' : asd_categorias_especiais_full,
	    'ASD Categorias especiais 25% desconto outros' : asd_categorias_especiais_outros,
	    'ARP Full abaixo R$ 79' : arp_menos_de_79_full,
	    'ARP Outros abaixo R$ 79' : arp_menos_de_79_outros,
	    'ARP Full a partir R$ 79 com 50% desconto' : arp_mais_de_79_full,
	    'ARP Outros a partir R$ 79 com 50% desconto' : arp_mais_de_79_outros,
	    'ARP Categorias especiais 25% desconto FULL' : arp_categorias_especiais_full,
	    'ARP Categorias especiais 25% desconto outros' : arp_categorias_especiais_outros,
	    'RSD Full' : rsd_full,
	    'RSD Outros' : rsd_outros,
	    'RRP Full' : rrp_full,
	    'RRP Outros' : rrp_outros
	}

regras_frete = pd.DataFrame(dicionário)
# Trocando as vírgulas por pontos
regras_frete = regras_frete.replace(',','.', regex=True)
# Alterando o tipo das colunas
regras_frete = regras_frete.astype({
	    'peso faixa inicial' : float,
	    'Peso faixa final' : float,
	    'VSD Full abaixo R$ 79' : float,
	    'VSD Outros abaixo R$ 79' : float,
	    'VSD Full a partir R$ 79 com 50% desconto' : float,
	    'VSD Outros a partir R$ 79 com 50% desconto' : float,
	    'VSD Categorias especiais 25% desconto FULL' : float,
	    'VSD Categorias especiais 25% desconto outros' : float,
	    'VRP Full abaixo R$ 79' : float,
	    'VRP Outros abaixo R$ 79' : float,
	    'VRP Full a partir R$ 79 com 50% desconto' : float,
	    'VRP Outros a partir R$ 79 com 50% desconto' : float,
	    'VRP Categorias especiais 25% desconto FULL' : float,
	    'VRP Categorias especiais 25% desconto outros' : float,
	    'ASD Full abaixo R$ 79' : float,
	    'ASD Outros abaixo R$ 79' : float,
	    'ASD Full a partir R$ 79 com 50% desconto' : float,
	    'ASD Outros a partir R$ 79 com 50% desconto' : float,
	    'ASD Categorias especiais 25% desconto FULL' : float,
	    'ASD Categorias especiais 25% desconto outros' : float,
	    'ARP Full abaixo R$ 79' : float,
	    'ARP Outros abaixo R$ 79' : float,
	    'ARP Full a partir R$ 79 com 50% desconto' : float,
	    'ARP Outros a partir R$ 79 com 50% desconto' : float,
	    'ARP Categorias especiais 25% desconto FULL' : float,
	    'ARP Categorias especiais 25% desconto outros' : float,
	    'RSD Full' : float,
	    'RSD Outros' : float,
	    'RRP Full' : float,
	    'RRP Outros' : float
	})

# Alterando o peso das células com gramas para quilos
regras_frete['Peso faixa final'][0] = regras_frete['Peso faixa final'][0] / 1000
regras_frete['peso faixa inicial'][1] = regras_frete['peso faixa inicial'][1] / 1000
#regras_frete = pd.read_csv(r'C:\Users\marcos.feitosa\Documents\Python Scripts\Calcula_preco_ml\TabelaFreteML.csv')

# Estabelecendo tarifas e comissões
#Comissão Mercado Livre Premium
MLP = float(0.17)

#Comissão Mercado Livre Clássico
MLC = float(0.12)

#Tarifa para vendas <= R$ 79
tarifaML = float(5)

#Preço de referência
preço_referencia = float(79)

#Sidebar
st.sidebar.title('Menu')
opcao = st.sidebar.radio('Selecione uma página ou modelo de cálculo',['Instruções','Modelo de cálculo 1','Modelo de cálculo 2','Modelo de cálculo 3','Modelo de cálculo 4','Modelo de cálculo 5'])

#Home
if opcao == 'Instruções':
	st.subheader('CÁLCULO DE PREÇO PARA ANÚNCIOS DO MERCADO LIVRE')
	st.info('')
	st.markdown(' ##### Olá! Você está na calculadora de preços do Mercado Livre. Leia com atenção as instruções a seguir para utilizar de maneira correta a calculadora de preços.')
	st.info('')
	st.write('No menu do lado esquerdo você encontrará cinco modelos de cálculo de preço sendo eles:',
		'\n1) Você define o valor do lucro em reais R$ e a calculadora define o preço;',
		'\n2) Você define a margem de lucro em porcentagem % e a calculadora define o preço;',
		'\n3) Você define o markup sobre o custo do produto e a calculadora define o preço;',
		'\n4) Você define o markup geral da sua operação ou o percentual dos seus custos operacionais e a margem de lucro líquido e a calculadora define o preço;',
		'\n5) Você é quem define o preço do anúncio clássico e do anúncio premium e a calculadora irá calcular o lucro ou prejuízo.')
	st.info('')
	st.write('Em todos os modelos de cálculo você precisará informar os dados do produto e os dados sua loja no Mercado Livre sendo:')
	st.write('')
	st.write('Dados do produto:',
		'\n* Custo do produto',
		'\n* Largura, altura e comprimento',
		'\n* Peso do produto',
		'\n* Se é categoria especial ou não')
	st.write('')
	st.write('Dados da loja no Mercado Livre:',
		'\n* Região de despacho do produto',
		'\n* Reputação da loja')
	st.info('')
	st.write('Para cada modelo de cálculo haverá um dados de entrada específico do modelo de cálculo. A seguir você pode conferir as instruções de cada dado de entrada caso tenha dúvidas.')
	st.write('')
	st.markdown('##### Modelo de cálculo 1 - Cálculo pelo valor do lucro')
	st.write('Neste modelo de cálculo você irá informar para a calculadora o valor do lucro desejado em Reais (BRL).',
		'\n\n**Exemplo:** Você possui um produto que custou 100,00 (BRL) e deseja ter um lucro de 25,00 (BRL) na venda desse produto no Mercado Livre. Na página do Modelo de cálculo 1 você encontrara um campo específico para inserir o valor de 25,00 (BRL) referente ao valor de lucro desejado.')
	st.write('')
	st.write('')
	st.write('')
	st.markdown('##### Modelo de cálculo 2 - Cálculo por margem de lucro')
	st.write('Neste modelo de cálculo você irá informar para a calculadora a margem de lucro desejada sendo:')
	st.latex(r''' margem~de~lucro = \frac{lucro}{faturamento}''')
	st.write('')
	st.write('**Exemplo:** Você possui um produto que custou 10,00 (BRL) e deseja ter uma margem de lucro de 20%. Se o preço de venda for 100,00 (BRL) o lucro será de 20,00 (BRL).')
	st.write('')
	st.write('')
	st.write('')
	st.markdown('##### Modelo de cálculo 3 - Cálculo por markup sobre o custo do produto')
	st.write('Neste modelo de cálculo você irá informar para a calculadora o markup sobre o custo do produto.')
	st.write('**Exemplo:** Você possui um produto que custou 100,00 (BRL) e deseja ter markup de 1,5 o lucro será de 50,00 (BRL) tanto para o anúncio clássico quanto para o anúncio premium.')
	st.write('')
	st.write('')
	st.write('')
	st.markdown('##### Modelo de cálculo 4 - Cálculo por markup geral ou por percentual de custos operacionais e lucro líquido')
	st.write('**IMPORTANTE** Para utilizar este modelo de cálculo tenha em mãos os dados da sua DRE _(Demonstração do Resultado do Exercício)_.')
	st.write('Neste modelo de cálculo você terá duas opções de dados de entrada sendo:',
		'\n\n* Markup geral:')
	st.latex(r''' markup~geral = \frac{1}{(1 - custos)}~~~~~~~~~\to~~~~~~~custos = \frac{soma~dos~custos}{soma~das~receitas}''')
	st.write('**Exemplo:** VNa sua DRE a soma das receitas é de 100.000,00 (BRL) e a soma dos custos é de 20.000,00 (BRL)')
	st.latex(r'''custos = \frac{20000,00}{100000,00}~~~~~~~\to~~~~~~~custos = 0,2''')
	st.latex(r''' markup~geral = \frac{1}{(1 - 0,2)}~~~~\to~~~~markup~geral=\frac{1}{0,8}~~~~\to~~~~markup~geral = 1,25''')
	st.write('* Os custos operacionais em % e a margem de lucro líquido desejado')
	st.write('Para esta opção considerar para os custos operacionais a mesma fórmula de custos do markup geral e informar a margem de lucro líquido desejado em %.')
	st.write('')
	st.write('')
	st.write('')
	st.markdown('##### Modelo de cálculo 5 - Cálculo de lucro a partir de preço de venda definido')
	st.write('Neste modelo de cálculo você é quem irá definir o preço de venda do anúncio clássico e do anúncio premium e a calculadora irá calcular o lucro ou prejuízo.')
	st.info('')
	st.subheader('Dúvidas ou sugestões')
	st.markdown('Para dúvidas ou sugestões envie um email para: [calcula.preco.ml@gmail.com](mailto:calcula.preco.ml@gmail.com) ')
	st.markdown('Ou')
	st.markdown('Me chama no whatsapp [whatsapp](https://wa.me/qr/ZJIF3OAYB7UKK1)')

#Modelo de cálculo 1
if opcao == 'Modelo de cálculo 1':
	#Informações do produto
	st.markdown('## Informações do produto')
	#Custo
	custo = st.number_input('Qual o custo do produto R$',0.00)
	#Altura
	altura = st.number_input('Altura (cm)',0)
	#Largura
	largura = st.number_input('Largura (cm)',0)
	#Comprimento
	comprimento = st.number_input('Comprimento (cm)',0)
	#Peso
	peso_produto = st.number_input('Peso (g)',0)
	#Categoria especial
	especial = st.radio('É categoria especial?',['Sim','Não'])
	st.markdown('Para saber se a categoria é especial, [Clique aqui.](https://www.mercadolivre.com.br/ajuda/3922)')
	if especial == 'Sim':
		especial = '1'
	elif especial == 'Não':
		especial = '2'
	#Full
	full = st.radio('Qual o método de envio?',['Mercado Envios Coleta','Mercado Envios Full'])
	if full == 'Mercado Envios Full':
		full = '1'
	elif full == 'Mercado Envios Coleta':
		full = '2'

	#Informações do seller
	st.markdown('## Informações do seller')
	#Região de despacho
	regiao = st.radio('Região de despacho',['Sul / Sudeste','Restante do país'])
	if regiao == 'Sul / Sudeste':
		regiao = '1'
	elif regiao == 'Restante do país':
		regiao = '2'
	#Reputação
	reputacao = st.radio('Reputação',['Verde','Amarela','Laranja ou Vermelha'])
	if reputacao == 'Verde':
		reputacao = '1'
	elif reputacao == 'Amarela':
			reputacao = '2'
	elif reputacao == 'Laranja ou Vermelha':
			reputacao = '3'

	# Calculando o frete

	peso_produto = float(peso_produto / 1000)
	peso_volumetrico = float(largura * comprimento * altura / 6000 )

	if peso_produto > peso_volumetrico:
	    peso_para_calculo = peso_produto
	elif peso_produto <= peso_volumetrico:
	    peso_para_calculo = peso_volumetrico


	# Selecionando a tabela

	for i in range(0,len(regras_frete)):
	    if regras_frete['peso faixa inicial'][i] <= peso_para_calculo <= regras_frete['Peso faixa final'][i]:
	        vsd_categorias_especiais_full = regras_frete['VSD Categorias especiais 25% desconto FULL'][i]
	        vsd_mais_de_79_full = regras_frete['VSD Full a partir R$ 79 com 50% desconto'][i]
	        vsd_categorias_especiais_outros = regras_frete['VSD Categorias especiais 25% desconto outros'][i]
	        vsd_mais_de_79_outros = regras_frete['VSD Outros a partir R$ 79 com 50% desconto'][i]
	        vrp_categorias_especiais_full = regras_frete['VRP Categorias especiais 25% desconto FULL'][i]
	        vrp_mais_de_79_full = regras_frete['VRP Full a partir R$ 79 com 50% desconto'][i]
	        vrp_categorias_especiais_outros = regras_frete['VRP Categorias especiais 25% desconto outros'][i]
	        vrp_mais_de_79_outros = regras_frete['VRP Outros a partir R$ 79 com 50% desconto'][i]
	        asd_categorias_especiais_full = regras_frete['ASD Categorias especiais 25% desconto FULL'][i]
	        asd_mais_de_79_full = regras_frete['ASD Full a partir R$ 79 com 50% desconto'][i]
	        asd_categorias_especiais_outros = regras_frete['ASD Categorias especiais 25% desconto outros'][i]
	        asd_mais_de_79_outros = regras_frete['ASD Outros a partir R$ 79 com 50% desconto'][i]
	        arp_categorias_especiais_full = regras_frete['ARP Categorias especiais 25% desconto FULL'][i]
	        arp_mais_de_79_full = regras_frete['ARP Full a partir R$ 79 com 50% desconto'][i]
	        arp_categorias_especiais_outros = regras_frete['ARP Categorias especiais 25% desconto outros'][i]
	        arp_mais_de_79_outros = regras_frete['ARP Outros a partir R$ 79 com 50% desconto'][i]
	        rsd_full = regras_frete['RSD Full'][i]
	        rsd_outros = regras_frete['RSD Outros'][i]
	        rrp_full = regras_frete['RRP Full'][i]
	        rrp_outros = regras_frete['RRP Outros'][i]

	#REPUTAÇÃO VERDE
	if regiao == '1' and reputacao == '1' and full == '1' and especial == '1':
	    custo_frete = vsd_categorias_especiais_full
	elif regiao == '1' and reputacao == '1' and full == '1' and especial == '2':
	    custo_frete = vsd_mais_de_79_full
	elif regiao == '1' and reputacao == '1' and full == '2' and especial == '1':
	    custo_frete = vsd_categorias_especiais_outros
	elif regiao == '1' and reputacao == '1' and full == '2' and especial == '2':
	    custo_frete = vsd_mais_de_79_outros
	elif regiao == '2' and reputacao == '1' and full == '1' and especial == '1':
	    custo_frete = vrp_categorias_especiais_full
	elif regiao == '2' and reputacao == '1' and full == '1' and especial == '2':
	    custo_frete = vrp_mais_de_79_full
	elif regiao == '2' and reputacao == '1' and full == '2' and especial == '1':
	    custo_frete = vrp_categorias_especiais_outros
	elif regiao == '2' and reputacao == '1' and full == '2' and especial == '2':
	    custo_frete = vrp_mais_de_79_outros


	#REPUTAÇÃO AMARELA
	elif regiao == '1' and reputacao == '2' and full == '1' and especial == '1':
	    custo_frete = asd_categorias_especiais_full
	elif regiao == '1' and reputacao == '2' and full == '1' and especial == '2':
	    custo_frete = asd_mais_de_79_full
	elif regiao == '1' and reputacao == '2' and full == '2' and especial == '1':
	    custo_frete = asd_categorias_especiais_outros
	elif regiao == '1' and reputacao == '2' and full == '2' and especial == '2':
	    custo_frete = asd_mais_de_79_outros
	elif regiao == '2' and reputacao == '2' and full == '1' and especial == '1':
	    custo_frete = arp_categorias_especiais_full
	elif regiao == '2' and reputacao == '2' and full == '1' and especial == '2':
	    custo_frete = arp_mais_de_79_full
	elif regiao == '2' and reputacao == '2' and full == '2' and especial == '1':
	    custo_frete = arp_categorias_especiais_outros
	elif regiao == '2' and reputacao == '2' and full == '2' and especial == '2':
	    custo_frete = arp_mais_de_79_outros

	#REPUTAÇÃO VERMELHA
	elif regiao == '1' and reputacao == '3' and full == '1':
	    custo_frete = rsd_full
	elif regiao == '1' and reputacao == '3' and full == '2':
	    custo_frete = rsd_outros
	elif regiao == '2' and reputacao == '3' and full == '1':
	    custo_frete = rrp_full
	elif regiao == '2' and reputacao == '3' and full == '2':
	    custo_frete = rrp_outros

	#st.markdown(custo_frete)

	#Informando o modelo de cálculo
	#Informar o lucro desejado
	st.markdown('## Dados de entrada do modelo de cálculo')
	lucro_desejado = st.number_input('',0.00)
	st.markdown('Informe o valor do lucro desejado em Reais **(R$)**')
	if lucro_desejado == 0:
		st.warning('Cuidado! Você definiu R$ 0,00 como valor do lucro.')
	
	#Cálculo
	st.markdown('## Resultado')
	condicao = st.button('Calcular')

	if condicao == True:
		#Cálculo clássico
		preço_final_classico = 0
		lucro_classico = 0

		while lucro_classico <= lucro_desejado:
			if preço_final_classico <= preço_referencia:
				tarifa = tarifaML
				frete = 0
			else:
				tarifa = 0
				frete = custo_frete
			lucro_classico = preço_final_classico - preço_final_classico * MLC - custo - tarifa - frete
			preço_final_classico += 0.01

		lucro_classico = preço_final_classico - preço_final_classico * MLC - custo - tarifa - frete
		
		st.write('')
		st.write('###### O preço do anúncio Clássico deve ser R$', round(preço_final_classico,2),
			'\n ###### O valor do frete é de R$', round(frete,2),
			'\n ###### O valor da comissão é de R$', round(preço_final_classico * MLC + tarifa,2),
			'\n ###### O repasse do Mercado Livre será de R$', round(lucro_classico + custo,2),
			'\n ###### O lucro será de R$', round(lucro_classico,2),
			'\n ###### A margem de lucro é de ',round(lucro_classico/preço_final_classico * 100,2),'%')
		
		#Calculo Premium
		preço_final_premium = 0
		lucro_premium = 0

		while lucro_premium <= lucro_desejado:
			if preço_final_premium <= preço_referencia:
				tarifa = tarifaML
				frete = 0
			else:
				tarifa = 0
				frete = custo_frete
			lucro_premium = preço_final_premium - preço_final_premium * MLP - custo - tarifa - frete
			preço_final_premium += 0.01

		lucro_premium = preço_final_premium - preço_final_premium * MLP - custo - tarifa - frete

		st.write('--------------------------------------')
		st.write('###### O preço do anúncio Premium deve ser R$', round(preço_final_premium,2),
			'\n ###### O valor do frete é de R$', round(frete,2),
			'\n ###### O valor da comissão é de R$', round(preço_final_premium * MLP + tarifa,2),
			'\n ###### O repasse do Mercado Livre será de R$', round(lucro_premium + custo,2),
			'\n ###### O lucro será de R$', round(lucro_premium,2),
			'\n ###### A margem de lucro é de ',round(lucro_premium/preço_final_premium * 100,2),'%')

#Modelo de cálculo 2
if opcao == 'Modelo de cálculo 2':
	#Informações do produto
	st.markdown('## Informações do produto')
	#Custo
	custo = st.number_input('Qual o custo do produto R$',0.00)
	#Altura
	altura = st.number_input('Altura (cm)',0)
	#Largura
	largura = st.number_input('Largura (cm)',0)
	#Comprimento
	comprimento = st.number_input('Comprimento (cm)',0)
	#Peso
	peso_produto = st.number_input('Peso (g)',0)
	#Categoria especial
	especial = st.radio('É categoria especial?',['Sim','Não'])
	st.markdown('Para saber se a categoria é especial, acesse: <https://www.mercadolivre.com.br/ajuda/3922>')
	if especial == 'Sim':
		especial = '1'
	elif especial == 'Não':
		especial = '2'
	#Full
	full = st.radio('Qual o método de envio?',['Mercado Envios Coleta','Mercado Envios Full'])
	if full == 'Mercado Envios Full':
		full = '1'
	elif full == 'Mercado Envios Coleta':
		full = '2'

	#Informações do seller
	st.markdown('## Informações do seller')
	#Região de despacho
	regiao = st.radio('Região de despacho',['Sul / Sudeste','Restante do país'])
	if regiao == 'Sul / Sudeste':
		regiao = '1'
	elif regiao == 'Restante do país':
		regiao = '2'
	#Reputação
	reputacao = st.radio('Reputação',['Verde','Amarela','Laranja ou Vermelha'])
	if reputacao == 'Verde':
		reputacao = '1'
	elif reputacao == 'Amarela':
			reputacao = '2'
	elif reputacao == 'Laranja ou Vermelha':
			reputacao = '3'


	#Informar o lucro desejado
	st.markdown('## Dados de entrada do modelo de cálculo')
	margem_lucro_desejada = st.number_input('',0)
	st.markdown('Informe a margem de lucro desejada em porcentagem **%**')
	if margem_lucro_desejada == 0:
		st.warning('Cuidado! Você definiu 0% como margem lucro.')
	# Calculando o frete

	peso_produto = float(peso_produto / 1000)
	peso_volumetrico = float(largura * comprimento * altura / 6000 )

	if peso_produto > peso_volumetrico:
	    peso_para_calculo = peso_produto
	elif peso_produto <= peso_volumetrico:
	    peso_para_calculo = peso_volumetrico


	# Selecionando a tabela

	for i in range(0,len(regras_frete)):
	    if regras_frete['peso faixa inicial'][i] <= peso_para_calculo <= regras_frete['Peso faixa final'][i]:
	        vsd_categorias_especiais_full = regras_frete['VSD Categorias especiais 25% desconto FULL'][i]
	        vsd_mais_de_79_full = regras_frete['VSD Full a partir R$ 79 com 50% desconto'][i]
	        vsd_categorias_especiais_outros = regras_frete['VSD Categorias especiais 25% desconto outros'][i]
	        vsd_mais_de_79_outros = regras_frete['VSD Outros a partir R$ 79 com 50% desconto'][i]
	        vrp_categorias_especiais_full = regras_frete['VRP Categorias especiais 25% desconto FULL'][i]
	        vrp_mais_de_79_full = regras_frete['VRP Full a partir R$ 79 com 50% desconto'][i]
	        vrp_categorias_especiais_outros = regras_frete['VRP Categorias especiais 25% desconto outros'][i]
	        vrp_mais_de_79_outros = regras_frete['VRP Outros a partir R$ 79 com 50% desconto'][i]
	        asd_categorias_especiais_full = regras_frete['ASD Categorias especiais 25% desconto FULL'][i]
	        asd_mais_de_79_full = regras_frete['ASD Full a partir R$ 79 com 50% desconto'][i]
	        asd_categorias_especiais_outros = regras_frete['ASD Categorias especiais 25% desconto outros'][i]
	        asd_mais_de_79_outros = regras_frete['ASD Outros a partir R$ 79 com 50% desconto'][i]
	        arp_categorias_especiais_full = regras_frete['ARP Categorias especiais 25% desconto FULL'][i]
	        arp_mais_de_79_full = regras_frete['ARP Full a partir R$ 79 com 50% desconto'][i]
	        arp_categorias_especiais_outros = regras_frete['ARP Categorias especiais 25% desconto outros'][i]
	        arp_mais_de_79_outros = regras_frete['ARP Outros a partir R$ 79 com 50% desconto'][i]
	        rsd_full = regras_frete['RSD Full'][i]
	        rsd_outros = regras_frete['RSD Outros'][i]
	        rrp_full = regras_frete['RRP Full'][i]
	        rrp_outros = regras_frete['RRP Outros'][i]

	#REPUTAÇÃO VERDE
	if regiao == '1' and reputacao == '1' and full == '1' and especial == '1':
	    custo_frete = vsd_categorias_especiais_full
	elif regiao == '1' and reputacao == '1' and full == '1' and especial == '2':
	    custo_frete = vsd_mais_de_79_full
	elif regiao == '1' and reputacao == '1' and full == '2' and especial == '1':
	    custo_frete = vsd_categorias_especiais_outros
	elif regiao == '1' and reputacao == '1' and full == '2' and especial == '2':
	    custo_frete = vsd_mais_de_79_outros
	elif regiao == '2' and reputacao == '1' and full == '1' and especial == '1':
	    custo_frete = vrp_categorias_especiais_full
	elif regiao == '2' and reputacao == '1' and full == '1' and especial == '2':
	    custo_frete = vrp_mais_de_79_full
	elif regiao == '2' and reputacao == '1' and full == '2' and especial == '1':
	    custo_frete = vrp_categorias_especiais_outros
	elif regiao == '2' and reputacao == '1' and full == '2' and especial == '2':
	    custo_frete = vrp_mais_de_79_outros


	#REPUTAÇÃO AMARELA
	elif regiao == '1' and reputacao == '2' and full == '1' and especial == '1':
	    custo_frete = asd_categorias_especiais_full
	elif regiao == '1' and reputacao == '2' and full == '1' and especial == '2':
	    custo_frete = asd_mais_de_79_full
	elif regiao == '1' and reputacao == '2' and full == '2' and especial == '1':
	    custo_frete = asd_categorias_especiais_outros
	elif regiao == '1' and reputacao == '2' and full == '2' and especial == '2':
	    custo_frete = asd_mais_de_79_outros
	elif regiao == '2' and reputacao == '2' and full == '1' and especial == '1':
	    custo_frete = arp_categorias_especiais_full
	elif regiao == '2' and reputacao == '2' and full == '1' and especial == '2':
	    custo_frete = arp_mais_de_79_full
	elif regiao == '2' and reputacao == '2' and full == '2' and especial == '1':
	    custo_frete = arp_categorias_especiais_outros
	elif regiao == '2' and reputacao == '2' and full == '2' and especial == '2':
	    custo_frete = arp_mais_de_79_outros

	#REPUTAÇÃO VERMELHA
	elif regiao == '1' and reputacao == '3' and full == '1':
	    custo_frete = rsd_full
	elif regiao == '1' and reputacao == '3' and full == '2':
	    custo_frete = rsd_outros
	elif regiao == '2' and reputacao == '3' and full == '1':
	    custo_frete = rrp_full
	elif regiao == '2' and reputacao == '3' and full == '2':
	    custo_frete = rrp_outros

	#Modelo de cálculo clássico
	st.markdown('## Resultado')
	condicao = st.button('Calcular')

	if condicao == True:
		preço_final_classico = 0.01
		lucro_classico = 0

		while (lucro_classico / preço_final_classico) <= (margem_lucro_desejada / 100):
			if preço_final_classico <= preço_referencia:
				tarifa = tarifaML
				frete = 0
			else:
				tarifa = 0
				frete = custo_frete
			lucro_classico = preço_final_classico - preço_final_classico * MLC - custo - tarifa - frete
			preço_final_classico += 0.01

		lucro_classico = preço_final_classico - preço_final_classico * MLC - custo - tarifa - frete

		st.write('')
		st.write('###### O preço do anúncio Clássico deve ser R$', round(preço_final_classico,2),
			'\n ###### O valor do frete é de R$', round(frete,2),
			'\n ###### O valor da comissão é de R$', round(preço_final_classico * MLC + tarifa,2),
			'\n ###### O repasse do Mercado Livre será de R$', round(lucro_classico + custo,2),
			'\n ###### O lucro será de R$', round(lucro_classico,2),
			'\n ###### A margem de lucro é de ',round(lucro_classico/preço_final_classico * 100,2),'%')

		#Modelo de cálculo premium
		preço_final_premium = 0.01
		lucro_premium = 0

		while (lucro_premium / preço_final_premium)  <= (margem_lucro_desejada / 100):
			if preço_final_premium <= preço_referencia:
				tarifa = tarifaML
				frete = 0
			else:
				tarifa = 0
				frete = custo_frete
			lucro_premium = preço_final_premium - preço_final_premium * MLP - custo - tarifa - frete
			preço_final_premium += 0.01

		lucro_premium = preço_final_premium - preço_final_premium * MLP - custo - tarifa - frete

		st.write('--------------------------------------')
		st.write('###### O preço do anúncio Premium deve ser R$', round(preço_final_premium,2),
			'\n ###### O valor do frete é de R$', round(frete,2),
			'\n ###### O valor da comissão é de R$', round(preço_final_premium * MLP + tarifa,2),
			'\n ###### O repasse do Mercado Livre será de R$', round(lucro_premium + custo,2),
			'\n ###### O lucro será de R$', round(lucro_premium,2),
			'\n ###### A margem de lucro é de ',round(lucro_premium/preço_final_premium * 100,2),'%')

#Modelo de cálculo 3
if opcao == 'Modelo de cálculo 3':
	#Informações do produto
	st.markdown('## Informações do produto')
	#Custo
	custo = st.number_input('Qual o custo do produto R$',0.00)
	#Altura
	altura = st.number_input('Altura (cm)',0)
	#Largura
	largura = st.number_input('Largura (cm)',0)
	#Comprimento
	comprimento = st.number_input('Comprimento (cm)',0)
	#Peso
	peso_produto = st.number_input('Peso (g)',0)
	#Categoria especial
	especial = st.radio('É categoria especial?',['Sim','Não'])
	st.markdown('Para saber se a categoria é especial, acesse: <https://www.mercadolivre.com.br/ajuda/3922>')
	if especial == 'Sim':
		especial = '1'
	elif especial == 'Não':
		especial = '2'
	#Full
	full = st.radio('Qual o método de envio?',['Mercado Envios Coleta','Mercado Envios Full'])
	if full == 'Mercado Envios Full':
		full = '1'
	elif full == 'Mercado Envios Coleta':
		full = '2'

	#Informações do seller
	st.markdown('## Informações do seller')
	#Região de despacho
	regiao = st.radio('Região de despacho',['Sul / Sudeste','Restante do país'])
	if regiao == 'Sul / Sudeste':
		regiao = '1'
	elif regiao == 'Restante do país':
		regiao = '2'
	#Reputação
	reputacao = st.radio('Reputação',['Verde','Amarela','Laranja ou Vermelha'])
	if reputacao == 'Verde':
		reputacao = '1'
	elif reputacao == 'Amarela':
			reputacao = '2'
	elif reputacao == 'Laranja ou Vermelha':
			reputacao = '3'

	# Calculando o frete

	peso_produto = float(peso_produto / 1000)
	peso_volumetrico = float(largura * comprimento * altura / 6000 )

	if peso_produto > peso_volumetrico:
	    peso_para_calculo = peso_produto
	elif peso_produto <= peso_volumetrico:
	    peso_para_calculo = peso_volumetrico


	# Selecionando a tabela

	for i in range(0,len(regras_frete)):
	    if regras_frete['peso faixa inicial'][i] <= peso_para_calculo <= regras_frete['Peso faixa final'][i]:
	        vsd_categorias_especiais_full = regras_frete['VSD Categorias especiais 25% desconto FULL'][i]
	        vsd_mais_de_79_full = regras_frete['VSD Full a partir R$ 79 com 50% desconto'][i]
	        vsd_categorias_especiais_outros = regras_frete['VSD Categorias especiais 25% desconto outros'][i]
	        vsd_mais_de_79_outros = regras_frete['VSD Outros a partir R$ 79 com 50% desconto'][i]
	        vrp_categorias_especiais_full = regras_frete['VRP Categorias especiais 25% desconto FULL'][i]
	        vrp_mais_de_79_full = regras_frete['VRP Full a partir R$ 79 com 50% desconto'][i]
	        vrp_categorias_especiais_outros = regras_frete['VRP Categorias especiais 25% desconto outros'][i]
	        vrp_mais_de_79_outros = regras_frete['VRP Outros a partir R$ 79 com 50% desconto'][i]
	        asd_categorias_especiais_full = regras_frete['ASD Categorias especiais 25% desconto FULL'][i]
	        asd_mais_de_79_full = regras_frete['ASD Full a partir R$ 79 com 50% desconto'][i]
	        asd_categorias_especiais_outros = regras_frete['ASD Categorias especiais 25% desconto outros'][i]
	        asd_mais_de_79_outros = regras_frete['ASD Outros a partir R$ 79 com 50% desconto'][i]
	        arp_categorias_especiais_full = regras_frete['ARP Categorias especiais 25% desconto FULL'][i]
	        arp_mais_de_79_full = regras_frete['ARP Full a partir R$ 79 com 50% desconto'][i]
	        arp_categorias_especiais_outros = regras_frete['ARP Categorias especiais 25% desconto outros'][i]
	        arp_mais_de_79_outros = regras_frete['ARP Outros a partir R$ 79 com 50% desconto'][i]
	        rsd_full = regras_frete['RSD Full'][i]
	        rsd_outros = regras_frete['RSD Outros'][i]
	        rrp_full = regras_frete['RRP Full'][i]
	        rrp_outros = regras_frete['RRP Outros'][i]

	#REPUTAÇÃO VERDE
	if regiao == '1' and reputacao == '1' and full == '1' and especial == '1':
	    custo_frete = vsd_categorias_especiais_full
	elif regiao == '1' and reputacao == '1' and full == '1' and especial == '2':
	    custo_frete = vsd_mais_de_79_full
	elif regiao == '1' and reputacao == '1' and full == '2' and especial == '1':
	    custo_frete = vsd_categorias_especiais_outros
	elif regiao == '1' and reputacao == '1' and full == '2' and especial == '2':
	    custo_frete = vsd_mais_de_79_outros
	elif regiao == '2' and reputacao == '1' and full == '1' and especial == '1':
	    custo_frete = vrp_categorias_especiais_full
	elif regiao == '2' and reputacao == '1' and full == '1' and especial == '2':
	    custo_frete = vrp_mais_de_79_full
	elif regiao == '2' and reputacao == '1' and full == '2' and especial == '1':
	    custo_frete = vrp_categorias_especiais_outros
	elif regiao == '2' and reputacao == '1' and full == '2' and especial == '2':
	    custo_frete = vrp_mais_de_79_outros


	#REPUTAÇÃO AMARELA
	elif regiao == '1' and reputacao == '2' and full == '1' and especial == '1':
	    custo_frete = asd_categorias_especiais_full
	elif regiao == '1' and reputacao == '2' and full == '1' and especial == '2':
	    custo_frete = asd_mais_de_79_full
	elif regiao == '1' and reputacao == '2' and full == '2' and especial == '1':
	    custo_frete = asd_categorias_especiais_outros
	elif regiao == '1' and reputacao == '2' and full == '2' and especial == '2':
	    custo_frete = asd_mais_de_79_outros
	elif regiao == '2' and reputacao == '2' and full == '1' and especial == '1':
	    custo_frete = arp_categorias_especiais_full
	elif regiao == '2' and reputacao == '2' and full == '1' and especial == '2':
	    custo_frete = arp_mais_de_79_full
	elif regiao == '2' and reputacao == '2' and full == '2' and especial == '1':
	    custo_frete = arp_categorias_especiais_outros
	elif regiao == '2' and reputacao == '2' and full == '2' and especial == '2':
	    custo_frete = arp_mais_de_79_outros

	#REPUTAÇÃO VERMELHA
	elif regiao == '1' and reputacao == '3' and full == '1':
	    custo_frete = rsd_full
	elif regiao == '1' and reputacao == '3' and full == '2':
	    custo_frete = rsd_outros
	elif regiao == '2' and reputacao == '3' and full == '1':
	    custo_frete = rrp_full
	elif regiao == '2' and reputacao == '3' and full == '2':
	    custo_frete = rrp_outros

	#st.markdown(custo_frete)

	#Informando o modelo de cálculo
	#Informar o lucro desejado
	st.markdown('## Dados de entrada do modelo de cálculo')
	markup_produto = st.number_input('',1.00)
	st.markdown('Informe o markup desejado sobre o custo do produto.')
	if markup_produto == 0:
		st.warning('Cuidado! Você definiu 0 como markup.')
	elif 0 < markup_produto < 1:
		st.warning('Cuidado! Você definiu um valor menor do que 1 como markup')

	#Cálculo
	st.markdown('## Resultado')
	condicao = st.button('Calcular')

	if condicao == True:
		##Cálculo clássico
		preço_final_classico = 0.01
		lucro_classico = 0

		while (markup_produto * custo - custo) >= lucro_classico:
			if preço_final_classico <= preço_referencia:
				tarifa = tarifaML
				frete = 0
			else:
				tarifa = 0
				frete = custo_frete
			lucro_classico = preço_final_classico - preço_final_classico * MLC - custo - tarifa - frete
			preço_final_classico += 0.01

		lucro_classico = preço_final_classico - preço_final_classico * MLC - custo - tarifa - frete

		st.write('')
		st.write('###### O preço do anúncio Clássico deve ser R$', round(preço_final_classico,2),
			'\n ###### O valor do frete é de R$', round(frete,2),
			'\n ###### O valor da comissão é de R$', round(preço_final_classico * MLC + tarifa,2),
			'\n ###### O repasse do Mercado Livre será de R$', round(lucro_classico + custo,2),
			'\n ###### O lucro será de R$', round(lucro_classico,2),
			'\n ###### A margem de lucro é de ',round(lucro_classico/preço_final_classico * 100,2),'%')
		
		##Cálculo premium
		preço_final_premium = 0.01
		lucro_premium = 0

		while (markup_produto * custo - custo) >= lucro_premium:
			if preço_final_premium <= preço_referencia:
				tarifa = tarifaML
				frete = 0
			else:
				tarifa = 0
				frete = custo_frete
			lucro_premium = preço_final_premium - preço_final_premium * MLP - custo - tarifa - frete
			preço_final_premium += 0.01

		lucro_premium = preço_final_premium - preço_final_premium * MLP - custo - tarifa - frete

		st.write('--------------------------------------')
		st.write('###### O preço do anúncio Premium deve ser R$', round(preço_final_premium,2),
			'\n ###### O valor do frete é de R$', round(frete,2),
			'\n ###### O valor da comissão é de R$', round(preço_final_premium * MLP + tarifa,2),
			'\n ###### O repasse do Mercado Livre será de R$', round(lucro_premium + custo,2),
			'\n ###### O lucro será de R$', round(lucro_premium,2),
			'\n ###### A margem de lucro é de ',round(lucro_premium/preço_final_premium * 100,2),'%')

#Modelo de cálculo 4
if opcao == 'Modelo de cálculo 4':
	#Informações do produto
	st.markdown('## Informações do produto')
	#Custo
	custo = st.number_input('Qual o custo do produto R$',0.00)
	#Altura
	altura = st.number_input('Altura (cm)',0)
	#Largura
	largura = st.number_input('Largura (cm)',0)
	#Comprimento
	comprimento = st.number_input('Comprimento (cm)',0)
	#Peso
	peso_produto = st.number_input('Peso (g)',0)
	#Categoria especial
	especial = st.radio('É categoria especial?',['Sim','Não'])
	st.markdown('Para saber se a categoria é especial, acesse: <https://www.mercadolivre.com.br/ajuda/3922>')
	if especial == 'Sim':
		especial = '1'
	elif especial == 'Não':
		especial = '2'
	#Full
	full = st.radio('Qual o método de envio?',['Mercado Envios Coleta','Mercado Envios Full'])
	if full == 'Mercado Envios Full':
		full = '1'
	elif full == 'Mercado Envios Coleta':
		full = '2'

	#Informações do seller
	st.markdown('## Informações do seller')
	#Região de despacho
	regiao = st.radio('Região de despacho',['Sul / Sudeste','Restante do país'])
	if regiao == 'Sul / Sudeste':
		regiao = '1'
	elif regiao == 'Restante do país':
		regiao = '2'
	#Reputação
	reputacao = st.radio('Reputação',['Verde','Amarela','Laranja ou Vermelha'])
	if reputacao == 'Verde':
		reputacao = '1'
	elif reputacao == 'Amarela':
			reputacao = '2'
	elif reputacao == 'Laranja ou Vermelha':
			reputacao = '3'

	# Calculando o frete

	peso_produto = float(peso_produto / 1000)
	peso_volumetrico = float(largura * comprimento * altura / 6000 )

	if peso_produto > peso_volumetrico:
	    peso_para_calculo = peso_produto
	elif peso_produto <= peso_volumetrico:
	    peso_para_calculo = peso_volumetrico


	# Selecionando a tabela

	for i in range(0,len(regras_frete)):
	    if regras_frete['peso faixa inicial'][i] <= peso_para_calculo <= regras_frete['Peso faixa final'][i]:
	        vsd_categorias_especiais_full = regras_frete['VSD Categorias especiais 25% desconto FULL'][i]
	        vsd_mais_de_79_full = regras_frete['VSD Full a partir R$ 79 com 50% desconto'][i]
	        vsd_categorias_especiais_outros = regras_frete['VSD Categorias especiais 25% desconto outros'][i]
	        vsd_mais_de_79_outros = regras_frete['VSD Outros a partir R$ 79 com 50% desconto'][i]
	        vrp_categorias_especiais_full = regras_frete['VRP Categorias especiais 25% desconto FULL'][i]
	        vrp_mais_de_79_full = regras_frete['VRP Full a partir R$ 79 com 50% desconto'][i]
	        vrp_categorias_especiais_outros = regras_frete['VRP Categorias especiais 25% desconto outros'][i]
	        vrp_mais_de_79_outros = regras_frete['VRP Outros a partir R$ 79 com 50% desconto'][i]
	        asd_categorias_especiais_full = regras_frete['ASD Categorias especiais 25% desconto FULL'][i]
	        asd_mais_de_79_full = regras_frete['ASD Full a partir R$ 79 com 50% desconto'][i]
	        asd_categorias_especiais_outros = regras_frete['ASD Categorias especiais 25% desconto outros'][i]
	        asd_mais_de_79_outros = regras_frete['ASD Outros a partir R$ 79 com 50% desconto'][i]
	        arp_categorias_especiais_full = regras_frete['ARP Categorias especiais 25% desconto FULL'][i]
	        arp_mais_de_79_full = regras_frete['ARP Full a partir R$ 79 com 50% desconto'][i]
	        arp_categorias_especiais_outros = regras_frete['ARP Categorias especiais 25% desconto outros'][i]
	        arp_mais_de_79_outros = regras_frete['ARP Outros a partir R$ 79 com 50% desconto'][i]
	        rsd_full = regras_frete['RSD Full'][i]
	        rsd_outros = regras_frete['RSD Outros'][i]
	        rrp_full = regras_frete['RRP Full'][i]
	        rrp_outros = regras_frete['RRP Outros'][i]

	#REPUTAÇÃO VERDE
	if regiao == '1' and reputacao == '1' and full == '1' and especial == '1':
	    custo_frete = vsd_categorias_especiais_full
	elif regiao == '1' and reputacao == '1' and full == '1' and especial == '2':
	    custo_frete = vsd_mais_de_79_full
	elif regiao == '1' and reputacao == '1' and full == '2' and especial == '1':
	    custo_frete = vsd_categorias_especiais_outros
	elif regiao == '1' and reputacao == '1' and full == '2' and especial == '2':
	    custo_frete = vsd_mais_de_79_outros
	elif regiao == '2' and reputacao == '1' and full == '1' and especial == '1':
	    custo_frete = vrp_categorias_especiais_full
	elif regiao == '2' and reputacao == '1' and full == '1' and especial == '2':
	    custo_frete = vrp_mais_de_79_full
	elif regiao == '2' and reputacao == '1' and full == '2' and especial == '1':
	    custo_frete = vrp_categorias_especiais_outros
	elif regiao == '2' and reputacao == '1' and full == '2' and especial == '2':
	    custo_frete = vrp_mais_de_79_outros


	#REPUTAÇÃO AMARELA
	elif regiao == '1' and reputacao == '2' and full == '1' and especial == '1':
	    custo_frete = asd_categorias_especiais_full
	elif regiao == '1' and reputacao == '2' and full == '1' and especial == '2':
	    custo_frete = asd_mais_de_79_full
	elif regiao == '1' and reputacao == '2' and full == '2' and especial == '1':
	    custo_frete = asd_categorias_especiais_outros
	elif regiao == '1' and reputacao == '2' and full == '2' and especial == '2':
	    custo_frete = asd_mais_de_79_outros
	elif regiao == '2' and reputacao == '2' and full == '1' and especial == '1':
	    custo_frete = arp_categorias_especiais_full
	elif regiao == '2' and reputacao == '2' and full == '1' and especial == '2':
	    custo_frete = arp_mais_de_79_full
	elif regiao == '2' and reputacao == '2' and full == '2' and especial == '1':
	    custo_frete = arp_categorias_especiais_outros
	elif regiao == '2' and reputacao == '2' and full == '2' and especial == '2':
	    custo_frete = arp_mais_de_79_outros

	#REPUTAÇÃO VERMELHA
	elif regiao == '1' and reputacao == '3' and full == '1':
	    custo_frete = rsd_full
	elif regiao == '1' and reputacao == '3' and full == '2':
	    custo_frete = rsd_outros
	elif regiao == '2' and reputacao == '3' and full == '1':
	    custo_frete = rrp_full
	elif regiao == '2' and reputacao == '3' and full == '2':
	    custo_frete = rrp_outros

	#Informando o markup geral
	st.markdown('## Dados de entrada do modelo de cálculo')
	selecao_opcao = st.radio('O que você deseja informar?',['Markup geral','Percentual dos custos operacionais'])
	if selecao_opcao == 'Markup geral':
		markup_geral = st.number_input('',1.00)
		st.markdown('Informe o markup geral desejado sobre o custo do produto.')
		if markup_geral == 0:
			st.warning('Cuidado! Você definiu 0 como markup.')
		elif 0 < markup_geral < 1:
			st.warning('Cuidado! Você definiu um valor menor do que 1 como markup')

		#Cálculo
		st.markdown('## Resultado')
		condicao = st.button('Calcular')

		if condicao == True:

			#Cálculo clássico
			custos_seller = ((markup_geral - 1)/markup_geral)
			custos_com_comissão = custos_seller + MLC
			markup_calculo = 1/(1-custos_com_comissão)

			preço_mkp_previo = markup_calculo * custo

			if preço_mkp_previo <= preço_referencia:
				tarifa = tarifaML
				frete = 0
			else:
				tarifa = 0
				frete = custo_frete

			custos_não_variáveis = tarifa + frete + custo

			preço_mkpc = markup_calculo * custos_não_variáveis

			lucro_classico = preço_mkpc - preço_mkpc * MLC - custo - tarifa - frete

			preço_final_classico = preço_mkpc

			st.write('')
			st.write('###### O preço do anúncio Clássico deve ser R$', round(preço_final_classico,2),
				'\n ###### O valor do frete é de R$', round(frete,2),
				'\n ###### O valor da comissão é de R$', round(preço_final_classico * MLC + tarifa,2),
				'\n ###### O repasse do Mercado Livre será de R$', round(lucro_classico + custo,2),
				'\n ###### O lucro será de R$', round(lucro_classico,2),
				'\n ###### A margem de lucro é de ',round(lucro_classico/preço_final_classico * 100,2),'%')

			#Cálculo Premium
			custos_seller = ((markup_geral - 1)/markup_geral)
			custos_com_comissão = custos_seller + MLP
			markup_calculo = 1/(1-custos_com_comissão)

			preço_mkp_previo = markup_calculo * custo

			if preço_mkp_previo <= preço_referencia:
				tarifa = tarifaML
				frete = 0
			else:
				tarifa = 0
				frete = custo_frete

			custos_não_variáveis = tarifa + frete + custo

			preço_mkpp = markup_calculo * custos_não_variáveis

			lucro_premium = preço_mkpp - preço_mkpp * MLP - custo - tarifa - frete

			preço_final_premium = preço_mkpp

			st.write('--------------------------------------')
			st.write('###### O preço do anúncio Premium deve ser R$', round(preço_final_premium,2),
				'\n ###### O valor do frete é de R$', round(frete,2),
				'\n ###### O valor da comissão é de R$', round(preço_final_premium * MLP + tarifa,2),
				'\n ###### O repasse do Mercado Livre será de R$', round(lucro_premium + custo,2),
				'\n ###### O lucro será de R$', round(lucro_premium,2),
				'\n ###### A margem de lucro é de ',round(lucro_premium/preço_final_premium * 100,2),'%')

	else:
		custos_seller = st.number_input('Informe o percentual de custos operacionais.',0.00)/100
		
		if custos_seller == 0:
			st.warning('Cuidado! Você definiu 0% como custo operacional.')
		
		margem_liquida = st.number_input('Informe a margem líquida desejada.',0.00)/100
		if margem_liquida == 0:
			st.warning('Cuidado! Você definiu 0% como margem líquida desejada.')
		#Cálculo
		st.markdown('## Resultado')
		condicao = st.button('Calcular')

		if condicao == True:

			#Cálculo clássico
			custos_com_comissão = custos_seller + MLC + margem_liquida
			markup_calculo = 1/(1-custos_com_comissão)

			preço_mkp_previo = markup_calculo * custo

			if preço_mkp_previo <= preço_referencia:
				tarifa = tarifaML
				frete = 0
			else:
				tarifa = 0
				frete = custo_frete

			custos_não_variáveis = tarifa + frete + custo

			preço_mkpc = markup_calculo * custos_não_variáveis

			lucro_classico = preço_mkpc - preço_mkpc * MLC - custo - tarifa - frete

			preço_final_classico = preço_mkpc

			st.write('')
			st.write('###### O preço do anúncio Clássico deve ser R$', round(preço_final_classico,2),
				'\n ###### O valor do frete é de R$', round(frete,2),
				'\n ###### O valor da comissão é de R$', round(preço_final_classico * MLC + tarifa,2),
				'\n ###### O repasse do Mercado Livre será de R$', round(lucro_classico + custo,2),
				'\n ###### O lucro será de R$', round(lucro_classico,2),
				'\n ###### A margem de lucro é de ',round(lucro_classico/preço_final_classico * 100,2),'%')

			#Cálculo Premium
			custos_com_comissão = custos_seller + MLP + margem_liquida
			markup_calculo = 1/(1-custos_com_comissão)

			preço_mkp_previo = markup_calculo * custo

			if preço_mkp_previo <= preço_referencia:
				tarifa = tarifaML
				frete = 0
			else:
				tarifa = 0
				frete = custo_frete

			custos_não_variáveis = tarifa + frete + custo

			preço_mkpp = markup_calculo * custos_não_variáveis

			lucro_premium = preço_mkpp - preço_mkpp * MLP - custo - tarifa - frete

			preço_final_premium = preço_mkpp

			st.write('--------------------------------------')
			st.write('###### O preço do anúncio Premium deve ser R$', round(preço_final_premium,2),
				'\n ###### O valor do frete é de R$', round(frete,2),
				'\n ###### O valor da comissão é de R$', round(preço_final_premium * MLP + tarifa,2),
				'\n ###### O repasse do Mercado Livre será de R$', round(lucro_premium + custo,2),
				'\n ###### O lucro será de R$', round(lucro_premium,2),
				'\n ###### A margem de lucro é de ',round(lucro_premium/preço_final_premium * 100,2),'%')

#Modelo de cálculo 5
if opcao == 'Modelo de cálculo 5':
	#Informações do produto
	st.markdown('## Informações do produto')
	#Custo
	custo = st.number_input('Qual o custo do produto R$',0.00)
	#Altura
	altura = st.number_input('Altura (cm)',0)
	#Largura
	largura = st.number_input('Largura (cm)',0)
	#Comprimento
	comprimento = st.number_input('Comprimento (cm)',0)
	#Peso
	peso_produto = st.number_input('Peso (g)',0)
	#Categoria especial
	especial = st.radio('É categoria especial?',['Sim','Não'])
	st.markdown('Para saber se a categoria é especial, acesse: <https://www.mercadolivre.com.br/ajuda/3922>')
	if especial == 'Sim':
		especial = '1'
	elif especial == 'Não':
		especial = '2'
	#Full
	full = st.radio('Qual o método de envio?',['Mercado Envios Coleta','Mercado Envios Full'])
	if full == 'Mercado Envios Full':
		full = '1'
	elif full == 'Mercado Envios Coleta':
		full = '2'

	#Informações do seller
	st.markdown('## Informações do seller')
	#Região de despacho
	regiao = st.radio('Região de despacho',['Sul / Sudeste','Restante do país'])
	if regiao == 'Sul / Sudeste':
		regiao = '1'
	elif regiao == 'Restante do país':
		regiao = '2'
	#Reputação
	reputacao = st.radio('Reputação',['Verde','Amarela','Laranja ou Vermelha'])
	if reputacao == 'Verde':
		reputacao = '1'
	elif reputacao == 'Amarela':
			reputacao = '2'
	elif reputacao == 'Laranja ou Vermelha':
			reputacao = '3'

	# Calculando o frete

	peso_produto = float(peso_produto / 1000)
	peso_volumetrico = float(largura * comprimento * altura / 6000 )

	if peso_produto > peso_volumetrico:
	    peso_para_calculo = peso_produto
	elif peso_produto <= peso_volumetrico:
	    peso_para_calculo = peso_volumetrico


	# Selecionando a tabela

	for i in range(0,len(regras_frete)):
	    if regras_frete['peso faixa inicial'][i] <= peso_para_calculo <= regras_frete['Peso faixa final'][i]:
	        vsd_categorias_especiais_full = regras_frete['VSD Categorias especiais 25% desconto FULL'][i]
	        vsd_mais_de_79_full = regras_frete['VSD Full a partir R$ 79 com 50% desconto'][i]
	        vsd_categorias_especiais_outros = regras_frete['VSD Categorias especiais 25% desconto outros'][i]
	        vsd_mais_de_79_outros = regras_frete['VSD Outros a partir R$ 79 com 50% desconto'][i]
	        vrp_categorias_especiais_full = regras_frete['VRP Categorias especiais 25% desconto FULL'][i]
	        vrp_mais_de_79_full = regras_frete['VRP Full a partir R$ 79 com 50% desconto'][i]
	        vrp_categorias_especiais_outros = regras_frete['VRP Categorias especiais 25% desconto outros'][i]
	        vrp_mais_de_79_outros = regras_frete['VRP Outros a partir R$ 79 com 50% desconto'][i]
	        asd_categorias_especiais_full = regras_frete['ASD Categorias especiais 25% desconto FULL'][i]
	        asd_mais_de_79_full = regras_frete['ASD Full a partir R$ 79 com 50% desconto'][i]
	        asd_categorias_especiais_outros = regras_frete['ASD Categorias especiais 25% desconto outros'][i]
	        asd_mais_de_79_outros = regras_frete['ASD Outros a partir R$ 79 com 50% desconto'][i]
	        arp_categorias_especiais_full = regras_frete['ARP Categorias especiais 25% desconto FULL'][i]
	        arp_mais_de_79_full = regras_frete['ARP Full a partir R$ 79 com 50% desconto'][i]
	        arp_categorias_especiais_outros = regras_frete['ARP Categorias especiais 25% desconto outros'][i]
	        arp_mais_de_79_outros = regras_frete['ARP Outros a partir R$ 79 com 50% desconto'][i]
	        rsd_full = regras_frete['RSD Full'][i]
	        rsd_outros = regras_frete['RSD Outros'][i]
	        rrp_full = regras_frete['RRP Full'][i]
	        rrp_outros = regras_frete['RRP Outros'][i]

	#REPUTAÇÃO VERDE
	if regiao == '1' and reputacao == '1' and full == '1' and especial == '1':
	    custo_frete = vsd_categorias_especiais_full
	elif regiao == '1' and reputacao == '1' and full == '1' and especial == '2':
	    custo_frete = vsd_mais_de_79_full
	elif regiao == '1' and reputacao == '1' and full == '2' and especial == '1':
	    custo_frete = vsd_categorias_especiais_outros
	elif regiao == '1' and reputacao == '1' and full == '2' and especial == '2':
	    custo_frete = vsd_mais_de_79_outros
	elif regiao == '2' and reputacao == '1' and full == '1' and especial == '1':
	    custo_frete = vrp_categorias_especiais_full
	elif regiao == '2' and reputacao == '1' and full == '1' and especial == '2':
	    custo_frete = vrp_mais_de_79_full
	elif regiao == '2' and reputacao == '1' and full == '2' and especial == '1':
	    custo_frete = vrp_categorias_especiais_outros
	elif regiao == '2' and reputacao == '1' and full == '2' and especial == '2':
	    custo_frete = vrp_mais_de_79_outros


	#REPUTAÇÃO AMARELA
	elif regiao == '1' and reputacao == '2' and full == '1' and especial == '1':
	    custo_frete = asd_categorias_especiais_full
	elif regiao == '1' and reputacao == '2' and full == '1' and especial == '2':
	    custo_frete = asd_mais_de_79_full
	elif regiao == '1' and reputacao == '2' and full == '2' and especial == '1':
	    custo_frete = asd_categorias_especiais_outros
	elif regiao == '1' and reputacao == '2' and full == '2' and especial == '2':
	    custo_frete = asd_mais_de_79_outros
	elif regiao == '2' and reputacao == '2' and full == '1' and especial == '1':
	    custo_frete = arp_categorias_especiais_full
	elif regiao == '2' and reputacao == '2' and full == '1' and especial == '2':
	    custo_frete = arp_mais_de_79_full
	elif regiao == '2' and reputacao == '2' and full == '2' and especial == '1':
	    custo_frete = arp_categorias_especiais_outros
	elif regiao == '2' and reputacao == '2' and full == '2' and especial == '2':
	    custo_frete = arp_mais_de_79_outros

	#REPUTAÇÃO VERMELHA
	elif regiao == '1' and reputacao == '3' and full == '1':
	    custo_frete = rsd_full
	elif regiao == '1' and reputacao == '3' and full == '2':
	    custo_frete = rsd_outros
	elif regiao == '2' and reputacao == '3' and full == '1':
	    custo_frete = rrp_full
	elif regiao == '2' and reputacao == '3' and full == '2':
	    custo_frete = rrp_outros


	#Informando os dados de entrada
	st.markdown('## Dados de entrada do modelo de cálculo')
	preço_classico = st.number_input('Informe o valor de venda do anúncio clássico',0.00)
	preço_premium = st.number_input('informe o valor de venda do anúncio premium',0.00)

	#Cálculo
	st.markdown('## Resultado')
	condicao = st.button('Calcular')

	if condicao == True:
		if preço_classico > 0 or preço_premium > 0:
			#Cálculo clássico
			
			if preço_classico <= preço_referencia:
				tarifa = tarifaML
				frete = 0
			else:
				tarifa = 0
				frete = custo_frete

			lucro_classico = preço_classico - preço_classico * MLC - custo - tarifa - frete


			if lucro_classico < 0:
				st.write('')
				st.write('###### Preço de venda do anúncio Clássico R$', round(preço_classico,2),
					'\n ###### O valor do frete é de R$', round(frete,2),
					'\n ###### O valor da comissão é de R$', round(preço_classico * MLC + tarifa,2),
					'\n ###### O repasse do Mercado Livre será de R$', round(lucro_classico + custo,2),
					'\n ###### O prejuízo será de R$', round(lucro_classico,2),
					'\n ###### O percentual do prejuízo é de ',round(lucro_classico/preço_classico * 100,2),'%')
				st.error('Valor de venda com prejuízo')
			else:
				st.write('')
				st.write('###### Preço de venda do anúncio Clássico R$', round(preço_classico,2),
					'\n ###### O valor do frete é de R$', round(frete,2),
					'\n ###### O valor da comissão é de R$', round(preço_classico * MLC + tarifa,2),
					'\n ###### O repasse do Mercado Livre será de R$', round(lucro_classico + custo,2),
					'\n ###### O lucro será de R$', round(lucro_classico,2),
					'\n ###### A margem de lucro é de ',round(lucro_classico/preço_classico * 100,2),'%')
			
			#Calculo Premium
			if preço_premium <= preço_referencia:
				tarifa = tarifaML
				frete = 0
			else:
				tarifa = 0
				frete = custo_frete

			lucro_premium = preço_premium - preço_premium * MLP - custo - tarifa - frete


			if lucro_premium < 0:
				st.write('--------------------------------------')
				st.write('###### Preço de venda do anúncio Premium R$', round(preço_premium,2),
					'\n ###### O valor do frete é de R$', round(frete,2),
					'\n ###### O valor da comissão é de R$', round(preço_premium * MLP + tarifa,2),
					'\n ###### O repasse do Mercado Livre será de R$', round(lucro_premium + custo,2),
					'\n ###### O prejuízo será de R$', round(lucro_premium,2),
					'\n ###### O percentual do prejuízo é de ',round(lucro_premium/preço_premium * 100,2),'%')
				st.error('Valor de venda com prejuízo')
			else:
				st.write('--------------------------------------')
				st.write('###### Preço de venda do anúncio Premium R$', round(preço_premium,2),
					'\n ###### O valor do frete é de R$', round(frete,2),
					'\n ###### O valor da comissão é de R$', round(preço_premium * MLP + tarifa,2),
					'\n ###### O repasse do Mercado Livre será de R$', round(lucro_premium + custo,2),
					'\n ###### O lucro será de R$', round(lucro_premium,2),
					'\n ###### A margem de lucro é de ',round(lucro_premium/preço_premium * 100,2),'%')

		else:
			st.error('Informe um valor de venda diferente de R$0,00 para o anúncio clássico e também para o premium.')
