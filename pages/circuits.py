from dash import html
import dash
from components.next_phase import new_phase_comp

dash.register_page(__name__)

layout = new_phase_comp(
    h1='Dashboard de circuitos',
    message='En esta página se podrá ver un resumen de los circuitos de la F1 próximamente',
)
