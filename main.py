from flask import Flask
import pandas as pd 


app = Flask(__name__)

tabela = pd.read_excel('Vendas - Dez.xlsx')

@app.route("/")
def fat():
    faturamento = float(tabela['Valor Final'].sum())
    return {"faturamento":faturamento}



@app.route("/vendas/produtos")
def vendas_produtos():
    tabela_vendas_produtos = tabela[['Produto', 'Valor Final']].groupby('Produto').sum()

    dic_todos_produtos = tabela_vendas_produtos.to_dict()
    return dic_todos_produtos



@app.route("/vendas/produtos/<produto>")
def fat_produto(produto):
    tabela_vendas_produtos = tabela[['Produto', 'Valor Final']].groupby('Produto').sum()
    if produto in tabela_vendas_produtos.index:
        vendas_produtos = tabela_vendas_produtos.loc[produto]
        dic_vendas_produto = vendas_produtos.to_dict()
        return dic_vendas_produto
    else:
        return {produto: 'Inexistente'}

app.run()