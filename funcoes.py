import csv
import re
from datetime import datetime

    ### Função para importar os datasets, RETORNA o dicionario ###
def import_csv(caminho):
    with open(caminho, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)

    ### Função para TRATAR valores NULOS/VAZIOS na coluna PRODUCT_CATEGORY_NAME, RETORNA o dicionario atualizado ###
def tratar_nulos_vazios_para_sem_categoria(lista, coluna):
    contador = 0 
    for item in lista:
        ### Atribuirá 'sem categoria'se o valor for igual None, '', 0 ou False 
        if not item.get(coluna):
            item[coluna] = "sem categoria"
            contador = contador + 1 
    return lista, contador

    ### Função verifica e mostra os Indices das linhas e o conteudo delas, RETORNA a lista com os indices ###
    ### Considerei nulo, vazio, zero ou negativo como valores indesejados                                 ###
def verificar_nulos(lista, colunas): 
    ### Uma lista para guardar os indices das linhas ###
    linhas_nulas = []

    for indice, item in enumerate(lista):
        for coluna in colunas:
            valor = item.get(coluna)
            try:
                ### Aqui converto para float, caso não seja um numero quebrará o try ###
                valor = float(valor)

                ### Considerei que o tamanho e o peso não podem ser zero ou negativo como citei mais acima ###
                if valor <= 0:
                    ### adiciono o indice da linha na lista que sera retornado no final da funcao ###
                    linhas_nulas.append(indice)
                    break

            except (ValueError, TypeError):
                ### caso o try quebre por nao ser um numero, adiciono o indice da linha na lista que sera retornado no final###
                linhas_nulas.append(indice)
                break

    print(f'Total de linhas com nulos: {len(linhas_nulas)}')
    ### Caso não tenha nulos nao mostrar esses prints vazios ###
    if len(linhas_nulas) > 0:
        print(f'Indices das linhas com valores nulos: {linhas_nulas}')

        print('Mostrado conteudo de linhas com valores nulos:')
        for linha in linhas_nulas:
            print(f"Linha {linha}: {lista[linha]}")
    
    return linhas_nulas

    ### Verifica se o id do produto se repete, pois caso repetir podemos levar em ###
    ###   consideração que o produto terá o mesmo peso e dimenções                ###
def verificador_id_produto_repete(lista, linhas_nulas):

    contador = {}

    for indice in linhas_nulas:

        product_id = lista[indice]['product_id']

        contador[indice] = 0

        for indice2, item in enumerate(lista):
            if indice != indice2:
                if item['product_id'] == product_id:
                    contador[indice] += 1

    return contador

    ### Exclui linhas do dicionario ###
def exclui_linhas(lista, linhas_nulas):
    ### Usei o REVERSE=TRUE para que quado remover seja do maior para o menor ###
    for indice in sorted(linhas_nulas, reverse=True):
        lista.pop(indice)

    return lista

    ### Função para tratar letras maiusculas, espaços e caracteres especiais indesejados ###
def tratar_coluna_strip_lower_regex(lista, coluna):
    for item in lista:
        if item.get(coluna):
            ### Deixa todos os caracteres minisculos e remove os espaços ###
            item[coluna] = item[coluna].lower().strip()
            ### Remove caracteres: , . * + = ? ! : ; ###
            item[coluna] = re.sub(r'[,.*+=?!:;]', '',item[coluna])
    return lista

    ### Função que comapara se colua tem string vazio ou none, retornando uma lista dos indices das linhas ###
def verifica_entregas_vazias(lista, coluna):
    entrega_vazia = []
    for indice, linha in enumerate(lista):
        if linha[coluna] == '' or linha[coluna] is None:
            entrega_vazia.append(indice)
    return entrega_vazia

    ### Função verifica em uma lista, se as linhas especificas de uma coluna tem a string 'canceled',   ###
    ### Retornando uma lista com os indices das linhas que tiverem a expressao for verdadeira           ### 
def comparar_entrega_vazia_com_status_do_pedido(lista, linhas_nulas, coluna):
    relacao_status_pedido = []
    for indice in linhas_nulas:
            if lista[indice][coluna] == 'canceled' or lista[indice][coluna] is None:
                relacao_status_pedido.append(indice)
    return relacao_status_pedido

    ### Função corverte para data simplificada d/m/a ###
def converter_data_simples_dma(data):
    if data == '' or data is None:
        return None
    data_convertida = datetime.strptime(data, '%Y-%m-%d %H:%M:%S')
    return data_convertida.strftime('%d/%m/%Y')

    ### Funcao passa em toda uma coluna covertendo as datas ###
def converter_coluna_de_datas(lista, coluna):
    for linha in lista:
        linha[coluna] = converter_data_simples_dma(linha[coluna])
    return lista