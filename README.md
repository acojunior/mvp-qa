# MVP - Classificação de Câncer de Mama

## Descrição do Projeto

Este projeto tem como objetivo desenvolver um sistema completo de machine learning capaz de classificar tumores de mama como **benignos** ou **malignos**.

A solução foi construída como uma aplicação full stack, composta por:
- um modelo de machine learning treinado em notebook
- uma API backend em Python
- uma interface frontend para entrada de dados e visualização de resultados

---

## Dataset

Foi utilizado o dataset de câncer de mama disponível publicamente no Kaggle.

O dataset contém características extraídas de imagens médicas, como:
- raio
- textura
- perímetro
- área
- concavidade
- simetria

A variável alvo (`diagnosis`) indica:
- `0` → benigno
- `1` → maligno

---

## Modelagem

O problema foi tratado como uma tarefa de **classificação supervisionada**.

Foram avaliados os seguintes algoritmos:
- K-Nearest Neighbors (KNN)
- Árvore de Decisão
- Naive Bayes
- Support Vector Machine (SVM)

Também foram aplicadas técnicas de transformação:
- padronização (StandardScaler)
- normalização (MinMaxScaler)

Após comparação e otimização de hiperparâmetros com GridSearchCV, o melhor modelo foi:

**KNN com normalização**
- métrica: Manhattan
- n_neighbors: 13

---

## Avaliação

O modelo apresentou:

- Acurácia média (validação cruzada): ~0.95
- Acurácia no conjunto de teste: ~0.90

A diferença indica leve overfitting, porém o desempenho final foi considerado satisfatório para o problema.

---

## Teste Automatizado

Foi desenvolvido um teste utilizando **PyTest** para garantir que o modelo mantém um desempenho mínimo.

O teste valida que:

accuracy >= 0.88

### Executar o teste:

pytest

---

## Backend (Python)

O backend foi desenvolvido com Flask e é responsável por:
- carregar o modelo treinado
- receber dados via requisição HTTP
- retornar a predição

### Executar a API:

cd backend  
pip install -r requirements.txt  
python app.py

A API estará disponível em:

http://127.0.0.1:5000

---

## Frontend

O frontend foi desenvolvido em HTML, CSS e JavaScript puro.

Ele permite:
- inserir os dados manualmente
- enviar para a API
- visualizar o resultado da predição

### Executar:

Abra o arquivo:

frontend/index.html

---

## Integração

O fluxo da aplicação é:

Usuário → Frontend → API Flask → Modelo → Resultado

---

## Reflexão sobre Segurança

Por se tratar de um problema relacionado à saúde, a segurança e privacidade são aspectos fundamentais.

Caso os dados fossem reais, seria necessário:

- anonimizar informações sensíveis
- controlar acesso aos dados
- validar entradas para evitar dados inválidos ou maliciosos
- garantir comunicação segura entre frontend e backend

Além disso, o modelo deve ser utilizado apenas como ferramenta de apoio, não substituindo avaliação médica especializada.

---

## Como Executar o Projeto Completo

### 1. Backend

cd backend  
pip install -r requirements.txt  
python app.py

### 2. Frontend

Abra o arquivo:

frontend/index.html

---
