# SCTEC - Mini Projeto Avaliativo Módulo 1 - Semana 07

## 1. Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos de análise e tratamento de dados utilizando Python.

Os datasets utilizados pertencem ao conjunto de dados da Olist, contendo informações de produtos e pedidos de um e-commerce.

O pipeline segue o seguinte fluxo:

1. Importação de arquivos CSV;
2. Limpeza e tratamento de dados;
3. Padronização de strings;
4. Tratamento de valores nulos;
5. Aplicação de regras de negócio;
6. Conversão e formatação de datas;
7. Criação de sumário estatístico.

---

## 2. Estrutura do Projeto

```text
SCTEC-miniprojeto-Modulo1-semana07-Olist/
│
├── funcoes.py
├── main.py
├── README.md
│
└── datasets/
         ├── olist_orders_dataset.csv
         └── olist_products_dataset.csv
```

---

## 3. Imports Utilizados

* Python 3
* csv
* re (Regex)
* datetime
* copy.deepcopy

---

## 4. Fluxo do Projeto

### 4.1 Importação de CSV

Leitura de datasets utilizando `csv.DictReader`, convertendo os dados para listas de dicionários.

### 4.2 Tratamento de Strings

Padronização da coluna `product_category_name` aplicando:

* `lower()`
* `strip()`
* remoção de caracteres especiais utilizando Regex

### 4.3 Tratamento de Valores Nulos

Substituição de categorias vazias por:

```python
"sem categoria"
```

### 4.4 Validação de Dados Numéricos

Verificação dos campos:

* peso;
* comprimento;
* altura;
* largura.

Foram considerados inválidos:

* valores vazios;
* nulos;
* zero;
* negativos.

### 4.5 Regra de Negócio

Análise da relação entre:

* pedidos cancelados;
* ausência de data de entrega.

Objetivo:

Identificar se pedidos sem data de entrega possuem relação com cancelamentos.

Conclusão:

Apenas 20,88% de ausência dos valores de data de entrega tem relação com o Pedido Cancelado, não sendo apenas ele trazendo essa causa.

### 4.6 Conversão de Datas

Conversão do formato:
```text
2017-07-11 14:58:04
```

Para:
```text
11/07/2017
```

Utilizando o módulo `datetime`.

### 4.7 Sumário Estatístico

Ao final da execução, o sistema apresenta informações como:

* total de pedidos;
* total de produtos;
* quantidade de produtos sem categoria;
* quantidade de linhas removidas;
* pedidos cancelados;
* porcentagem de entregas vazias.

---

## 5. Como Executar

### 5.1 Clonar o Repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 5.2 Entrar na Pasta do Projeto

```bash
cd SCTEC-miniprojeto-Modulo1-semana07-Olist
```

### 5.3 Executar o Projeto

```bash
python main.py
```

---

## 6. Principais Aprendizados

Durante o desenvolvimento deste projeto foram praticados conceitos importantes como:

* manipulação de listas e dicionários;
* modularização;
* criação de funções;
* validação de dados;
* tratamento de exceções;
* manipulação de datas;
* limpeza de datasets;
* lógica de negócio;
* organização de código.

---

## 7. Melhorias Futuras

* utilizar Pandas para otimizar o processamento;
* gerar gráficos estatísticos;
* exportar relatórios;
* criar testes automatizados;
* melhorar performance das verificações.

---

## 8. Autor

Projeto desenvolvido por Felipe Jacques Lazarotto como atividade avaliativa para programa SCTEC/SENAI.
