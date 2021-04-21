from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
import dash_cytoscape as cyto
from dash.dependencies import Input, Output, State
import plotly.express as px
import requests
import SeedTaag.Class as C
import SeedTaag.Taagseed as tag



def defelements(M, R):
    elements = []
    for key in M:
        elements.append({'data': {'id': key, 'labelid': key}})
    for key in R:
        reactants = R[key].get_reactifs()
        products = R[key].get_products()
        reversible = R[key].getReversible()
        for reactant in reactants:
            for product in products:
                elements.append(
                    {'data': {'source': reactant, 'target': product}})
                if (reversible):
                    elements.append(
                        {'data': {'source': product, 'target': reactant}})
    return elements


def element2(M, R, S):
    elements = []
    count = 0
    for ab in S:
        count += 1
        lelabel = "composant_strictement_connexe "+str(count)
        elements.append({'data': {'id': ab, 'labelid': lelabel}})
        for key in S[ab]['groupe']:
            elements.append(
                {'data': {'id': key+'a', 'labelid': key, 'parent': ab}})
    for key in R:
        reactants = R[key].get_reactifs()
        products = R[key].get_products()
        reversible = R[key].getReversible()
        for reactant in reactants:
            for product in products:
                elements.append(
                    {'data': {'source': reactant+'a', 'target': product+'a'}})
                if (reversible):
                    elements.append(
                        {'data': {'source': product+'a', 'target': reactant+'a'}})
    return elements


def visualise(Metabo, react, graph):
    default_stylesheet = [
        {
            'selector': 'node',
            'style': {
                'label': 'data(labelid)'
            }
        },
        {
            'selector': 'edge',
            'style': {
                'target-arrow-color': 'black',
                'target-arrow-shape': 'triangle',
                'line-color': 'grey',
                'curve-style': 'bezier'}}]

    styles = {
        'container': {
            'position': 'fixed',
            'display': 'flex',
            'flexDirection': 'column',
            'height': '100%',
            'width': '100%'
        },
        'cy-container': {
            'flex': '10',
            'position': 'relative'
        },
        'cytoscape': {
            'position': 'absolute',
            'width': '100%',
            'height': '100%',
            'zIndex': 999
        }}

    CC = tag.scc_species(graph)
    app = Dash()
    elements1 = defelements(Metabo, react)
    elements2 = element2(Metabo, react, CC)

    app.layout = html.Div(style=styles['container'], children=[
        html.Div([
            html.Button("afficher CSC", id='toggle-button'),
            html.Div(id='toggle-text')
        ]),
        html.Div(className='cy-container', style=styles['cy-container'], children=[
            cyto.Cytoscape(
                id='cytoscape-responsive-layout',
                elements=elements1,
                stylesheet=default_stylesheet,
                style=styles['cytoscape'],
                layout={
                    'name': 'cose',
                    'idealEdgeLength': 100,
                    'nodeOverlap': 20,
                    'refresh': 20,
                    'fit': True,
                    'padding': 30,
                    'randomize': False,
                    'componentSpacing': 100,
                    'nodeRepulsion': 400000,
                    'edgeElasticity': 100,
                    'nestingFactor': 5,
                    'gravity': 80,
                    'numIter': 1000,
                    'initialTemp': 200,
                    'coolingFactor': 0.95,
                    'minTemp': 1.0
                },
            )
        ])
    ])

    @app.callback(Output('toggle-text', 'children'), Input('toggle-button', 'n_clicks'))
    def update_toggle_text(n_clicks):
        n_clicks = 2 if n_clicks is None else n_clicks
        return '\t' + 'CSC ' + ('Off' if n_clicks % 2 == 0 else 'On')

    @app.callback(Output('cytoscape-responsive-layout', 'elements'), Input('toggle-button', 'n_clicks'))
    def update_csc(n_clicks):
        n_clicks = 2 if n_clicks is None else n_clicks
        return (elements1 if n_clicks % 2 == 0 else elements2)

    app.run_server(dev_tools_hot_reload=False)
    input("exit")
    return
