from dash import html
import dash_bootstrap_components as dbc
import base64

# Cargar la imagen como un archivo binario
with open('frontend\Imagenes\CANAL2.jpg', 'rb') as img_file:
    encoded_img = base64.b64encode(img_file.read()).decode('ascii')


variableA = dbc.Container([
    dbc.Row([
        dbc.Col(html.Img(src=f'data:image/png;base64,{encoded_img}', style={'width': '100%', 'height': 'auto'})),
        dbc.Col(html.H1('DISEÑA TU CANAL', style={'font-size': '36px'}), md=14, style={'background-color': 'skyblue'}, align="center"),
    ])
])