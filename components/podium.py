from dash import html, dcc
import dash
from dash import dash_table
import pandas as pd
from .styles import podium_block

drivers_df = pd.read_csv('../data/drivers.csv')

def podium_block_component(position, driver):
    comp = html.Div(
        className=podium_block % f'{position}/3',
        children=[
            html.Div(
                className='flex flex-col justify-center items-center space-y-4',
                children=[
                    html.P(
                        className='text-xl text-center font-bold text-gray-500',
                        children=f'Posición {position}',
                    ),
                    html.P(
                        className='text-xl text-center font-bold text-gray-500',
                        children=driver,
                    )
                ],
            ),
        ]
    ),

    return comp

def build_podium(results_df):
    names = []
    
    for driver in results_df[:3]:
        driver_df = drivers_df[drivers_df['driverId']
                               == results_df['driverId']]
        names.append(driver_df['forename'].values[0] + ' ' + driver_df['surname'].values[0])

    podium = html.Div(
        className='flex flex-col justify-center items-center space-y-4 h-full mt-12',
        children=[
            html.P(
                className='text-lg text-center font-bold text-gray-500',
                children='Predicción de podium',
            ),
            html.Div(
                className='grid grid-cols-3 items-end h-48 w-full',
                children=[
                    podium_block_component('2', names[1]),
                    podium_block_component('1', names[0]),
                    podium_block_component('3', names[2])
                ]
            ),
            dash_table.DataTable(
                id='results-table',
                columns=[{"name": i, "id": i} for i in results_df.columns],
                data=results_df.to_dict('records'),
                style_cell={
                    'textAlign': 'center',
                    'color': '#000000',
                    'font-family': 'sans-serif',
                    'font-size': '1.2rem',
                    'padding': '0.5rem 0.5rem'
                },
                style_header={
                    'fontWeight': 'bold',
                    'color': '#000000',
                    'font-family': 'sans-serif',
                    'font-size': '1.2rem',
                },
                export_format="csv",
            ),
        ],
    )

    return podium
