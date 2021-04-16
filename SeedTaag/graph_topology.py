import networkx as nx
import SeedTaag.Taagseed as tg

def shortest_path(Graph) :
  return nx.shortest_path(Graph)

def degree_centrality(Graph) :
  return nx.degree_centrality(Graph)

def all_pairs_nodes_connectivity(Graph) :
  return nx.all_pairs_node_connectivity(Graph)

def degree(Graph) :
  return nx.degree(Graph)

def diameter(Graph) :
    SP = shortest_path(Graph)
    dia= 0
    sp= ""
    for key in SP.keys() :
        for key2 in SP[key].keys() :
            if dia < len(SP[key][key2]) :
                dia = len(SP[key][key2])-1
    return dia 

def tarjan(Graph):
  return nx.strongly_connected_components(Graph)

def all_tp(Graph):
  return list(nx.algorithms.dag.all_topological_sorts(Graph))

def taagseed(Reaction, Graph) :
  species= tg.scc_species(Graph)
  dag = tg.dag_init(Reaction, Graph)
  seed= tg.find_seed(dag, species)
  return seed
