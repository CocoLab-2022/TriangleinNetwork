import ast

from python.network_extraction_from_issue_comment import get_ower_repo_list, extract_participants, build_network

repos = get_ower_repo_list("repos")

def extractbNetwork():
    for i in range(0,200):
        comments_info = []
        path = "../data/_commentdata_36monthes/" + repos[i] + "_comments_36monthes"
        with open(path, 'r+', encoding='utf-8') as f:
            for line in f:
                comments_info_list = ast.literal_eval(line)
                comments_info.append(comments_info_list)
        # print(comments_info)
        participants = extract_participants(comments_info)
        print(build_network(participants, repos[i]))

if __name__ == "__main__":
    extractbNetwork()