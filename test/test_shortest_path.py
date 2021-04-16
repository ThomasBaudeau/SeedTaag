
import SeedTaag.graph_topology as topology
import SeedTaag.data_storage as storage

EXPECTED_SHORTEST_PATH= {
  'A': 
  {'A': ['A'], 'B': ['A', 'B'], 'C': ['A', 'B', 'C'], 'D': ['A', 'B', 'C', 'D'], 'E': ['A', 'B', 'C', 'E']}, 
  'B': 
  {'B': ['B'], 'C': ['B', 'C'], 'D': ['B', 'C', 'D'], 'E': ['B', 'C', 'E']}, 
  'C': 
  {'C': ['C'], 'D': ['C', 'D'], 'E': ['C', 'E'], 'B': ['C', 'E', 'B']}, 
  'D': 
  {'D': ['D'], 'E': ['D', 'E'], 'B': ['D', 'E', 'B'], 'C': ['D', 'E', 'B', 'C']}, 
  'E': 
  {'E': ['E'], 'B': ['E', 'B'], 'C': ['E', 'B', 'C'], 'D': ['E', 'B', 'C', 'D']}, 
  'F': 
  {'F': ['F'], 'E': ['F', 'E'], 'H': ['F', 'H'], 'B': ['F', 'E', 'B'], 'G': ['F', 'H', 'G'], 'C': ['F', 'E', 'B', 'C'], 'D': ['F', 'E', 'B', 'C', 'D']}, 
  'G': 
  {'G': ['G'], 'F': ['G', 'F'], 'E': ['G', 'F', 'E'], 'H': ['G', 'F', 'H'], 'B': ['G', 'F', 'E', 'B'], 'C': ['G', 'F', 'E', 'B', 'C'], 'D': ['G', 'F', 'E', 'B', 'C', 'D']}, 
  'H': 
  {'H': ['H'], 'G': ['H', 'G'], 'F': ['H', 'G', 'F'], 'E': ['H', 'G', 'F', 'E'], 'B': ['H', 'G', 'F', 'E', 'B'], 'C': ['H', 'G', 'F', 'E', 'B', 'C'], 'D': ['H', 'G', 'F', 'E', 'B', 'C', 'D']}
}

def test_shortest_path():
  S, R = storage.init_data('toy_metabolic.sbml.xml')
  G = storage.init_graph(S, R)
  result= topology.shortest_path(G)
  assert result == EXPECTED_SHORTEST_PATH

if __name__=="__main__" :
  test_shortest_path()