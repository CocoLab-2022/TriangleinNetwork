import ast
import os

import networkx as nx



from python.network_extraction_from_issue_comment import get_ower_repo_list, newoutputfile

#Author: Zhijie Wan

def get_nodes(participants):
    nodes = []
    for i in range(0, len(participants)):
        for j in range(0, len(participants[i]['commentor'])):
            nodes.append(participants[i]['commentor'][j])
            # print(participants[i]['commentor'][j])
        nodes = list(set(nodes))
        nodes = sorted(nodes)
    # print(nodes)
    print(len(nodes))
    return nodes

def build_graph_by_networkx(filename):
    network_weightedge = []
    path_1 = "../data/networkdata/" + filename + "_network_weightedge"
    with open(path_1, 'r+', encoding='utf-8') as f:
        for line in f:
            network_weightedge_list = ast.literal_eval(line)
            network_weightedge.append(network_weightedge_list)
    # print(network_weightedge)

    participants_info = []
    path_2 = "../data/participantsdata/" + filename + "_participants"
    with open(path_2, 'r+', encoding='utf-8') as f:
        for line in f:
            participants_info_list = ast.literal_eval(line)
            participants_info.append(participants_info_list)
    # print(participants)
    # build graph
    G = nx.Graph()
    # add nodes
    G.add_nodes_from(get_nodes(participants_info))
    # add weight
    e = network_weightedge
    # e = [(1, 2, 6), (2, 3, 2), (1, 3, 1), (3, 4, 7), (4, 5, 9), (5, 6, 3), (4, 6, 3)]
    for k in e:
        G.add_edge(k[0][0], k[0][1], weight=k[1])
    return G


if __name__ == "__main__":
    owers = get_ower_repo_list("owers")
    repos = get_ower_repo_list("repos")
    # print(owers)
    # print(repos)
    outputfilename = "trangle_count"
    outpufile = newoutputfile(outputfilename, "tranglecount")
    # print(nx.triangles(build_graph_by_networkx("homebrew-cask")))
    for i in range(0, 200):
        # print(nx.triangles(build_graph_by_networkx(repos[i])))
        # print({repos[i]: sum(nx.triangles(build_graph_by_networkx(repos[i])).values()) // 3})
        count = {repos[i]: sum(nx.triangles(build_graph_by_networkx(repos[i])).values()) // 3}
        print(count)
        with open(outpufile, 'a+', encoding='utf-8') as f:
            f.write("%s\n" % count)

