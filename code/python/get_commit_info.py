import ast
from xml.etree.ElementTree import tostring
from github import Github
import requests
import os

from network_extraction_from_issue_comment import newoutputfile, get_ower_repo_list

#Author: Zhijie Wan

Auth_token = os.getenv('GITHUB_TOKEN', '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')
IR = Github(Auth_token)


# get all issues and keep necessary information
# note that only keep the issue 'title', 'state' 'created_at', 'closed_at' and 'labels name' information
# you can get these data before, the reason why I get them again is that I forget informations to count quality.
def get_commit_info(owner, repo):
    page_no = 1
    query_url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {'Authorization': f'token {Auth_token}'}
    outputfilename = repo + "_commit"
    outputfile = newoutputfile(outputfilename, "commitdata")
    while (True):
        params_local = {
            "until": "2022-06-03T04:49:42Z",
            "per_page": 100,
            "page": page_no
        }
        print(page_no)
        page_no += 1
        response = requests.get(query_url, headers=headers, params=params_local)
        json_data_per_page = response.json()
        # if json_data_per_page is null, break the loop
        if (json_data_per_page == []): break
        for j in range(0, len(json_data_per_page)):
            item = {"commit": {"committer": {"date": json_data_per_page[j]["commit"]["committer"]["date"]}}}
            with open(outputfile, 'a+', encoding='utf-8') as f:
                f.write("%s\n" % item)
    print(repo + "成功了")

############################################################################################################
# {'commit': {'committer': {'date': '2022-04-29T09:58:42Z'}}}
# {'commit': {'committer': {'date': '2022-04-26T09:28:34Z'}}}
# {'commit': {'committer': {'date': '2022-04-26T09:27:37Z'}}}
# {'commit': {'committer': {'date': '2022-04-26T09:27:17Z'}}}
############################################################################################################

if __name__ == "__main__":
    owers = get_ower_repo_list("owers")
    repos = get_ower_repo_list("repos")
    # print(owers)
    # print(repos)
    print(owers[0])
    print(repos[0])
    for i in range(0, 200):
        get_commit_info(owers[i], repos[i])


# commit = []
# path_2 = "../data/commitdata/homebrew-cask_commit"
# with open(path_2, 'r+', encoding='utf-8') as f:
#     for line in f:
#         commit_list = ast.literal_eval(line)
#         commit.append(commit_list)
# print(commit[0]["commit"]["committer"]["date"])