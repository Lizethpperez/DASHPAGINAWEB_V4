import dash
from dash import html, dcc
import dash_bootstrap_components as dbc 
import layout
import matplotlib.pyplot as plt
import base64
from dash.dependencies import Input, Output
import numpy as np



# Importamos los enlaces de las otras carpetas
from matplotlib import colors 
from frontend.Estructuras.area_superior.titulo import variableA
from frontend.Estructuras.area_subtitulos.subtitulos import variableB
from frontend.Estructuras.DatosCR.CanalR import areadatosr
from frontend.Estructuras.DatosCT.CanalT import areadatosT
from frontend.Estructuras.DatosCC.CanalC import areadatosC
from frontend.Estructuras.DatosCTR.CanalTR import areadatosTR




app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(variableA, md=12, style={'textAlign': 'center'}),
        dbc.Col(variableB, md=12,style={'background-color':'gold'}),

    ])
])


if __name__ == '__main__':
                        app.run_server(debug=True)
                        

#CANAL RECTANGULAR
 #importamos el frontend
app.layout == areadatosr
# Callback para actualizar los cálculos cuando se ingresan nuevos valores de B y Y
@app.callback(
    [dash.dependencies.Output("Area_CanalR", "children"),
      dash.dependencies.Output("Perimetro_CanalR", "children"),
      dash.dependencies.Output("RH_CanalR", "children"),
      dash.dependencies.Output("T_CanalR", "children")],
    [dash.dependencies.Input("valorB", "value"),
     dash.dependencies.Input("valorY", "value")],
)
def propiedadesCR(valorB,valorY):
    # Aquí se realizan los cálculos necesarios
    area = (valorB*valorY)  # Cálculo del área 
    perimetro = ((2*valorY)+valorB)  # Cálculo del perímetro
    radio_hidraulico = (valorB*valorY)/(valorB+(2*valorY)) # Cálculo del radio hidráulico
    espejo_agua_T =(valorB)  # Cálculo del espejo de agua T
    
    return str(area), str(perimetro), str(radio_hidraulico), str(espejo_agua_T)





#CANAL TRAPEZOIDAL
app.layout == areadatosT
# Callback para actualizar los cálculos cuando se ingresan nuevos valores de B y Y
@app.callback(
    [dash.dependencies.Output("Area_CanalT", "children"),
     dash.dependencies.Output("Perimetro_CanalT", "children"),
     dash.dependencies.Output("RH_CanalT", "children"),
     dash.dependencies.Output("T_CanalT", "children")],
    [dash.dependencies.Input("ValorB1", "value"),
     dash.dependencies.Input("ValorY1", "value"),
     dash.dependencies.Input("ValorZ1", "value")]
)
def PropiedadesT(valorB1, valorY1, valorZ1):
    # Aquí se realizan los cálculos necesarios
    area2 = (valorB1+(valorZ1 * valorY1))*valorY1  # Cálculo del área
    perimetro2 = valorB1+((2*valorY1)*(1-valorZ1^2) )^(1/2)  # Cálculo del perímetro
    radio_hidraulico2 = (valorZ1* valorY1)/(2*(1+valorZ1^2)^(1/2)) # Cálculo del radio hidráulico
    espejo_agua_T2 = 2*valorZ1*valorY1 # Cálculo del espejo de agua T
    
    return str(area2), str(perimetro2), str(radio_hidraulico2), str(espejo_agua_T2)


#CANAL CIRCULAR
app.layout == areadatosC
# Callback para actualizar los cálculos cuando se ingresan nuevos valores de B y Y
@app.callback(
    [dash.dependencies.Output("Area_CanalC", "children"),
     dash.dependencies.Output("Perimetro_CanalC", "children"),
     dash.dependencies.Output("RH_CanalC", "children"),
     dash.dependencies.Output("T_CanalC", "children")],
    [dash.dependencies.Input("ValorD", "value"),
     dash.dependencies.Input("Valorθ", "value")]
)
def PropiedadesT(ValorD, Valorθ):
    # Aquí se realizan los cálculos necesarios
    area3 = (((Valorθ*np.sin(Valorθ))*ValorD^2)/8) # Cálculo del área
    perimetro3 = (Valorθ*ValorD)/2  # Cálculo del perímetro
    radio_hidraulico3 = ((1*(np.sin(Valorθ)*Valorθ))*(ValorD/4)) # Cálculo del radio hidráulico
    espejo_agua_T3 = ((np.sin(Valorθ/2))*ValorD) # Cálculo del espejo de agua T
    
    return str(area3), str(perimetro3), str(radio_hidraulico3), str(espejo_agua_T3)

#CANAL TRIANGULAR
app.layout == areadatosTR
# Callback para actualizar los cálculos cuando se ingresan nuevos valores de B y Y
@app.callback(
    [dash.dependencies.Output("Area_CanalTR", "children"),
     dash.dependencies.Output("Perimetro_CanalTR", "children"),
     dash.dependencies.Output("RH_CanalTR", "children"),
     dash.dependencies.Output("T_CanalTR", "children")],
    [dash.dependencies.Input("ValorY2", "value"),
     dash.dependencies.Input("ValorZ2", "value")]
)
def PropiedadesT(ValorY2, ValorZ2):
    # Aquí se realizan los cálculos necesarios
    area4 = (ValorZ2*ValorY2^2) # Cálculo del área
    perimetro4 = (2*ValorY2)((1+ ValorZ2^2)^(1/2)) # Cálculo del perímetro
    radio_hidraulico4 = (ValorZ2*ValorY2)/(2*((1+ValorZ2^2)^(1/2))) # Cálculo del radio hidráulico
    espejo_agua_T4 = 2*ValorZ2*ValorY2 # Cálculo del espejo de agua T
    
    return str(area4), str(perimetro4), str(radio_hidraulico4), str(espejo_agua_T4)

if __name__ == '__main__':
    app.run_server(debug=True)
