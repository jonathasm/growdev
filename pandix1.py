# Utilize o dataset contido nesse [link](https://www.kaggle.com/datasets/upadorprofzs/testes), e responda as questões
# abaixo.
#
# O dataset contém dados estatísticos do IBGE relativos à escolaridade, renda entre outros campos avaliados pela
# PNAD (Pesquisa Nacional por Amostra de Domicílios).
#
# Os dados podem representar informações relevantes e reveladoras sobre a distribuição de renda e possivelmente
# alguns indicadores sobre tais situações encontradas a partir dos dados.

# Exercícios

# Qual a quantidade de pessoas nas seguintes faixas etárias
# - 20 anos ou menos
# - 21 a 35 anos
# - 36 a 50 anos
# - 51 a 65 anos
# - maiores de 65 anos
import pandas as pd

df = pd.read_csv('dados.csv')
df.info()


def faixa_etaria(idade):
    return next((faixa for limite, faixa in [(20, '<20'), (35, '21-35'), (50, '36-50'), (65, '51-65')]
                 if idade <= limite), '>65')


df['Faixa Etária'] = df['Idade'].apply(faixa_etaria)

contagem = df['Faixa Etária'].value_counts()

contagem = contagem.reindex(['<20', '21-35', '36-50', '51-65', '>65'])

print(contagem)

# Qual é a média de escolaridade em cada faixa etária?
df['Anos Estudando'] = df['Anos de Estudo'] - 1
media_escolaridade = df.groupby('Faixa Etária')['Anos Estudando'].mean().astype(int)
media_escolaridade = media_escolaridade.reindex(['<20', '21-35', '36-50', '51-65', '>65'])
print(media_escolaridade)

# Qual a UF que concentra a maior renda?
uf_renda = df.groupby('UF')['Renda'].sum()
print(f'UF que concentra a maior renda é a UF Nº {uf_renda.idxmax()}')

# Qual a renda média de pessoas pretas e brancas de homens e mulheres?
media_renda = df.groupby(['Cor', 'Sexo'])['Renda'].mean().astype(int)
print('Renda média de pessoas pretas e brancas de homens e mulheres:')
print('Homem Preto:', media_renda[4][0])
print('Mulher Preta:', media_renda[4][1])
print('Homem Branco:', media_renda[2][0])
print('Mulher Branca:', media_renda[2][1])

# Qual a renda média concentrada em cada faixa etária?
media_renda_faixa_etaria = df.groupby('Faixa Etária')['Renda'].mean().astype(int)
media_renda_faixa_etaria = media_renda_faixa_etaria.reindex(['<20', '21-35', '36-50', '51-65', '>65'])
print('Renda média por faixa etária:')
print(media_renda_faixa_etaria)


# Qual a renda média nas faixas de anos de estudo abaixo?
# - 2 anos ou menos
# - 3 a 6 anos
# - 7 a 10 anos
# - 10 a 12 anos
# - 13 anos ou mais
def faixa_estudo(anos):
    faixas = [(2, '2 anos ou menos'),
              (6, '3 a 6 anos'),
              (10, '7 a 10 anos'),
              (12, '11 a 12 anos')]
    for limite, rotulo in faixas:
        if anos <= limite:
            return rotulo
    return '13 anos ou mais'


df['Faixa de Estudo'] = df['Anos Estudando'].apply(faixa_estudo)
media_renda_estudo = df.groupby('Faixa de Estudo')['Renda'].mean().astype(int)
media_renda_estudo = media_renda_estudo.reindex(['2 anos ou menos', '3 a 6 anos', '7 a 10 anos', '11 a 12 anos',
                                                 '13 anos ou mais'])
print('Renda média por faixa de anos de estudo:')
print(media_renda_estudo)

# Qual a escolaridade entre indígenas, para homens e mulheres?
media_escolaridade = df.groupby(['Cor', 'Sexo'])['Anos Estudando'].mean().astype(int)
print('Escolaridade média entre indígenas, para homens e mulheres:')
print('Homem Indígena:', media_escolaridade[0][0])
print('Mulher Indígena:', media_escolaridade[0][1])

# Qual a média de anos de estudo entre brancos e negros?
media_estudo = df.groupby('Cor')['Anos Estudando'].mean().astype(int)
print('Média de anos de estudo:')
print('Brancos:', media_estudo[2])
print('Negros:', media_estudo[4])


# Qual a média de anos de estudo e de renda para mulheres brancas, e para mulheres negras?
media_estudo_renda = df.groupby(['Cor', 'Sexo'])[['Anos Estudando', 'Renda']].mean().astype(int)

print('Média de anos de estudo e de renda:')
print('Mulher Branca - Anos de Estudo:', media_estudo_renda.loc[(2, 1), 'Anos Estudando'])
print('Mulher Branca - Renda:', media_estudo_renda.loc[(2, 1), 'Renda'])
print('Mulher Negra - Anos de Estudo:', media_estudo_renda.loc[(4, 1), 'Anos Estudando'])
print('Mulher Negra - Renda:', media_estudo_renda.loc[(4, 1), 'Renda'])

#  Qual é a UF com maior média de escolaridade e qual a UF com maior média de renda?
media_uf = df.groupby('UF')[['Anos Estudando', 'Renda']].mean()
uf_maior_escolaridade = media_uf['Anos Estudando'].idxmax()
uf_maior_renda = media_uf['Renda'].idxmax()
print(f'A UF com a maior média de escolaridade é a UF Nº {uf_maior_escolaridade}')
print(f'A UF com a maior média de renda é a UF Nº {uf_maior_renda}')

# Elabore você uma pergunta sobre a base de dados e escreva o código para responder a pergunta.
# Qual a UF com melhor proporção de mulheres em relação aos homens?
contagem_sexo = df.groupby(['UF', 'Sexo']).size().unstack()
proporcao_mulheres = contagem_sexo[1] / contagem_sexo[0]

uf_maior_proporcao_mulheres = proporcao_mulheres.idxmax()

print(f'A UF com a maior proporção de mulheres em relação aos homens é a UF Nº {uf_maior_proporcao_mulheres}')
