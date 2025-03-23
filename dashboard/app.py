import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import base64
import io
from PIL import Image
from scripts.estimativa_tinta import calcular_area_impressao

# Inicializa o aplicativo Dash
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Estimativa de Tinta para Impressão", style={'textAlign': 'center'}),
    
    # Componente para upload de imagem
    dcc.Upload(
        id='upload-image',
        children=html.Button('Carregar Imagem'),
        multiple=False
    ),
    
    # Div para exibir os resultados
    html.Div(id='output-data-upload'),
])

# Callback para processar o upload e mostrar os resultados
@app.callback(
    Output('output-data-upload', 'children'),
    Input('upload-image', 'contents')
)
def update_output(contents):
    if contents is None:
        return "Por favor, carregue uma imagem."
    
    # Decodificar a imagem enviada (formato base64)
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    img = Image.open(io.BytesIO(decoded))
    
    # Executar a função de cálculo da área de impressão
    preta, colorida = calcular_area_impressao(img)
    
    return html.Div([
        html.P(f"Tinta preta estimada: {preta:.2f}%"),
        html.P(f"Tinta colorida estimada: {colorida:.2f}%")
    ])

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
