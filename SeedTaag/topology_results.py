import SeedTaag.graph_topology as topology
import SeedTaag.Taagseed as Taagseed
import json
import pandas as pd


### DISPLAY ###

def display_all(Graph, Reactions, Metabo):
    """Display all topology results of the graph on the terminal

    :param networkx.classes.reportviews.DiDegreeView Graph : Networkx graph
    :param dict Reactions : Dictionary of Reaction object 
    :param dict Metabo : Dictionary of Metabo object 
    """
    display_shortest_path(Graph)
    print("\n")
    display_degree_centrality(Graph)
    print("\n")
    display_betweenness_centrality(Graph)
    print("\n")
    display_connectivity(Graph)
    print("\n")
    display_degree(Graph)
    print("\n")
    display_diameter(Graph)
    print("\n")
    display_eccentricity(Graph)
    print("\n")
    display_seed(Graph, Reactions, Metabo)


def display_shortest_path(Graph):
    """Display all shortest paths of the graph on the terminal

    :param networkx.classes.reportviews.DiDegreeView Graph : Networkx graph 
    """
    SP = topology.shortest_path(Graph)
    for key in SP.keys():
        for key2 in SP[key].keys():
            print("The shortest path for ", key, " to ",
                  key2, " is :\t", SP[key][key2])


def display_degree_centrality(Graph):
    """Display the degree centrality of each nodes on the terminal

    :param networkx.classes.reportviews.DiDegreeView Graph: Networkx graph 
    """
    C = topology.degree_centrality(Graph)
    for key in C.keys():
        print("The centrality degree for the metabolite ",
              key, " is :\t", C[key])


def display_betweenness_centrality(Graph):
    """Display the betweenness centrality of each nodes on the terminal

    :param networkx.classes.reportviews.DiDegreeView Graph: Networkx graph 
    """
    Bc = topology.betweenness_centrality(Graph)
    for key in Bc.keys():
        print("The betweenness centrality for the metabolite ",
              key, " is :\t", Bc[key])


def display_connectivity(Graph):
    """Display the connectivity of each pairs of nodes on the terminal

    :param networkx.classes.reportviews.DiDegreeView Graph: Networkx graph 
    """
    C = topology.all_pairs_nodes_connectivity(Graph)
    for key in C.keys():
        for key2 in C[key].keys():
            print("The connectivity of this pair of node ",
                  key, "-", key2, " is :\t", C[key][key2])


def display_degree(Graph):
    """Display the degree of each nodes on the terminal

    :param networkx.classes.reportviews.DiDegreeView Graph: Networkx graph 
    """
    D = topology.degree(Graph)
    for attribut in D:
        print("The degree of the metabolite ",
              attribut[0], " is :\t", attribut[1])


def display_diameter(Graph):
    """Display the graph diameter on the terminal

    :param networkx.classes.reportviews.DiDegreeView Graph: Networkx graph 
    """
    Dia = topology.diameter(Graph)
    print("Diameter :\t", Dia)


def display_eccentricity(Graph):
    """Display the eccentricity of each nodes on the terminal

    :param networkx.classes.reportviews.DiDegreeView Graph: Networkx graph 
    """
    Ec = topology.eccentricity(Graph)
    for i in range(len(Ec)):
        print("Eccentricity for the metabolite ", i, ":\t", Ec[i])


def display_seed(Graph, Reactions, Metabo):
    """Display all seeds of the metabolic network on the terminal

    :param networkx.classes.reportviews.DiDegreeView Graph: Networkx graph 
    :param dict Reactions : Dictionary of Reaction object
    :param dict Metabo : Dictionary of Metabo object 
    """
    S = topology.taagseed(Metabo, Reactions, Graph)
    for key in S.keys():
        print("Seed : ", S[key]['seed'], "- Probability :", S[key]['proba'])

### SAVE ###


def save_all(Graph, Reactions, Metabo):
    """Save all topology results of the graph in a JSON file

    :param networkx.classes.reportviews.DiDegreeView Graph: Networkx graph 
    :param dict Reactions : Dictionary of Reaction object
    :param dict Metabo : Dictionary of Metabo object  
    """
    De = {}
    SP = topology.shortest_path(Graph)
    Co = topology.all_pairs_nodes_connectivity(Graph)
    Ce = topology.degree_centrality(Graph)
    D = topology.degree(Graph)
    S = topology.taagseed(Metabo, Reactions, Graph)
    Dia = topology.diameter(Graph)
    Ecc = topology.eccentricity(Graph)
    Bc = topology.betweenness_centrality(Graph)
    for attribut in D:
        De[attribut[0]] = attribut[1]
    data = {"Shortest_path": SP, "Degree Centrality": Ce, "Betweenness centrality": Bc,
            "Connectivity": Co, "Degree": De, "Diameter": Dia, "Eccentricity": Ecc, "Seed": S}

    with open("topology_results.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Backup done")


