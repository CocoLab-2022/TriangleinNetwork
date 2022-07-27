import ast

from python.network_extraction_from_issue_comment import get_issue_comment_info, extract_participants, build_network

#Author: Zhijie Wan

# if __name__ == "__main__":
#     owers = get_ower_repo_list("owers")
#     repos = get_ower_repo_list("repos")
#     # print(owers)
#     # print(repos)
#     print(owers[0])
#     print(repos[0])
#     for i in range(0, 200):
#         comment_url = get_issues(owers[i], repos[i])
#         print(len(comment_url))
#         comment_info = get_issue_comment_info(comment_url, repos[i])
#         print(len(comment_info))
#         participants = extract_participants(comment_info)
#         print(build_network(participants, repos[i]))

if __name__ == "__main__":
    comment_url = []
    with open("../data/issuedata/fabio_issue_cleaned", 'r+', encoding='utf-8') as f:
        for line in f:
            comments_url_list = ast.literal_eval(line)
            comment_url.append(comments_url_list)
    # print(comment_url[1270])
    get_issue_comment_info(comment_url, "fabio")

    # build network
    comments_info = []
    with open("../data/issuedata/fabio_issue_comment", 'r+', encoding='utf-8') as f:
        for line in f:
            comments_info_list = ast.literal_eval(line)
            comments_info.append(comments_info_list)
    # print(comments_info)
    participants = extract_participants(comments_info)
    print(build_network(participants, "fabio"))