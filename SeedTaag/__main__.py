import topology_results as topology
import data_storage as storage
import argparse 
### GRAPH ###
"""
S, R= storage.init_data('1Seed4Loop3SeedLoop.sbml')
G = storage.init_graph(S, R)



### TOPOLOGY ###

topology.display_all(G, R)

### SAVE ###

topology.save_all(G, R)

###### WORK IN PROGRESS #######
"""
MESSAGE ="""
metabolic network topologie and seed detector
"""


def main():
    parser = argparse.ArgumentParser('staag',
    description='for specific help on each subcommand use:'
    )
    parser.add_argument('-i',
    '--input',
    required=True,
    help='name of the sbml file to read',
    )
    exgroup = parser.add_mutually_exclusive_group(required=True)
    exgroup.add_argument('--all',
    action='store_true',
    help='displaying all the topologie result')

    exgroup.add_argument('--select',
    action='store',
    nargs='+',
    choices=['sp','c','cn','d','s','-f','-g'],
    help='display selected topology result:\n\
        sp=shortest path;\
        c=centrality;\
        cn=connectivity;\
        d=degree;\
        s=seed')

    exgroup.add_argument('--save_all',
    action='store_true',
    help='save all display result')
    exgroup.add_argument('--save',
    action='store',
    nargs='+',
    choices=['sp', 'c', 'cn', 'd', 's'],
    help='save selected topology result:\n\
        sp=shortest path;\
        c=centrality;\
        cn=connectivity;\
        d=degree;\
        s=seed')

    args=parser.parse_args()
    S, R = storage.init_data(args.input)
    G = storage.init_graph(S, R)
    if args.all:
        topology.display_all(G, R)
    if args.save_all:
        topology.save_all(G, R)
    if (args.select):
        rep = list(set(args.select))
        if len(rep)>6:
            raise ValueError('Error: Too many argument')
        else:
            if 'sp' in rep:
                topology.display_shortest_path(G)
                print("\n")
            if 'c' in rep:
                topology.display_centrality(G)
                print("\n")
            if 'cn' in rep:
                topology.display_connectivity(G)
                print("\n")
            if 'd' in rep:
                topology.display_degree(G)
                print("\n")
            if 's' in rep:
                topology.display_seed(G,R)
                print("\n")
            if '-f' in rep:
                pass
            if '-g' in rep:
                pass
            if '-h' in rep:
                pass
    if (args.save):
        rep = list(set(args.save))
        if len(rep) > 6:
            raise ValueError('Error: Too many argument')
        else:
            if 'sp' in rep:
                topology.save_shortest_path(G)
                print("\n")
            if 'c' in rep:
                topology.save_centrality(G)
                print("\n")
            if 'cn' in rep:
                topology.save_connectivity(G)
                print("\n")
            if 'd' in rep:
                topology.save_degree(G)
                print("\n")
            if 's' in rep:
                topology.save_seed(G, R)
                print("\n")
            if '-f' in rep:
                pass
            if '-g' in rep:
                pass
            if '-h' in rep:
                pass


if __name__ == "__main__":
    main()
