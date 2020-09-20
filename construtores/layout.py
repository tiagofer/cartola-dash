import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc


def create_navbar(logo=str,link=str):
    # navbar
    navbar = dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    # Use row and col to control vertical alignment of logo / brand
                    dbc.Row(
                        [
                            dbc.Col(html.Img(src=logo, height="50px")),
                            dbc.Col(dbc.NavbarBrand("", className="ml-5")),
                        ],
                        align="center",
                        no_gutters=True,
                    ),
                    href=link,
                ),
                dbc.NavbarToggler(id="navbar-toggler2"),
                dbc.Row(html.H3("Tutorial Cartola FC"),style={"color":"white"}),
            ]
        ),
        color="#DC6429",
        dark=False,
        className="mb-5",
    )

    return navbar

def create_controls(labels,ids):
    """Com base em uma lista de labels e ids, que devem ser do mesmo tamanho
    cria-se um menu dentro de um elemento do tipo card, contendo botões do tipo Dropdown

    Args:
        labels (array): Listagem com os nomes que serão exibidos no menu Ex.["Clube","Posição","Jogador"]
        ids (str): ids dos elementos Dropdown que serão criados, eles serão utilizados nos Callbacks

    Returns:
        dash_boostrap_component.Card: retorna um Card com o número de itens do Tipo DropDown igual a 
        quantidade de elemtos dos arrays passados como parâmetro
    """    
    controls = dbc.Card(
        [
                dbc.FormGroup(
                    [
                        dbc.Label(label),
                        dcc.Dropdown(
                            id=id
                        ),
                    ]
                )
            for label,id in zip(labels,ids) ],
        body=True,
        className="mt-5"
    )

    return controls