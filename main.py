# Hacer componente para añadir la clasificación y los datos para predecir todo
# Lanzar la predicción y mostrarla
# En la pantalla de dashbord seleccionar, tipo de datos(circuito, corredor..)

from dash import Dash, html, dcc
import dash
import plotly.express as px
import pandas as pd
import numpy as np
from components.nav import navbar
from dash.dependencies import Input, Output, State
from utils.utils import validate_prediction, build_prediction_df, predict_algorithm
from components.podium import build_podium
import os

app = Dash(
    __name__,
    serve_locally=True,
    external_scripts=[
        "https://cdn.tailwindcss.com?plugins=forms,typography,aspect-ratio,line-clamp"
    ],
    
    use_pages=True,
)

app.layout = html.Div(
    children=[
        navbar,
        dash.page_container
    ],
)

drivers_df = pd.read_csv('../data/drivers.csv')

@app.callback(
    Output('predictions-result', 'children'),
    Output('predictions-form', 'className'),
    Input('predict-button', 'n_clicks'),
    [
        State('qualifying_1', 'value'),
        State('qualifying_2', 'value'),
        State('qualifying_3', 'value'),
        State('qualifying_4', 'value'),
        State('qualifying_5', 'value'),
        State('qualifying_6', 'value'),
        State('qualifying_7', 'value'),
        State('qualifying_8', 'value'),
        State('qualifying_9', 'value'),
        State('qualifying_10', 'value'),
        State('qualifying_11', 'value'),
        State('qualifying_12', 'value'),
        State('qualifying_13', 'value'),
        State('qualifying_14', 'value'),
        State('qualifying_15', 'value'),
        State('qualifying_16', 'value'),
        State('qualifying_17', 'value'),
        State('qualifying_18', 'value'),
        State('qualifying_19', 'value'),
        State('qualifying_20', 'value'),
        State('temperature', 'value'),
        State('circuit', 'value'),
        State('precipitation', 'value'),
    ],
)
def predict(n_clicks,
            qualifying_1,
            qualifying_2,
            qualifying_3,
            qualifying_4,
            qualifying_5,
            qualifying_6,
            qualifying_7,
            qualifying_8,
            qualifying_9,
            qualifying_10,
            qualifying_11,
            qualifying_12,
            qualifying_13,
            qualifying_14,
            qualifying_15,
            qualifying_16,
            qualifying_17,
            qualifying_18,
            qualifying_19,
            qualifying_20,
            temperature,
            circuit,
            precipitation,
):
    result = {
        'qualifying': [
            qualifying_1,
            qualifying_2,
            qualifying_3,
            qualifying_4,
            qualifying_5,
            qualifying_6,
            qualifying_7,
            qualifying_8,
            qualifying_9,
            qualifying_10,
            qualifying_11,
            qualifying_12,
            qualifying_13,
            qualifying_14,
            qualifying_15,
            qualifying_16,
            qualifying_17,
            qualifying_18,
            qualifying_19,
            qualifying_20,
        ],
        'temperature': temperature,
        'circuit': circuit,
        'precipitation': precipitation,
    }

    validated = validate_prediction(result)

    if not validated:
        return '', 'lg:w-2/3 md:w-2/3 sm:w-3/4 w-full mx-auto'

    base_path = os.path.dirname(os.path.abspath(__file__))

    prediction_df = build_prediction_df(result)
    results = []
    model = pd.read_pickle(base_path + '/ml/model.sav')

    for index, row in prediction_df.iterrows():
        row_df = pd.DataFrame(row).transpose().reset_index(drop=True)
        prediction = model.predict(row_df.values)

        results.append(prediction)

    prediction_df['position'] = [int(x) for x in results]

    prediction_df = prediction_df.sort_values(by=['position'], ascending=True)

    return build_podium(prediction_df), 'hidden'

if __name__ == '__main__':
    app.run_server(debug=True)
