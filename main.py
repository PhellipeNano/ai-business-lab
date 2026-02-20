# 1. Lista de vendas
# Cada item da lista é um produto com um custo e uma receira associada. O objetivo é calcular o lucro total e gerar um relatório de vendas.

vendas = [
    {"produto": "Camiseta", "receita": 120.00, "custo": 50.00},
    {"produto": "Calça Jeans", "receita": 250.00, "custo": 100.00},
    {"produto": "Tênis", "receita": 400.00, "custo": 200.00},
    {"produto": "Boné", "receita": 80.00, "custo": 30.00}
]

# 2. Função que calcula total
def calcular_total(lista_vendas, campo):
    #somar todos os valores do campo especificado em cada venda
    return sum(venda[campo] for venda in lista_vendas)

# 3. Função que calcula lucro
def calcular_lucro(receita, custo):
    #calcular o lucro subtraindo o custo da receita para cada venda
    return receita - custo 


print("               📊 RELATÓRIO DE VENDAS 📊               ")

#4. Gerar relatório de vendas
for venda in vendas:
  
    nome = venda['produto']
    rec = venda['receita']
    cus = venda['custo']
    
    lucro_item = calcular_lucro(rec, cus)
    
    # f-strings (f"..."): É o recurso de interpolação do Python.
    # Colocar o 'f' antes das aspas permite injetar variáveis diretamente usando chaves {}.
    # O :<12 significa "alinhe à esquerda usando 12 espaços".
    # O :>7.2f significa "alinhe à direita com 7 espaços, formate como 'float' com 2 casas decimais".
    print(f"Produto: {nome:<12} | Receita: R${rec:>7.2f} | Lucro: R${lucro_item:>7.2f}")

print("=" * 55)
print ("Total de Receita: R$", calcular_total(vendas, "receita"))
print ("Total de Custo: R$", calcular_total(vendas, "custo"))
print ("Total: R$", calcular_lucro(calcular_total(vendas, "receita"), calcular_total(vendas, "custo")))
print ("=" * 55)
