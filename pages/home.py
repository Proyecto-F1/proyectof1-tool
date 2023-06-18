from dash import html
import dash

dash.register_page(__name__, path='/')

layout = html.Div(
    className='flex justify-center flex-col space-y-4 items-center h-screen',
    children=[
        html.H1('Predicción de resultados de F1', className='text-4xl'),
        html.Div(
            className='flex justify-center items-center',
            children=[
                html.Img(
                    className='w-2/3',
                    src='https://proyectof1.com/wp-content/uploads/2023/06/Proyecto-F1-1.png',
                ),
            ],
        ),
        html.Div(
            className='flex justify-center items-center space-x-4 flex-row',
            children=[
                html.Div(
                    className="flex space-x-4",
                    children=[
                        html.A(
                            className="text-gray-500 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium",
                            href="/predictions",
                            children="Predictions",
                        ),
                        html.A(
                            className="text-gray-500 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium",
                            href="/circuits",
                            children="Circuits",
                        ),
                        html.A(
                            className="text-gray-500 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium",
                            href="/drivers",
                            children="Drivers",
                        ),
                        html.A(
                            className="text-gray-500 hover:bg-gray-700 hover:text-white px-3 py-2 rounded-md text-sm font-medium",
                            href="/teams",
                            children="Teams",
                        ),
                    ],

                )
            ],
        ),
    ],
)
