from dash.dependencies import Input, Output, State
#import helper.coleta_dados as cd
from app import app, cache
import plotly.express as px

import pandas as pd 
import numpy as np 

TIMEOUT = 60

@cache.memoize(timeout=TIMEOUT)
def fetch_github():
    #criando as urls para 7 rodadas
    urls = []
    for i in range(8):
        urls.append(f'https://raw.githubusercontent.com/henriquepgomide/caRtola/master/data/2020/rodada-{i+1}.csv')

    #criando lista de dataframes das rodadas
    rodadas = []
    for url in urls:
        rodadas.append(pd.read_csv(url))

    #remover coluna Unnamed: 0
    for rodada in rodadas:
        rodada.drop('Unnamed: 0',axis=1,inplace=True)

    #adicionando coluna DP até a rodada 3
    for i in range(3):
        rodadas[i]['DP'] = 0
    
    #criando dataframe com todas as rodadas
    df_rodadas = pd.DataFrame()
    try:
        for rodada in rodadas:
            df_rodadas = df_rodadas.append(rodada)
    except Exception as error:
        return error

    return df_rodadas

#criando dataframe com os dados das rodadas
df = fetch_github()

#criando a lista para o menu Dropdown com todos os clubes do campeonato
@app.callback(
    Output('drop-clube-01', 'options'),
    [Input('drop-clube-01', 'search_value')])
def set_clube_values(search_value):
    return [{'label': i, 'value': i} for i in df['atletas.clube.id.full.name'].unique()]

#criando a lista para o menu Dropdown com todas as posições do campeonato
@app.callback(
    Output('drop-posicao-01', 'options'),
    [Input('drop-posicao-01', 'search_value')])
def set_posicao_values(search_value):
    return [{'label': i, 'value': i} for i in df['atletas.posicao_id'].unique()]

#filtrando os jogadores pela posição e o clube
@app.callback(
    Output('drop-jogador-01', 'options'),
    [Input('drop-clube-01', 'value'),Input('drop-posicao-01', 'value')])
def set_jogador_values(clube,posicao):
    df_filtered = df[(df['atletas.clube.id.full.name']==clube) & (df['atletas.posicao_id']==posicao)]
    return [{'label': i, 'value': i} for i in df_filtered['atletas.apelido'].unique()]

#Callback para a exibição do gráfico com o histórico do jogador
@app.callback(
    Output('tab-01-scatter-pontos','figure'),
    [Input('drop-clube-01','value'), 
    Input('drop-posicao-01','value'),
    Input('drop-jogador-01','value')]
)
def update_scatter_jogador(clube,posicao,jogador):
    #Filtragem do dataframe
    df_filtered = df[(df['atletas.clube.id.full.name']==clube) & \
        (df['atletas.posicao_id']==posicao) & \
            (df['atletas.apelido']==jogador)]
    #O método retorna uma figura do Plotly Express
    return px.scatter(df_filtered,x="atletas.rodada_id",y="atletas.pontos_num",\
           #Cria uma linha de tendência, encaixada aos pontos
           trendline="ols",\
           #Muda o nome dos eixos X e Y
           labels={
               "atletas.rodada_id":"Rodadas", 
               "atletas.pontos_num":"Pontos" 
           }, \
           #Muda o Template para uma cor mais bonitinha :) 
           template="plotly_white",color_discrete_sequence=px.colors.qualitative.Set2)


#==========tab_02==========
@app.callback(
    Output('drop-clube-02', 'options'),
    [Input('drop-clube-02', 'search_value')])
def set_clube_values(search_value):
    return [{'label': i, 'value': i} for i in df['atletas.clube.id.full.name'].unique()]

@app.callback(
    Output('drop-posicao-02', 'options'),
    [Input('drop-posicao-02', 'search_value')])
def set_posicao_values(search_value):
    return [{'label': i, 'value': i} for i in df['atletas.posicao_id'].unique()]

@app.callback(
    Output('drop-jogador-02', 'options'),
    [Input('drop-clube-02', 'value'),Input('drop-posicao-02', 'value')])
def set_jogador_values(clube,posicao):
    df_filtered = df[(df['atletas.clube.id.full.name']==clube) & (df['atletas.posicao_id']==posicao)]
    return [{'label': i, 'value': i} for i in df_filtered['atletas.apelido'].unique()]

@app.callback(
    Output('tab-02-scatter-valorizacao','figure'),
    [Input('drop-clube-02','value'), 
    Input('drop-posicao-02','value'),
    Input('drop-jogador-02','value')]
)
def update_scatter_jogador_preco(clube,posicao,jogador):
    df_filtered = df[(df['atletas.clube.id.full.name']==clube) & \
        (df['atletas.posicao_id']==posicao) & \
            (df['atletas.apelido']==jogador)]
    return px.scatter(df_filtered,x="atletas.rodada_id",y="atletas.variacao_num",\
           trendline="ols",\
           labels={
               "atletas.rodada_id":"Rodadas", 
               "atletas.variacao_num":"Variação de Preço" 
           }, \
           template="plotly_white",color_discrete_sequence=px.colors.qualitative.Set2)