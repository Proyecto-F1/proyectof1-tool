from dash import html
from components.styles import container

def new_phase_comp(h1, message):
    next_phase = html.Div(
        className=f'{container} items-center justify-center flex flex-col h-screen space-y-4',
        children=[
            html.H1(
                className='text-4xl font-bold text-gray-500',
                children=h1,
            ),
            html.P(
                className='text-xl text-center text-gray-500',
                children=message,
            ),
        ],
    )

    return next_phase
