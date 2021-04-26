from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
import dash_cytoscape as cyto
from dash.dependencies import Input, Output, State
import plotly.express as px
import requests
import SeedTaag.Class as C
import SeedTaag.Taagseed as tag



def defelements(Metabos, Reactions):
    elements = []
    for key in Metabos:
        properties = Metabos[key].properties()
        elements.append({'data': {'id': key, 'labelid': properties['id'],
        'name':properties['name'],
        'compartiment':properties['compartment'],'boundaryConditions':properties['boundaryConditions'],
        'hasOnlySubtanceUnit':properties['hasOnlySubtanceUnit'],'constant':['constant']}})
    for key in Reactions:
        properties = Reactions[key].properties()
        for reactant in properties['reactifs']:
            for product in properties['products']:
                elements.append({'data': {'source': product.get_id(),
                                          'target': reactant.get_id(), 'labelid': key, 'name': properties['name'],
                                          'enzymes': properties['enzymes']}})
                if (properties['reversible']):
                    elements.append({'data': {'source': product.get_id(),
                    'target': reactant.get_id(),'labelid':key,'name':properties['name'],
                    'enzymes':properties['enzymes']}})
    return elements


def defcsc(Metabos, Reactions, S):
    elements = []
    count = 0
    for scc in S:
        count += 1
        lelabel = "strongly connected components "+str(count)
        elements.append({'data': {'id': scc, 'labelid': lelabel}})
        for key in S[scc]['groupe']:
            properties = Metabos[key].properties()
            elements.append({'data': {'id': key+'_', 'labelid': properties['id'],
            'name': properties['name'],
            'compartiment': properties['compartment'], 'boundaryConditions': properties['boundaryConditions'],
            'hasOnlySubtanceUnit': properties['hasOnlySubtanceUnit'], 'constant': ['constant']}})
    for key in Reactions:
            properties = Reactions[key].properties()
            for reactant in properties['reactifs']:
                for product in properties['products']:
                    elements.append({'data': {'source': product.get_id()+'_',
                    'target': reactant.get_id()+'_', 'labelid': key, 'name': properties['name'],
                    'enzymes': properties['enzymes']}})
                    if (properties['reversible']):
                        elements.append({'data': {'source': product.get_id()+'_',
                        'target': reactant.get_id()+'_', 'labelid': key, 'name': properties['name'],
                        'enzymes': properties['enzymes']}})
    return elements

def defdag(node, edge):
    elements = []
    count = 0
    for key in node:
        count += 1
        lelabel = "strongly connected components "+str(count)
        elements.append({'data': {'id': key, 'labelid': lelabel,
        'group':node[key]['groupe'],'lenght':node[key]['lenght']}})
    for key in edge:
        elements.append(
            {'data': {'source': edge[key]['r'], 'target': edge[key]['p'], 'labelid': key}})
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

    dag_node = tag.scc_species(graph)
    dag_edge = tag.find_dag_edge(Metabo, react, dag_node)
    app = Dash()
    elements1 = defelements(Metabo, react)
    elements2 = defcsc(Metabo, react, dag_node)
    elements3 = defdag(dag_node,dag_edge)

    app.layout = html.Div(style=styles['container'], children=[
        dcc.Dropdown(
            id='dropdown-update-elements',
            value='grid',
            clearable=False,
            options=[
                {'label': name.capitalize(), 'value': name}
                for name in ['simple_graph', 'scc_graph', 'dag']
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

    @app.callback(Output('cytoscape-update-layout', 'layout'),
                  Input('dropdown-update-elements', 'value'))
    def update_layout(value):
        if value == 'simple_graph':
            return elements1
        if value == 'scc_graph':
            return elements2
        if value == 'dag':
            return elements3

    app.run_server()

   
