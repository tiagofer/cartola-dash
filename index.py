#importando as bibliotecas
import callbacks
#importando o layout criado no arquivo layouts.py
from layouts import layout
#importando a aplicação Dash
from app import app,server

#inicializa layout
app.layout = layout

#Código responsável pela execução da aplicação
if __name__ == "__main__":
    app.run_server(debug=False, port=8888)
