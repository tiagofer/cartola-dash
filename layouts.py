  
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import construtores.layout as cl

#inserindo a navbar
navbar = cl.create_navbar("https://img.utdstc.com/icons/cartolafc-android.png:225","#")
controles_01 = cl.create_controls(['Clube','Posição','Jogador'],['drop-clube-01','drop-posicao-01','drop-jogador-01'])
controles_02 = cl.create_controls(['Clube','Posição','Jogador'],['drop-clube-02','drop-posicao-02','drop-jogador-02'])

#ids dos gráficos
tab_01_scatter_pontos = 'tab-01-scatter-pontos'
tab_02_scatter_valorizacao = 'tab-02-scatter-valorizacao'

#criando a tab Pontuação
tab_01 =  html.Div(
    [
        dbc.Row(
            [
                dbc.Col(controles_01, md=4,className='mt-5'),
                dbc.Col(dcc.Graph(id=tab_01_scatter_pontos),md=8, className='mt-4')
            ]
        )
    ]
)  

#Criando a tab Valorização
tab_02 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(controles_02, md=4,className='mt-5'),
                dbc.Col(dcc.Graph(id=tab_02_scatter_valorizacao),md=8, className='mt-4')
            ]
        )
    ]
)


tabs = dbc.Tabs(
    [
        dbc.Tab(tab_01,label="Pontuação"),
        dbc.Tab(tab_02,label="Valorização")
    ]
)

#montagem do layout
layout = html.Div(
    [   
        #inserindo a navbar
        navbar,
        dbc.Container(
            [   
                tabs
            ]
        )
    ]
)

