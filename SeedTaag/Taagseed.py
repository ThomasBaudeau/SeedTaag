import SeedTaag.graph_topology as gt
import SeedTaag.data_storage as ds

def find_seed(dag,specie):
    """Find the seed of a dag

    :param networkx_object dag : Networkx graph must be a directed acyclic graph
    :param specie dict: Dictionary of node contained in the graph

    :returns: Dictionary of seeds
    :rtype: dict
    """
    seed = {}
    count = 0
    for node in dag.nodes:
        theset = gt.ancestors(dag, node)
        if len(theset) == 0:
            count += 1
            seed[count] = {'seed': specie[node]['groupe'],
                           'proba': '1/'+str(specie[node]['lenght'])}
    return seed

def find_dag_node(graph):
    """Create dictionary of node with strongly connected components informations

    :param networkx_object graph: Networkx graph must be directed

    :returns: Dictionary of node with strongly connected components informations
    :rtype: dict
    """
    scc=[list(c)
        for c in sorted
            (gt.tarjan(graph))]
    node_dag={}
    for i in range(len(scc)):
        node_dag[i+1] = {'groupe': scc[i], 'lenght': len(scc[i])}
    return node_dag


def find_dag_edge(Metabo, Reactions, scc_node):
    """Built dictionary of the relation connecting two nodes

    :param dict Metabo : Dictionary of Metabo object
    :param dict Reactions : Dictionary of Reaction object
    :param dict scc_node : Dictionary of node

    :returns: Dictionary of reaction built with the relations between two nodes
    :rtype: dict
    """
    dag_edge={}
    keys = list(scc_node.keys())
    count=0
    while len(keys)!=0:
        count+=1
        key=keys[0]
        keys.remove(key)
        for j in keys:
            for node in scc_node[key]['groupe']:
                for node2 in scc_node[j]['groupe']:
                    for reaction in Reactions:
                        rep = Reactions[reaction].isinreaction(Metabo[node], Metabo[node2])
                        if rep != None:
                            if rep:
                                dag_edge[count] = {'r': key, 'p': j}
                                count+=1
                            elif not rep:
                                dag_edge[count] = {'r': j, 'p': key}
                                count += 1
    return dag_edge


def dag_init(Metabo,Reactions, Graph):
    """Create sbml graph and dict of their related nodes 

    :param dict Metabo : Dictionary of Metabo object
    :param dict Reactions : Dictionary of Reaction object
    :param networkx_object Graph : networkx graph must be directed

    :returns: Graph built with networkx and a dictionary of node with strictly connected component informations
    :rtype: networkx object, dict
    """
    scc_node = find_dag_node(Graph)
    scc_edge = find_dag_edge(Metabo,Reactions, scc_node)
    dag = ds.init_graph(scc_node, scc_edge,True)
    return dag,scc_node


