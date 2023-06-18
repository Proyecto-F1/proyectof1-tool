from dash import html
from .styles import a_link

nav_links = [
    {
        "href": "/predictions",
        "text": "Predictions",
    },
    {
        "href": "/circuits",
        "text": "Circuits",
    },
    {
        "href": "/drivers",
        "text": "Drivers",
    },
    {
        "href": "/teams",
        "text": "Teams",
    },
]

nav_elements = []

for element in nav_links:
    nav_component = html.A(
        className=a_link,
        href=element["href"],
        children=[
            element["text"]
        ],
    ),

    nav_elements.append(nav_component)

navbar = html.Nav(
    className="bg-gray-800 shadow-lg mx-auto px-2 sm:px-6 lg:px-8 ",
    children=[
        html.Div(
            className="flex justify-between items-center lg:w-2/3 md:w-2/3 sm:w-3/4 w-full mx-auto my-auto py-4",
            children=[
                html.A(
                    href="/",
                    children=[
                        html.Img(
                            className="h-16",
                            src="https://proyectof1.com/wp-content/uploads/2023/06/Proyecto_F1__4_-removebg-preview-1.png",
                            alt="Workflow",
                        ),
                    ],
                ),
                html.Div(
                    className="hidden sm:block sm:ml-6",
                    children=[
                        html.Div(
                            className="flex space-x-4",
                            children=[
                                html.A(
                                    className=a_link,
                                    href=element["href"],
                                    children=[
                                        element["text"]
                                    ],
                                )

                                for element in nav_links
                            ],
                        )
                    ],
                ),
            ],
        ),
    ],
)
