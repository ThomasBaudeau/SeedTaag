import SeedTaag.graph_topology as gt
import SeedTaag.data_storage as ds

def find_seed(dag,specie):
    """dind the seed of a dag

    Args:
        dag (networkx object): networkx graph must be a directed acyclic graph
        specie (dict): dictionary of node contained in the graph

    Returns:
        dict: dictionary of seeds
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
    """create dictionary of node with strictly connected component informations

    Args:
        graph (networkx object): networkx graph must be directed

    Returns:
        [dict]: dictionary of node with strictly connected component informations
    """
    scc=[list(c)
        for c in sorted
            (gt.tarjan(graph))]
    node_dag={}
    for i in range(len(scc)):
        node_dag[i+1] = {'groupe': scc[i], 'lenght': len(scc[i])}
    return node_dag


def find_dag_edge(Metabo, Reactions, scc_node):
    """built dictionary of the relation connecting two nodes

    Args:
        Metabo (dict): dictionary of Metabo object
        Reactions (dict): dictionary of Reaction object
        scc_node (dict): dictionary of node

    Returns:
        dict: dictionary of reaction built with the relations between two nodes
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
    """create sbml graph and dict of their related nodes 

    Args:
        Metabo (dict): dictionary of Metabo object
        Reactions (dict): dictionary of Reaction object
        Graph (networkx object): networkx graph must be directed

    Returns:
        [networkx object,dict]:  graph built with networkx and a dictionary of node with strictly connected component informations
    """
    scc_node = find_dag_node(Graph)
    scc_edge = find_dag_edge(Metabo,Reactions, scc_node)
    dag = ds.init_graph(scc_node, scc_edge,True)
    return dag,scc_node


