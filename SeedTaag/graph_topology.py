import SeedTaag.Taagseed as tg
import networkx as nx
import igraph as ig
from igraph import Graph

def shortest_path(Graph) :
  #G = Graph.from_networkx(G)
  #return Graph.shortest_paths(G) #avec graphe de Igraph
  return nx.shortest_path(Graph)

def degree_centrality(Graph) :
  return nx.degree_centrality(Graph)

def betweenness_centrality(Graph) :
    return nx.betweenness_centrality(Graph)

def all_pairs_nodes_connectivity(Graph) :
  return nx.all_pairs_node_connectivity(Graph)

def degree(Graph) :
  return nx.degree(Graph)

def diameter(G) : # avec graphe Igraph
    G = Graph.from_networkx(G)
    return Graph.diameter(G)

def eccentricity(G) : # avec graphe Igraph
    G = Graph.from_networkx(G)
    return Graph.eccentricity(G)

def tarjan(Graph):
  return nx.strongly_connected_components(Graph)

def all_tp(Graph):
  return list(nx.algorithms.dag.all_topological_sorts(Graph))

def taagseed(Reaction, Graph) :
  species= tg.scc_species(Graph)
  dag = tg.dag_init(Reaction, Graph)
  seed= tg.find_seed(dag, species)
  return seed
