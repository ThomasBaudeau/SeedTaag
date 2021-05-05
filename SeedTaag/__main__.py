import SeedTaag.topology_results as topology
import SeedTaag.data_storage as storage
import SeedTaag.visualise as v
import argparse

MESSAGE ="""
metabolic network topology and seed detector
"""


def main():
    """Main fonction for use SeedTaag package with -m SeedTaag

    :Raises ValueError:Too many argument : incorrect usage of the command
    """
    parser = argparse.ArgumentParser('staag',
                                     description='for specific help on each subcommand use:',
                                     formatter_class=argparse.RawTextHelpFormatter
                                     )
    parser.add_argument('-i',
                        '--input',
                        required=True,
                        help='name of the sbml file to read\n ',
                        )
    parser.add_argument('-d',
                        '--display',
                        required=False,
                        action='store_true',
                        help='display graph on page web at :http://127.0.0.1:8050/\n ')
    exgroup = parser.add_mutually_exclusive_group(required=True)
    exgroup.add_argument('--all',
                         action='store_true',
                         help='displaying all the topologie result\n ')

    exgroup.add_argument('--select',
                         action='store',
                         nargs='+',
                         choices=['sp', 'c', 'cn', 'd', 's', '-f', '-g'],
                         help='save selected topology result:\n     sp=shortest path;\n     dc=degree centrality;\n     cn=connectivity;\n     d=degree;\n     s=seed;\n     dm=diameter;\n     bc=betweeness centrality\n ')

    exgroup.add_argument('--save_all',
                         action='store_true',
                         help='save all display results\n ')
    exgroup.add_argument('--save',
                         action='store',
                         nargs='+',
                         choices=['sp', 'dc', 'cn', 'd', 's', 'dm', 'bc'],
                         help='save selected topology result:\n     sp=shortest path;\n     dc=degree centrality;\n     cn=connectivity;\n     d=degree;\n     s=seed;\n     dm=diameter;\n     bc=betweeness centrality\n ')
                         
    args=parser.parse_args()
    S, R = storage.init_data(args.input)
    G = storage.init_graph(S, R)
    if args.all:
        topology.display_all(G, R,S)
    if args.save_all:
        topology.save_all(G, R,S)
    if (args.select):
        rep = list(set(args.select))
        if len(rep)>6:
            raise ValueError('Error: Too many argument')
        else:
            if 'sp' in rep:
                topology.display_shortest_path(G)
                print("\n")
            if 'dc' in rep:
                topology.display_centrality(G)
                print("\n")
            if 'cn' in rep:
                topology.display_connectivity(G)
                print("\n")
            if 'd' in rep:
                topology.display_degree(G)
                print("\n")
            if 's' in rep:
                topology.display_seed(G,R,S)
                print("\n")
            if 'dm' in rep:
                topology.display_diameter(G)
                print("\n")
            if 'bc' in rep:
                topology.display_degree_centrality(G)
                print("\n")
         
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
                topology.save_seed(G, R,S)
                print("\n")
            if 'dm' in rep:
                topology.save_diameter(G)
                print("\n")
            if 'bc' in rep:
                topology.save_degree_centrality(G)
                print("\n")
    if (args.display):
        v.visualise(S,R,G)


if __name__ == "__main__":
    main()