def save_shortest_path(Graph):
    """Save all shortest paths of the graph in a JSON file

    :param networkx.classes.reportviews.DiDegreeView Graph: Networkx graph
    """
    SP = topology.shortest_path(Graph)
    with open("shortest_paths.json", "w") as file:
        json.dump(SP, file, indent=4)
    print("Backup done")


def save_degree_centrality(Graph):
    """Save the degree centrality of each nodes in a tsv file

    :param networkx.classes.reportviews.DiDegreeView Graph: Networkx graph
    """
    C = topology.degree_centrality(Graph)

    # TSV :
    col = {"Metabolite": [], "Centrality": []}
    for key in C.keys():
        col["Metabolite"].append(key)
        col["Centrality"].append(C[key])
    df = pd.DataFrame(col)
    df.to_csv("degree_centrality.tsv", sep="\t", index=False)

    # JSON :
    # with open("centrality.json", "w") as file :
    #     json.dump(C, file, indent= 4)
    print("Backup done")


def save_connectivity(Graph):
    """Save the connectivity of each pairs of nodes in a tsv file

    :param networkx.classes.reportviews.DiDegreeView Graph: Networkx graph
    """
    C = topology.all_pairs_node_connectivity(Graph)

    # TSV :
    col = {"un": [], "deux": [], "connectivity": []}
    for key in C.keys():
        for key2 in C[key].keys():
            col["un"].append(key)
            col["deux"].append(key2)
            col["connectivity"].append(C[key][key2])
    df = pd.DataFrame(col)
    df.to_csv("all_pairs_node_connectivity.tsv", sep="\t", index=False)

    # JSON :
    # with open("connectivity.json", "w") as file :
    #     json.dump(C, file, indent= 4)
    print("Backup done")


def save_degree(Graph):
    """Save the degree of each nodes in a tsv file

    :param networkx.classes.reportviews.DiDegreeView Graph: Networkx graph 
    """
    De = {}
    D = topology.degree(Graph)
    for attribut in D:
        De[attribut[0]] = attribut[1]

    # TSV :
    col = {"Metabolite": [], "Degree": []}
    for key in De.keys():
        col["Metabolite"].append(key)
        col["Degree"].append(De[key])
    df = pd.DataFrame(col)
    df.to_csv("degree.tsv", sep="\t", index=False)

    # JSON :
    # with open("degree.json", "w") as file :
    #     json.dump(De, file, indent= 4)
    print("Backup done")


def save_diameter(Graph):
    """Save the graph diameter in a JSON file

    :param networkx.classes.reportviews.DiDegreeView Graph: Networkx graph 
    """
    Dia = topology.diameter(Graph)
    with open("diameter.json", "w") as file:
        json.dump(Dia, file, indent=4)
    print("Backup done")


def save_eccentricity(Graph):
    """Save the eccentricity of each nodes in a JSON file

    :param networkx.classes.reportviews.DiDegreeView Graph: Networkx graph 
    """
    Ecc = topology.eccentricity(Graph)
    with open("eccentricity.json", "w") as file:
        json.dump(Ecc, file, indent=4)
    print("Backup done")


def save_betweenness_centrality(Graph):
    """Save the betweenness centrality of each nodes in a tsv file

    :param networkx.classes.reportviews.DiDegreeView Graph: Networkx graph
    """
    Bc = topology.betweenness_centrality(Graph)
    col = {"Metabolite": [], "Centrality": []}
    for key in Bc.keys():
        col["Metabolite"].append(key)
        col["Centrality"].append(Bc[key])
    # with open("centrality.json", "w") as file :
    #     json.dump(C, file, indent= 4)
    df = pd.DataFrame(col)
    df.to_csv("betweenness_centrality.tsv", sep="\t", index=False)
    print("Backup done")


def save_seed(Graph, Reaction, Metabo):
    """Save all seeds of the metabolic network in a JSON file

    :param networkx.classes.reportviews.DiDegreeView Graph: Networkx graph 
    :param dict Reactions : Dictionary of Reaction object
    :param dict Metabo : Dictionary of Metabo object 
    """
    S = topology.taagseed(Metabo, Reaction, Graph)
    with open("seeds.json", "w") as file:
        json.dump(S, file, indent=4)
    print("Backup done")
