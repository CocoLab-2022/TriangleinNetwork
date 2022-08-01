import ast

from python.network_extraction_from_issue_comment import get_ower_repo_list

# the issue data will update, so we need get issue's last number as a mark last time
def get_issue_lastnumber():
    owers = get_ower_repo_list("owers")
    repos = get_ower_repo_list("repos")
    # print(owers)
    # print(repos)
    print(owers[0])
    print(repos[0])
    lastnumber = []
    for i in range(0, 200):
        with open("../data/issuedata/" + repos[i] + "_issue_cleaned", 'r+', encoding='utf-8') as f:
            firstline = f.readline()
            firstline= ast.literal_eval(firstline)
            lastnumber.append(firstline[0])
    print(lastnumber)
    return lastnumber

get_issue_lastnumber()