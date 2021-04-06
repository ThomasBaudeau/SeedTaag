import SeedTaag.graph_topology as topology 

### DISPLAY ###

def display_all(Graph) :
    display_shortest_path(Graph)
    print("\n")
    display_centrality(Graph)
    print("\n")
    display_connectivity(Graph)
    print("\n")
    display_degree(Graph)

def display_shortest_path(Graph) :
    SP= topology.shortest_path(Graph)
    for key in SP.keys() :
        for key2 in SP[key].keys() :
            print("The shortest path for ", key, " to ", key2, " is : ")
            print(SP[key][key2])

def display_centrality(Graph) :
    C= topology.degree_centrality(Graph)
    for key in C.keys() :
        print("The centrality degree for the metabolite ", key ," is :", C[key] )

def display_connectivity(Graph) :
    C= topology.all_pairs_node_connectivity(Graph)
    for key in C.keys() :
        for key2 in C[key].keys() :
            print("The connectivity of this pair of node ", key, "-", key2, " is : ", C[key][key2])

def display_degree(Graph) :
    D= topology.degree(Graph)
    for attribut in D :
        print("The degree of the metabolite ", attribut[0], " is :", attribut[1])

### SAVE ###

def save_all(Graph) :
    return

def save_shortest_path(Graph) :
    return

def save_centrality(Graph) :
    return

def save_connectivity(Graph) :
    return

def save_degree(Graph) :
    return
