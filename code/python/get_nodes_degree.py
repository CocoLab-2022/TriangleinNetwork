import ast

from python.get_differentsides_count import build_graph_by_networkx
from python.network_extraction_from_issue_comment import get_ower_repo_list, newoutputfile

def get_nodes(filename):
    participants_info = []
    path_2 = "../data/participantsdata/" + filename + "_participants"
    with open(path_2, 'r+', encoding='utf-8') as f:
        for line in f:
            participants_info_list = ast.literal_eval(line)
            participants_info.append(participants_info_list)

    nodes = []
    for i in range(0, len(participants_info)):
        for j in range(0, len(participants_info[i]['commentor'])):
            nodes.append(participants_info[i]['commentor'][j])
            # print(participants[i]['commentor'][j])
        nodes = list(set(nodes))
        nodes = sorted(nodes)
    # print(nodes)
    # print(len(nodes))
    return nodes

def get_nodes_degree():
    repos = get_ower_repo_list("repos")
    # print(owers)
    # print(repos)
    for i in range(0, 200):
        outputfilename = repos[i] + "_nodes_degree"
        outpufile = newoutputfile(outputfilename, "nodesdegree")
        node = get_nodes(repos[i])
        lenth = len(node)
        print(repos[i])
        for j in range(lenth):
            count = [node[j], build_graph_by_networkx(repos[i]).degree(node[j])]
            print(count)
            with open(outpufile, 'a+', encoding='utf-8') as f:
                f.write("%s\n" % count)

# print(build_graph_by_networkx("homebrew-cask").degree("0xdevalias"))
get_nodes_degree()