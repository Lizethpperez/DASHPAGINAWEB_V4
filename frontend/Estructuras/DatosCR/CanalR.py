from dash import html, dcc
import dash_bootstrap_components as dbc
from flask import Flask, render_template
import layout
from PIL import Image
import base64



areadatosr = dbc.Container([
    html.H1("CANAL RECTANGULAR"),
    html.H2("Propiedades Geométricas del canal"),

    # Valores de Entrada B y Y
    html.Div([
        html.Label("Valor de B"),
        dcc.Input(id="valorB", type="number", placeholder="Ingrese el valor de B"),
    ]),
    
    html.Div([
        html.Label("Valor de Y"),
        dcc.Input(id="valorY", type="number", placeholder="Ingrese el valor de Y"),
        html.Br()
    ]),

    # Cálculo del área
    html.Div([
        html.Label("Área del Canal(m2):"),
        html.Label(id="Area_CanalR"),
    ]),
    
    # Cálculo del perímetro
    html.Div([
        html.Label("Perímetro mojado del Canal(m):"),
        html.Label(id="Perimetro_CanalR"),
    ]),
    
    # Cálculo del Radio Hidráulico
    html.Div([
        html.Label("Radio Hidráulico(m):"),
        html.Label(id="RH_CanalR"),
    ]),
    
    # Cálculo del Espejo de agua T
    html.Div([
        html.Label("Espejo de agua T(m):"),
        html.Label(id="T_CanalR"),

    ]),
])



 
import base64
# Cargar la imagen como un archivo binario
with open('frontend\Imagenes\CANAL RECTANGULAR.png', 'rb') as img_file:
    encoded_img = base64.b64encode(img_file.read()).decode('ascii')

    

variableCR = dbc.Container([
     dbc.Row([
         html.Br(),
         dbc.Col([
             
             html.Label('SECCIÓN GEOMÉTRICA DEL CANAL', style={'font-size':'14'}),
             html.Img(src=f'data:image/png;base64,{encoded_img}', style={'width': '100%', 'height': '80%'}),
                 html.Br(), 
                 html.Br(),
                 html.Br(),]
             
             
             
, md=3, style={'textAlign': 'center', 'background-color': 'honeydew'},        
                 ),
        dbc.Col(areadatosr, md=9, style={'textAlign': 'center'}),  
        ])
    
    ])  

   
