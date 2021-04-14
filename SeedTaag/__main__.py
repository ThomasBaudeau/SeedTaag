import graph_formation as formation
import topology_results as topology
import data_extraction as extract
import data_storage as storage


import libsbml
import networkx as nx

### GRAPH ###

S, R= storage.init_data('1Seed4Loop3SeedLoop.sbml')
G = storage.init_graph(S, R)



### TOPOLOGY ###

topology.display_all(G, R)

### SAVE ###

topology.save_all(G, R)

