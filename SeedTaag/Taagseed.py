import SeedTaag.graph_topology as gt
import SeedTaag.data_storage as ds

def find_seed(dag,specie):
    """
    function for find seed element in a DAG 
    """
    seed = {}
    count = 0
    print(specie)
    for node in dag.nodes:
        theset = gt.descendants(dag, node)
        if len(theset) == 0:
            count += 1
            seed[count] = {'seed': specie[node]['groupe'],
                           'proba': '1/'+str(specie[node]['lenght'])}
    return seed

def find_dag_node(graph):
    """
    built dictionary of all the speciespecieC of graph
    """
    scc=[list(c)
        for c in sorted
            (gt.tarjan(graph))]
    node_dag={}
    for i in range(len(scc)):
        node_dag[i+1] = {'groupe': scc[i], 'lenght': len(scc[i])}
    return node_dag


def find_dag_edge(Metabo, Reactions, scc_node):
    """
    built dictionary of links between all the specieCC
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
    scc_node = find_dag_node(Graph)
    scc_edge = find_dag_edge(Metabo,Reactions, scc_node)
    dag = ds.init_graph(scc_node, scc_edge,True)
    return dag,scc_node


