import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import base64
import io
from PIL import Image
from scripts.estimativa_tinta import calcular_area_impressao  # Função para calcular a área de tinta

# Inicializa o aplicativo Dash
app = dash.Dash(__name__)

# Layout da aplicação
app.layout = html.Div([
    html.H1("Estimativa de Tinta para Impressão", style={'textAlign': 'center'}),
    
    # Componente para upload de imagem
    dcc.Upload(
        id='upload-image',
        children=html.Button('Carregar Imagem'),
        multiple=False  # Permite o upload de apenas uma imagem
    ),
    
    # Div para exibir os resultados após o cálculo
    html.Div(id='output-data-upload'),
])

# Função de callback para processar a imagem carregada
@app.callback(
    Output('output-data-upload', 'children'),
    Input('upload-image', 'contents')
)
def update_output(contents):
    if contents is None:
        return "Por favor, carregue uma imagem."
    
    # Decodificar a imagem enviada em formato base64
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    img = Image.open(io.BytesIO(decoded))
    
    # Chama a função para calcular a área de tinta
    preta, colorida = calcular_area_impressao(img)
    
    return html.Div([
        html.P(f"Tinta preta estimada: {preta:.2f}%"),
        html.P(f"Tinta colorida estimada: {colorida:.2f}%")
    ])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
