from dash import html, dcc
import dash_bootstrap_components as dbc
import base64



areadatosC = dbc.Container([
    html.H1("CANAL CIRCULAR"),
    html.H2("Propiedades Geométricas del canal"),

    # Valores de Entrada D y θ
    html.Div([
        html.Label("Valor de D"),
        dcc.Input(id="ValorD", type="number", placeholder="Ingrese el valor de D"),
    ]),
    
    html.Div([
        html.Label("Valor de θ"),
        dcc.Input(id="Valorθ", type="number", placeholder="Ingrese el valor de θ"),
        html.Br()
    ]),

    # Cálculo del área
    html.Div([
        html.Label("Área del Canal(m2):"),
        html.Label(id="Area_CanalC"),
    ]),
    
    # Cálculo del perímetro
    html.Div([
        html.Label("Perímetro mojado del Canal(m):"),
        html.Label(id="Perimetro_CanalC"),
    ]),
    
    # Cálculo del Radio Hidráulico
    html.Div([
        html.Label("Radio Hidráulico(m):"),
        html.Label(id="RH_CanalC"),
    ]),
    
    # Cálculo del Espejo de agua T
    html.Div([
        html.Label("Espejo de agua T(m):"),
        html.Label(id="T_CanalC"),
    ]),
])

import base64
# Cargar la imagen como un archivo binario
with open('frontend\Imagenes\CANALCIRCULAR.jpeg', 'rb') as img_file:
    encoded_img = base64.b64encode(img_file.read()).decode('ascii')



variableCC = dbc.Container([
     dbc.Row([
         html.Br(),
         dbc.Col([
             
             html.Label('SECCIÓN GEOMÉTRICA DEL CANAL', style={'font-size':'14'}),
             html.Img(src=f'data:image/png;base64,{encoded_img}', style={'width': '100%', 'height': '80%'}), 
                 html.Br(),]
                 
                          
, md=3, style={'textAlign': 'center', 'background-color': 'honeydew'}),
        
        dbc.Col(areadatosC, md=9, style={'textAlign': 'center'}),
    ])
])