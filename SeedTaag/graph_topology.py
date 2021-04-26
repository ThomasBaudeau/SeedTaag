import SeedTaag.Taagseed as tg
import networkx as nx
import igraph as ig
from igraph import Graph

def shortest_path(Graph) :
  """ Measure all shortest paths of the graph

  Args:
      Graph (<class 'networkx.classes.reportviews.DiDegreeView'>): Graph

  Returns:
      dict = {'A' : {'A' : ['A'], ...} , 'B' : {'A' : ['B', 'A'], ...} , ..}
  """
  #G = Graph.from_networkx(G)
  #return Graph.shortest_paths(G) #avec graphe de Igraph
  return nx.shortest_path(Graph)

def degree_centrality(Graph) :
  """ Measure the degree centrality of each nodes

  Args:
      Graph (<class 'networkx.classes.reportviews.DiDegreeView'>): Graph

  Returns:
      dict = { 'A' : degree_centrality, 'B' : degree_centrality, ...}
  """
  return nx.degree_centrality(Graph)

def betweenness_centrality(Graph) :
  """ Measure the betweenness centrality of each nodes

  Args:
      Graph (<class 'networkx.classes.reportviews.DiDegreeView'>): Graph

  Returns:
      dict = { 'A' : betweenness_centrality, 'B' : betweenness_centrality, ...}
  """
  return nx.betweenness_centrality(Graph)

def all_pairs_nodes_connectivity(Graph) :
  """ Measure the connectivity of each pairs of nodes

  Args:
      Graph (<class 'networkx.classes.reportviews.DiDegreeView'>): Graph

  Returns:
      dict = {'A' : {'B' : connectivity} , 'A' : {'C' : connectivity}, ... }
  """
  return nx.all_pairs_node_connectivity(Graph)

def degree(Graph) :
  """ Save the degree of each nodes

  Args:
      Graph (<class 'networkx.classes.reportviews.DiDegreeView'>): Graph

  Returns:
      <class 'networkx.classes.reportviews.DiDegreeView'>
  """
  return nx.degree(Graph)

def diameter(G) : # avec graphe Igraph
  """ Measure the graph diameter

  Args:
      Graph (<class 'networkx.classes.reportviews.DiDegreeView'>): Graph

  Returns:
      int
  """
  G = Graph.from_networkx(G)
  return Graph.diameter(G)

def eccentricity(G) : # avec graphe Igraph
  """ Measure the eccentricity of each nodes

  Args:
      Graph (<class 'networkx.classes.reportviews.DiDegreeView'>): Graph

  Returns:
      list: [eccentricity_1, eccentricity_2, ...]
  """
  G = Graph.from_networkx(G)
  return Graph.eccentricity(G)

def tarjan(Graph):
  return nx.strongly_connected_components(Graph)

def descendants(Graph,node):
    return nx.algorithms.dag.descendants(Graph, node)

def taagseed(Reaction, Graph) :
  dag, scc_node = tg.dag_init(Reaction, Graph)
  seed = tg.find_seed(dag, scc_node)
  return seed
