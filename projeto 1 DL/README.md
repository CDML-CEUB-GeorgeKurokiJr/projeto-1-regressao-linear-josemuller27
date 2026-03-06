# Análise de Renda e Escolaridade do Censo dos Estados Unidos

## Descrição do Projeto

Este projeto tem como objetivo analisar dados do Adult Census Dataset para investigar a relação entre nível educacional e renda nos Estados Unidos.

O foco principal da análise é responder à seguinte pergunta:

Quantas pessoas que não possuem ensino superior conseguem ganhar mais de 50 mil dólares por ano?

Além disso, o projeto também busca entender:

* Qual a porcentagem de pessoas sem faculdade que ganham mais de 50 mil dólares por ano
* A distribuição por sexo entre essas pessoas
* Possíveis padrões entre educação, renda e gênero

Essa análise permite compreender melhor como fatores educacionais influenciam o nível de renda da população.

---

# Base de Dados

O dataset utilizado é o Adult Census Income Dataset, amplamente utilizado em estudos de ciência de dados e machine learning.

Ele contém informações demográficas e socioeconômicas de indivíduos nos Estados Unidos.

Fonte oficial
https://archive.ics.uci.edu/ml/datasets/adult

Versão disponível no Kaggle
https://www.kaggle.com/datasets/uciml/adult-census-income

Características do dataset:

* Aproximadamente 32 mil registros
* 15 variáveis
* Mistura de dados categóricos e numéricos

Principais variáveis presentes na base:

* age: idade do indivíduo
* workclass: tipo de ocupação
* education: nível educacional
* occupation: profissão
* sex: sexo
* hours-per-week: horas trabalhadas por semana
* native-country: país de origem
* income: renda anual

A variável income possui duas categorias:

<=50K

> 50K

---

# Objetivo da Análise

O objetivo principal deste projeto é identificar e quantificar pessoas que ganham mais de 50 mil dólares por ano mesmo sem possuir ensino superior.

Para isso, o projeto realiza:

1. Limpeza dos dados
2. Filtragem das pessoas sem faculdade
3. Análise da renda dessas pessoas
4. Cálculo das porcentagens
5. Análise por sexo

---

# Etapas do Projeto

## Limpeza dos Dados

Primeiro foi realizada a limpeza do dataset.

As principais etapas foram:

* Remoção de valores ausentes representados por "?"
* Ajustes de formato das colunas
* Preparação dos dados para análise

---

## Filtragem de Pessoas Sem Faculdade

Foram consideradas como pessoas sem ensino superior os seguintes níveis educacionais:

* Preschool
* 1st-4th
* 5th-6th
* 7th-8th
* 9th
* 10th
* 11th
* 12th
* HS-grad
* Some-college

Essas categorias representam indivíduos que não possuem graduação completa.

---

## Identificação de Pessoas com Alta Renda

Após filtrar os indivíduos sem ensino superior, foi analisado quantos possuem renda superior a 50 mil dólares por ano.

Esse grupo foi identificado utilizando a variável income com valor:

> 50K

---

## Cálculo das Porcentagens

A análise final calcula:

* A porcentagem de pessoas sem ensino superior que ganham mais de 50 mil dólares por ano
* A distribuição por sexo dentro desse grupo

Isso permite observar quem consegue alcançar níveis de renda mais altos mesmo sem formação universitária.

---

# Tecnologias Utilizadas

O projeto foi desenvolvido utilizando as seguintes ferramentas:

* Python
* Pandas para manipulação de dados
* NumPy para cálculos numéricos
* Matplotlib para visualização de dados
* Seaborn para visualizações estatísticas
* Jupyter Notebook para desenvolvimento da análise

---

# Estrutura do Projeto

census-income-analysis

data
adult.csv

notebooks
censo_eua_analysis.ipynb

src
preprocessing.py

requirements.txt
README.md

---

# Como Executar o Projeto

1. Clone o repositório

git clone https://github.com/seu-usuario/census-income-analysis.git

2. Instale as dependências

pip install -r requirements.txt

3. Abra o notebook de análise

notebooks/censo_eua_analysis.ipynb

---

# Possíveis Extensões do Projeto

Este projeto pode ser expandido com novas análises, como:

* criação de modelos de machine learning para prever renda
* análise de importância das variáveis
* estudo da relação entre horas trabalhadas e renda
* construção de um dashboard interativo com Streamlit

---

# Autor

José Müller

Data Scientist
AI Analyst
Data Analyst

Principais habilidades:

Python
Machine Learning
Data Analysis
Data Visualization
NLP
SQL
