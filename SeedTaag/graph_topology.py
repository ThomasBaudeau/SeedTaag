import networkx as nx

def shortest_path(Graph) :
  return nx.shortest_path(Graph)

def degree_centrality(Graph) :
  return nx.degree_centrality(Graph)

def all_pairs_nodes_connectivity(Graph) :
  return nx.all_pairs_node_connectivity(Graph)

def degree(Graph) :
  return nx.degree(Graph)


def tarjan(Graph):
  return nx.strongly_connected_components(Graph)

def all_tp(Graph):
  return list(nx.algorithms.dag.all_topological_sorts(G1))
