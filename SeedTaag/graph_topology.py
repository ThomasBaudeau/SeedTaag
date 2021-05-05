import SeedTaag.Taagseed as tg
import networkx as nx
import igraph as ig
from igraph import Graph

def shortest_path(Graph) :
  """ Measure all shortest paths of the graph

    :param networkx.classes.reportviews.DiDegreeView Graph : Networkx graph

    :returns: dict = {'A' : {'A' : ['A'], ...} , 'B' : {'A' : ['B', 'A'], ...} , ..}
    :rtype: dict
  """
  #G = Graph.from_networkx(G)
  #return Graph.shortest_paths(G) #avec graphe de Igraph
  return nx.shortest_path(Graph)

def degree_centrality(Graph) :
  """ Measure the degree centrality of each nodes

    :param networkx.classes.reportviews.DiDegreeView Graph : Networkx graph

    :returns: dict = { 'A' : degree_centrality, 'B' : degree_centrality, ...}
    :rtype: dict
  """
  return nx.degree_centrality(Graph)

def betweenness_centrality(Graph) :
  """Measure the betweenness centrality of each nodes

    :param networkx.classes.reportviews.DiDegreeView Graph : Networkx graph

    :returns: dict = { 'A' : betweenness_centrality, 'B' : betweenness_centrality, ...}
    :rtype: dict
  """
  return nx.betweenness_centrality(Graph)

def all_pairs_nodes_connectivity(Graph) :
    """Measure the connectivity of each pairs of nodes

    :param networkx.classes.reportviews.DiDegreeView Graph : Networkx graph

    :returns: dict = {'A' : {'B' : connectivity} , 'A' : {'C' : connectivity}, ... }
    :rtype: dict
    """
    return nx.all_pairs_node_connectivity(Graph)

def degree(Graph) :
    """Save the degree of each nodes

    :param networkx.classes.reportviews.DiDegreeView Graph : Networkx graph

    :returns: degree of each nodes
    :rtype: networkx.classes.reportviews.DiDegreeView
    """
    return nx.degree(Graph)

def diameter(G) : # avec graphe Igraph
    """Measure the graph diameter

    :param networkx.classes.reportviews.DiDegreeView G : Networkx graph

    :returns: Diameter
    :rtype: int
    """
    G = Graph.from_networkx(G)
    return Graph.diameter(G)

def eccentricity(G) : # avec graphe Igraph
  """Measure the eccentricity of each nodes

    :param networkx.classes.reportviews.DiDegreeView G : Networkx graph

    :returns: [eccentricity_1, eccentricity_2, ...]
    :rtype: list
  """
  G = Graph.from_networkx(G)
  return Graph.eccentricity(G)

def tarjan(Graph):
  """Find the strongly connected component of the graph with the tarjan algorithm

    :param networkx.classes.reportviews.DiDegreeView Graph: Networkx graph

    :returns: Set of node who each one represent scc
    :rtype: node_set_networkx
  """
  return nx.strongly_connected_components(Graph)

def ancestors(Graph,node):
  """Find the ancestor of one node

    :param networkx.classes.reportviews.DiDegreeView Graph : Networkx graph
    :param dict node : Dictionary of nodes in the graph

    :returns: Ancestor of the node
    :rtype: node_set_networkx
  """
  return nx.algorithms.dag.ancestors(Graph, node)


def taagseed(Metabo,Reaction, Graph):
  """Find the seed in the graph

    :param dict Metabo : Dictionary of metabo objects
    :param dict Reaction : Dictionary of reaction objects
    :param networkx.classes.reportviews.DiDegreeView Graph : Networkx graph

    :returns: Dictionary of seeds 
    :rtype: dict 
  """
  dag, scc_node = tg.dag_init(Metabo,Reaction, Graph)
  seed = tg.find_seed(dag, scc_node)
  return seed
