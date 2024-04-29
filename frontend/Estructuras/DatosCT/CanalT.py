from dash import html, dcc
import dash_bootstrap_components as dbc
import base64



areadatosT = dbc.Container([
    html.H1("CANAL TRAPEZOIDAL"),
    html.H2("Propiedades Geométricas del canal"),

    # Valores de Entrada B, Y y Z
    html.Div([
        html.Label("Valor de B"),
        dcc.Input(id="valorB1", type="number", placeholder="Ingrese el valor de B"),
    ]),
    
    html.Div([
        html.Label("Valor de Y"),
        dcc.Input(id="valorY1", type="number", placeholder="Ingrese el valor de Y"),
    ]),

        html.Div([
        html.Label("Valor de Z"),
        dcc.Input(id="valorZ1", type="number", placeholder="Ingrese el valor de Z"),
        html.Br()
    ]),

    # Cálculo del área
    html.Div([
        html.Label("Área del Canal(m2):"),
        html.Label(id="Area_CanalT"),
    ]),
    
    # Cálculo del perímetro
    html.Div([
        html.Label("Perímetro del Canal(m):"),
        html.Label(id="Perimetro_CanalT"),
    ]),
    
    # Cálculo del Radio Hidráulico
    html.Div([
        html.Label("Radio Hidráulico(m):"),
        html.Label(id="RH_CanalT"),
    ]),
    
    # Cálculo del Espejo de agua T
    html.Div([
        html.Label("Espejo de agua T(m):"),
        html.Label(id="T_CanalT"),
    ]),
])


import base64
# Cargar la imagen como un archivo binario
with open('frontend\Imagenes\CANAL TRAPEZOIDAL.png', 'rb') as img_file:
    encoded_img = base64.b64encode(img_file.read()).decode('ascii')


variableCT = dbc.Container([
     dbc.Row([
         html.Br(),
         dbc.Col([
             
             html.Label('SECCIÓN GEOMÉTRICA DEL CANAL', style={'font-size':'14'}),
             html.Img(src=f'data:image/png;base64,{encoded_img}', style={'width': '100%', 'height': '80%'}),
                 html.Br(), 
                 html.Br(),
                 html.Br(),]
                 
                 
, md=3, style={'textAlign': 'center', 'background-color': 'honeydew'}),
         
        dbc.Col(areadatosT, md=9, style={'textAlign': 'center'}),
    ])
])