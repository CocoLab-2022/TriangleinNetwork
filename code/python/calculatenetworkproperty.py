import ast
import csv

import networkx as nx

from python.network_extraction_from_issue_comment import get_ower_repo_list, newoutputfile


repos = get_ower_repo_list("repos")

def write_data_to_csv(property, list):
    # pentagon_count = get_data("count/pentagon_count")
    # quadrangle_count = get_data("count/quadrangle_count")
    # trangle_count = get_data("count/trangle_count")
    # star_3_count = get_data("count/stars_3_count")
    # star_4_count = get_data("count/stars_4_count")
    # star_5_count = get_data("count/stars_5_count")
    repos = get_ower_repo_list("repos")

    outputfilename = "all_data.csv"
    outputfile = newoutputfile(outputfilename, "_csvdata")

    header = ['Project', property]
    data = []
    for i in range(197):
        each_data = [repos[i], list[i]]
        data.append(each_data)

    with open(outputfile, 'w', encoding='utf-8', newline='') as f:
        # write
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        for row in data:
            writer.writerow(row)

def rewrite_data_to_csv(property, lists):
    # outputfilename = "all_data.csv"
    # outputfile = newoutputfile(outputfilename, "_csvdata")
    path = '../data/_csvdata/all_data.csv'
    with open(path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        data = list(csv_reader)

    header = data[0]
    header.append(property)
    i = 0
    for row in data[1:]:
        row.append(lists[i])
        i += 1

    with open(path,'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(header)
        for row in data[1:]:
            csv_writer.writerow(row)

def getDSNDensity():
    Density = []
    for i in range(0,197):
        edges = getNodesEdgesCount(repos[i])
        edgesCount = edges[2]
        nodesCount = edges[1]
        repo = edges[0]
        density = 2 * edgesCount / (nodesCount*(nodesCount - 1))
        Density.append(density)
        # print(repo, densty)
    rewrite_data_to_csv("DSN density", Density)
    # Densty = sorted(Densty)
    print(Density)

def getDSNSize():
    size = []
    for i in range(0,197):
        nodes = getNodesEdgesCount(repos[i])
        nodesCount = nodes[2]
        repo = nodes[0]
        print(repo, nodesCount)
        size.append(nodesCount)
        # print(repo, nodesCount)
    write_data_to_csv("DSN size", size)
    # size = sorted(size)
    print(size)

# def drawgraph():
#     path = "../data/_networkdata/" + "Tone.js" + "_network_weightedge"
#     with open(path, 'r+', encoding='utf-8') as f:
#         for line in f:

def getDSNBridges():
    num_bridges = []
    for i in range(0, 197):
        G = nx.Graph()
        edges = []
        path = "../data/_networkdata/" + repos[i] + "_network_weightedge"
        with open(path, 'r+', encoding='utf-8') as f:
            for line in f:
                lists = ast.literal_eval(line)
                edges.append(lists[0])
                # print(list[0])
        G.add_edges_from(edges)

        # 找到网络中的桥
        bridges = list(nx.bridges(G))
        num_bridges.append(len(bridges))
        print(repos[i], "网络中的桥数：", len(bridges))
    # num_bridges = sorted(num_bridges)
    rewrite_data_to_csv("DSN bridges", num_bridges)
    print(num_bridges)

def get_kstars(k):
    k_stars_count = []
    for i in range(0, 197):
        k_stars = []
        G = nx.Graph()
        edges = []
        path = "../data/_networkdata/" + repos[i] + "_network_weightedge"
        with open(path, 'r+', encoding='utf-8') as f:
            for line in f:
                lists = ast.literal_eval(line)
                edges.append(lists[0])
                # print(list[0])
        G.add_edges_from(edges)

        for node in G.nodes():
            neighbors = list(G.neighbors(node))
            if len(neighbors) == k:
                k_stars.append(node)
        print(k_stars)
        k_stars_count.append(len(k_stars))

    rewrite_data_to_csv("DSN k-stars (k=3)", k_stars_count)



def getStability():
    Stability = []
    composeStability = []
    # count = 0
    for i in range(0,197):
        path = "../data/_networkdata/" + repos[i] + "_network_weightedge"
        with open(path, 'r+', encoding='utf-8') as f:
            edges = []
            nodes = []
            for line in f:
                edge_list = ast.literal_eval(line)
                edge = edge_list[0]
                edges.append(edge)
                nodes.append(edge_list[0][0])
                nodes.append(edge_list[0][1])

        nodes = set(nodes)
        nodes_count = len(nodes)

        graph = nx.Graph()
        graph.add_edges_from(edges)

        triangles = nx.triangles(graph)

        triangle_edges = 0
        # print(triangle_edges)
        for node in graph.nodes:
            for neighbor in graph.neighbors(node):
                if neighbor > node:
                    if (node, neighbor) in graph.edges() and triangles[node] > 0 and triangles[neighbor] > 0:
                        triangle_edges += 1

        stability = 2 * triangle_edges / ((nodes_count - 1) * nodes_count)
        # if stability >= 0.01:
        #    count +=1
        composestability = stability * stability

        Stability.append(stability)
        composeStability.append(composestability)

        print(repos[i], triangle_edges, stability, composestability)
    # print(count)
    # Stability = sorted(Stability)
    print(Stability)
    rewrite_data_to_csv("DSN stability", Stability)
    rewrite_data_to_csv("compose stability", composeStability)
        # triangles_edges.append(triangle_edges)

    # print(triangles_edges)


def getNodesEdgesCount(filename):
    nodes = []
    edges_count = 0
    NEC = []
    path = "../data/_networkdata/" + filename + "_network_weightedge"
    with open(path, 'r+', encoding='utf-8') as f:
        for line in f:
            edge_list = ast.literal_eval(line)
            edges_count += 1
            nodes.append(edge_list[0][0])
            nodes.append(edge_list[0][1])

    nodes = set(nodes)
    nodes_count = len(nodes)
    NEC.append(filename)
    NEC.append(edges_count)
    NEC.append(nodes_count)
    # print(nodes, nodes_count)
    return NEC


# getNodesEdgesCount("hosts")
# getDSNSize()
# getDSNDensity()
# getStability()
# getDSNBridges()
get_kstars(3)