import ast
from xml.etree.ElementTree import tostring

from dateutil.relativedelta import relativedelta
from github import Github
import requests
import os
from datetime import datetime as dt

from network_extraction_from_issue_comment import newoutputfile, get_ower_repo_list

#Author: Zhijie Wan


Auth_token = os.getenv('GITHUB_TOKEN', '')
IR = Github(Auth_token)
GITHUB_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

def get_repo_start_end_date(repo):
    lists = []
    start_end_time = []
    path = "../data/_commitdata_36monthes/" + repo + "_commits_36monthes"
    with open(path, 'r+', encoding='utf-8') as f:
        for line in f:
            list = ast.literal_eval(line)
            lists.append(list)
    max = dt.strptime(lists[0]['commit']['committer']['date'], GITHUB_TIME_FORMAT)
    min = dt.strptime(lists[0]['commit']['committer']['date'], GITHUB_TIME_FORMAT)
    for i in range(0, len(lists)):
        created_at = dt.strptime(lists[i]['commit']['committer']['date'], GITHUB_TIME_FORMAT)
        if max < created_at:
            max = created_at
        if min > created_at:
            min = created_at
    print(min, max)
    start_end_time.append(min)
    start_end_time.append(max)
    return start_end_time

# get all issues and keep necessary information
# note that only keep the issue 'title', 'state' 'created_at', 'closed_at' and 'labels name' information
# you can get these data before, the reason why I get them again is that I forget informations to count quality.
def get_commit_info(owner, repo, start_time, end_time):
    page_no = 1
    query_url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {'Authorization': f'token {Auth_token}'}
    outputfilename = repo + "_commits_36monthes"
    outputfile = newoutputfile(outputfilename, "_commitdata")
    while (True):
        params_local = {
            "until": end_time,
            "per_page": 100,
            "page": page_no
        }
        response = requests.get(query_url, headers=headers, params=params_local)
        json_data_per_page = response.json()
        # if json_data_per_page is null, break the loop
        if (json_data_per_page == []): break
        for j in range(0, len(json_data_per_page)):
            if json_data_per_page[j]["committer"]:
                item = {"commit": {"committer": {"id": json_data_per_page[j]["committer"]['id'],
                                                 "login": json_data_per_page[j]["committer"]['login'],
                                                 "name": json_data_per_page[j]["commit"]["committer"]['name'],
                                                 "email": json_data_per_page[j]["commit"]["committer"]['email'],
                                                 "date": json_data_per_page[j]["commit"]["committer"]["date"],
                                                 "type": json_data_per_page[j]["committer"]['type']}}}
            else:
                item = {"commit": {"committer": {"id": "None",
                                                 "login": "None",
                                                 "name": json_data_per_page[j]["commit"]["committer"]['name'],
                                                 "email": json_data_per_page[j]["commit"]["committer"]['email'],
                                                 "date": json_data_per_page[j]["commit"]["committer"]["date"],
                                                 "type": "None"}}}
            commit_time = dt.strptime(item['commit']['committer']['date'], GITHUB_TIME_FORMAT)
            if start_time <= commit_time <= end_time:
                with open(outputfile, 'a+', encoding='utf-8') as f:
                    f.write("%s\n" % item)
        print(page_no)
        page_no += 1

############################################################################################################
# {'commit': {'committer': {'login': 'None', 'name': 'twinturbo', 'email': 'me@broadcastingadam.com', 'date': '2012-03-29T17:47:01Z', 'type': 'None'}}}
# {'commit': {'committer': {'login': 'artemk', 'name': 'Artem Kramarenko', 'email': 'me@artemk.name', 'date': '2012-03-29T16:42:59Z', 'type': 'User'}}}
# {'commit': {'committer': {'login': 'None', 'name': 'Chris Hilton', 'email': 'chris.hilton@insphire.com', 'date': '2012-03-29T16:39:12Z', 'type': 'None'}}}
############################################################################################################

if __name__ == "__main__":
    owers = get_ower_repo_list("owers")
    repos = get_ower_repo_list("repos")
    # print(owers)
    # print(repos)
    # print(owers[0])
    # print(repos[0])
    for i in range(0, 50):
        start_end_time = get_repo_start_end_date(repos[i])
        # print(end_time)
        print(repos[i], "开始了")
        get_commit_info(owers[i], repos[i], start_end_time[0], start_end_time[1])
        print("第", i+1, "个", repos[i] + "成功了")
    # print("1")


# commit = []
# path_2 = "../data/commitdata/homebrew-cask_commit"
# with open(path_2, 'r+', encoding='utf-8') as f:
#     for line in f:
#         commit_list = ast.literal_eval(line)
#         commit.append(commit_list)
# print(commit[0]["commit"]["committer"]["date"])