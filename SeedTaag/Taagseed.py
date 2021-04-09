import graph_topology as gt
import data_storage as ds


def find_seed(DAG,specie):
    """
    function for find seed element in a DAG 
    """
    seed={}
    seeds=[]
    count=0
    tp=gt.all_tp(DAG)
    for key in reversed(tp):
        if not key[0] in seeds:
            count+=1
            seed[count] = {'seed': specie[key[0]]['groupe'], 'proba': '1/'+str(len(specie[key[0]]['groupe']))}
            seeds.append(key[0])
    return seed

def scc_species(graph):
    """
    built dictionary of all the speciespecieC of graph
    """
    seed=[list(c)
        for c in sorted
            (gt.tarjan(G))]
    seeds={}
    for i in range(len(seed)):
        seeds[i+1]={'groupe':seed[i],'taille':len(seed[i])}
    return seeds

def scc_link(Reactions,specie):
    """
    built dictionary of links between all the specieCC
    """
    seed_reaction={}
    keys=list(specie.keys())
    count=0
    while len(keys)!=0:
        count+=1
        key=keys[0]
        keys.remove(key)
        for j in keys:
            for node in specie[key]['groupe']:
                for node2 in specie[j]['groupe']:
                    for reaction in Reactions:
                        rep=Reactions[reaction].isinreaction(node,node2)
                        if rep != None:
                            if rep:
                                seed_reaction[count] = {'r': key, 'p': j}
                                count+=1
                            elif not rep:
                                seed_reaction[count] = {'r': j, 'p': key}
                                count += 1
    return seed_reaction


def dag_init(Reactions,Graph):
    specie = scc_species(Graph)
    link = scc_link(Reactions,specie)
    dag = ds.init_graph(specie, link, mode=False)
    return dag


