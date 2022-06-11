import ast

from python.network_extraction_from_issue_comment import get_issues, get_ower_repo_list

#Author: Zhijie Wan

if __name__ == "__main__":
    # comment_url = get_issues("fabiolb", "fabio")
    owers = get_ower_repo_list("owers")
    repos = get_ower_repo_list("repos")
    # print(owers)
    # print(repos)
    print(owers[0])
    print(repos[0])
    for i in range(0, 200):
        comment_url = get_issues(owers[i], repos[i])
        print(len(comment_url))