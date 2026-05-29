import copy
import funcoes

    ### Adicionando os caminhos dos arquivos em variaveis ###
csv_orders = 'datasets/olist_orders_dataset.csv'
csv_products = 'datasets/olist_products_dataset.csv'



####################################################################
########              Importar CSV                          ########       
####################################################################

### Lista de Dicionarios (ld) ###
ld_produtos = funcoes.import_csv(csv_products)
ld_pedidos = funcoes.import_csv(csv_orders)

####################################################################
########              1. Validação e tratamento             ########
########                  de dados ausente.                 ########
########                        COM                         ######## 
########              2. Padronizaçâo de Strings            ########
########                  e Regex                           ########
####################################################################
print("\n"+"*"*100)
print("*** Iniciando Analise")
print("*"*100)


print("\n"+"*"*100)
### Mostrando as chave do dicionario ###
print(f"Chaves do dicionário: {ld_produtos[0].keys()}")
print("*"*100)

print("\n"+"*"*100)
### Primeiro tratamento com lower, strip e regex na coluna 'product_category_name'###
print ("Tratando coluna Nome de Categoria de Produtos com Strip, Lower e Regex.")
ld_produtos_trat = funcoes.tratar_coluna_strip_lower_regex(ld_produtos, 'product_category_name')
print("*"*100)

print("\n"+"*"*100)
### Segundo tratamento de "sem categoria" ###
print ("Tratando coluna Nome de Categoria de Produtos alterando nulos ou string vazias por 'sem categoria'.")
ld_produtos_trat, cont_sem_categoria= funcoes.tratar_nulos_vazios_para_sem_categoria(ld_produtos, 'product_category_name')
print("*"*100)

print("\n"+"*"*100)
### Visualizando quantos valores nulos e quais as linhas que eles se encontram e retorna     ###
### uma lista com os idices das linhas e atribui a variavel linhas_nulas                     ###
print("Verificando e mostrando a seguir valores indesejados nas categorias peso, comprimento, altura ou largura.")
linhas_nulas = funcoes.verificar_nulos(ld_produtos, ['product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm'])
print("*"*100)

print("\n"+"*"*100)
### Verificar e printar se as linhas que tem valores indesejados(nulos, vazios e etc) tem    ###
###  o mesmo id de produto com outra linha                                                   ###
cont = funcoes.verificador_id_produto_repete(ld_produtos_trat, linhas_nulas)
print(f"Verificando quantas vezes o ID_Produto das linhas nulas se repete na tebela(Linha/Quantidade): {cont}")
print("*"*100)

print("\n"+"*"*100)
### Como identifiquei poucas linhas com valores indesejados e não achei relacão direta com outras linhas  ###
### Decidi que a melhor opção era deleta-las                                                              ###
### Motivo: acredito que o PESO e MEDIDAS do produtos sao cruciais para calcular os custos operacionais   ###
ld_produtos_limpo = funcoes.exclui_linhas(ld_produtos_trat, linhas_nulas)
print("Como não identifiquei relacão com outro produto, decidimos excluir as linhas")
print("Mostrando as linhas com nulos após a limpeza")
funcoes.verificar_nulos(ld_produtos, ['product_weight_g', 'product_length_cm', 'product_height_cm', 'product_width_cm'])
print("*"*100)

####################################################################
########              3. Logica de Regra de Negócio         ########
########                 (Filtros e Validação)              ########
####################################################################

print("\n"+"*"*100)
### lista_entrega_vazia recebe uma lista com os indices da linhas que tem a data de entrega vazia ###
lista_entrega_vazia = funcoes.verifica_entregas_vazias(ld_pedidos, 'order_delivered_customer_date')
print(f"Numeros de data de entregas vaizos/nulos: {len(lista_entrega_vazia)}")
print("*"*100)

print("\n"+"*"*100)
### lista_relacao_status_pedido vai receber os que tem o status do pedido cancelado,                         ###
###    provando quantos tem relação por não ter data de entrega.                                             ###
lista_relacao_status_pedido = funcoes.comparar_entrega_vazia_com_status_do_pedido(ld_pedidos, lista_entrega_vazia, 'order_status')
print(f"Quantos tem data de entrega vazia por ter o pedido Cancelado: {len(lista_relacao_status_pedido)}")
print("*"*100)

####################################################################
########              4. Formatação Temporal(datetime)      ########
####################################################################

ld_pedidos_data_modificada = funcoes.converter_coluna_de_datas(copy.deepcopy(ld_pedidos), 'order_approved_at')

####################################################################
########              5.Sumario Estatistico                 ########
####################################################################

percentage = (len(lista_relacao_status_pedido) / len(lista_entrega_vazia)) * 100
print("\n")
print("="*34)
print('===           RESUMO           ===')
print("="*34)
print(f'Total de pedidos: {len(ld_pedidos)}')
print(f'Total de produtos: {len(ld_produtos)}')
print(f'Quantidade de Produtos sem categoria: {cont_sem_categoria}')
print(f'Quantidade de Produtos com dimensões fisicas nulas: {len(linhas_nulas)}')
print(f'Quantidade de linhas DELETADAS de Produtos com dimensões fisicas nulas: {len(linhas_nulas)}')
print(f'Pedidos cancelados: {len(lista_relacao_status_pedido)}')
print(f'Data de Entrega vazia: {len(lista_entrega_vazia)}')
print(f'% de entregas vazias por pedido cancelado: {percentage:.2f}%')
print(f'% de entregas vazias por outros motivos: {(100-percentage):.2f}%')
print(f'Formatação de data: Formato Antes: {ld_pedidos[0]['order_approved_at']}. Formato Atual: {ld_pedidos_data_modificada[0]['order_approved_at']}.')
print("="*34)