from dash import html, dcc
import dash
import pandas as pd
from utils.utils import get_circuits_options, get_drivers_options
import random
import numpy as np
from components.styles import input_container, container, label, input_style, btn_primary

dash.register_page(__name__)

form_fields = []
drivers_options = get_drivers_options()
circuits_options = get_circuits_options()

form_fields.append(
    html.Div(
        className='grid grid-cols-3 gap-x-4 my-8',
        children=[
            html.Div(
                className=input_container,
                children=[
                    html.P(
                        className=label,
                        children='Circuito',
                    ),
                    html.Div(
                        className=container,
                        children=[
                            dcc.Dropdown(
                                className='',
                                id='circuit',
                                options=circuits_options
                            )
                        ],
                    ),
                ],
            ),
            html.Div(
                className=input_container,
                children=[
                    html.P(
                        className=label,
                        children='Precipitaciones',
                    ),
                    html.Div(
                        className=container,
                        children=[
                            dcc.Input(
                                className=input_style,
                                id='precipitation',
                                type='number',
                                placeholder='Introduce la probabilidad de precipitaciones',
                            ),
                        ],
                    ),
                ],
            ),
            html.Div(
                className=input_container,
                children=[
                    html.P(
                        className=label,
                        children='Temperatura',
                    ),
                    html.Div(
                        className=container,
                        children=[
                            dcc.Input(
                                className=input_style,
                                id='temperature',
                                type='number',
                                placeholder='Introduce la temperatura',
                            ),
                        ],
                    ),
                ],
            ),
        ],
        
    ),
)

drivers_fields = []
drivers_id = random.sample(drivers_options, 20)

for i in range(1, 21):
    margin_top = '' if i % 2 != 0 else 'mt-12'

    drivers_fields.append(
        html.Div(
            className=f'p-4 border-red-500 border-t-4 border-l-4 border-r-4 {margin_top}',
            children=[
                html.Div(
                    className=input_container,
                    children=[
                        html.P(
                            className=label,
                            children=f'Posición {i}',
                        ),
                        html.Div(
                            className=container,
                            children=[
                                dcc.Dropdown(
                                    className='',
                                    id=f'qualifying_{i}',
                                    options=drivers_options,
                                    searchable=True,
                                    placeholder='Selecciona un piloto',
                                    value=drivers_id[i-1]['value']
                                )
                            ],
                        ),
                    ],
                ),
            ],
        ),
    )

form_fields.append(
    html.Div(
        className='grid grid-cols-2 gap-4',
        children=drivers_fields,
    ),
)

form_fields.append(
    html.Div(
        className='flex justify-center items-center my-12',
        children=[
            html.Button(
                className=btn_primary,
                children='Predecir',
                id='predict-button',
            ),
        ],
    ),
)

layout = html.Div(
    children=[
        html.Div(
            className=container,
            children=form_fields,
            id='predictions-form',
        ),
        html.Div(
            className=container,
            id='predictions-result',
        ),
    ],
)
