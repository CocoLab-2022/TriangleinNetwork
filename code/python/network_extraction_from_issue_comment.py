import ast
from xml.etree.ElementTree import tostring
from github import Github
import requests
import os
import codecs
import json
from pprint import pprint
import time
from itertools import combinations

# Author: Yi Wang (Oliver)

Auth_token = os.getenv('GITHUB_TOKEN', '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')
Auth_token_0 = os.getenv('GITHUB_TOKEN', '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')
Auth_token_1 = os.getenv('GITHUB_TOKEN', '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')
Auth_token_2 = os.getenv('GITHUB_TOKEN', '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')
Auth_token_3 = os.getenv('GITHUB_TOKEN', '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')
Auth_token_4 = os.getenv('GITHUB_TOKEN', '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')
Auth_token_5 = os.getenv('GITHUB_TOKEN', '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')
IR = Github(Auth_token_1)


# utilitiy for creating new files
def newoutputfile(filename, index_data):
    file_dir = "../data/" + index_data
    if not os.path.isdir(file_dir):
        os.makedirs(file_dir)
    outputfilename = "../data/" + index_data + "/" + filename
    if not os.path.exists(outputfilename):
        with open(outputfilename, 'w', encoding="utf-8") as f:
            f.write("")
    return outputfilename


# get a repo's all contributors
def getprojectcontributors(reponame):
    repo = IR.get_repo(reponame)
    contributors = repo.get_contributors()
    return contributors


# get all issues and keep necessary information
# note that only keep the issue 'number' and 'comment_url' information
# if need, may add other info. e.g., 'user'
# indeed, it is worth to keeping 'comments',
# which specifies how many comments an issue has, then, using it could reduce the no. of reqiests made in the next method.
# I am just too lazy to revise the code.
def get_issues(owner, repo):
    page_no = 1
    query_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    headers = {'Authorization': f'token {Auth_token}'}
    params = {
        "state": "closed",
        "per_page": 100,
        "page": page_no
    }
    response = requests.get(query_url, headers=headers, params=params)
    response.status_code = 200
    total_issues = response.json()[0]['number']
    total_pages = int(total_issues / 100) + 1
    outputfilename = repo + "_issue" + "_cleaned"
    outputfile = newoutputfile(outputfilename, "issuedata")
    comment_url = []
    # page_no = 1200
    for page_no in range(1, total_pages):
        params_local = {
            "state": "closed",
            "per_page": 100,
            "page": page_no
        }
        print(page_no)
        response = requests.get(query_url, headers=headers, params=params_local)
        json_data_per_page = response.json()
        json_data_per_page_cleaned = []
        for j in range(0, len(json_data_per_page)):
            if 'pull' not in json_data_per_page[j]['html_url']:
                # json_data_per_page_cleaned.append(json_data_per_page[j])
                # print([json_data_per_page[j]['number'],json_data_per_page[j]['comments_url']])
                comment_url.append([json_data_per_page[j]['number'], json_data_per_page[j]['comments_url']])
        # with open(outputfile, 'a+', encoding='utf-8') as f:
        #    json.dump(json_data_per_page_cleaned, f, ensure_ascii=False, indent=4)
        page_no = page_no + 1
        time.sleep(1)
    with open(outputfile, 'a+', encoding='utf-8') as f:
        for item in comment_url:
            f.write("%s\n" % item)
    return comment_url


# comment_url = [[6, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/6/comments']]
# repo = "homebrew-cask"
# print(comment_url[len(comment_url)-1])

# get the necessary comment information
# written to the file is not necessary but worth to do
def get_issue_comment_info(comment_url, repo):
    headers = {'Authorization': f'token {Auth_token_0}'}
    outputfilename = repo + "_issue" + "_comment"
    outpufile = newoutputfile(outputfilename, "issuedata")
    for i in range(0, len(comment_url)):
        query_url = comment_url[i][1]
        response = requests.get(query_url, headers=headers)
        json_data_per_query = response.json()
        print(comment_url[i])
        if len(json_data_per_query) == 0:
            pass
        else:
            for j in range(0, len(json_data_per_query)):
                item  = [comment_url[i][0], json_data_per_query[j]['issue_url'], json_data_per_query[j]['user']['login'],
                     json_data_per_query[j]['user']['id'], json_data_per_query[j]['created_at'],
                     json_data_per_query[j]['author_association']]
                with open(outpufile, 'a+', encoding='utf-8') as f:
                    f.write("%s\n" % item)
        # time.sleep(0.8)


'''
#the following list is just for testing the next few methods.
comment_info = [
[18, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/18', 'phinze', 37534, '2012-09-27T22:34:58Z', 'CONTRIBUTOR'],
[18, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/18', 'ghost', 10137, '2012-10-09T20:21:05Z', 'NONE'],
[18, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/18', 'phinze', 37534, '2012-10-09T20:23:05Z', 'CONTRIBUTOR'],
[18, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/18', 'phinze', 37534, '2013-04-28T18:58:58Z', 'CONTRIBUTOR'],
[18, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/18', 'molawson', 180317, '2013-05-06T12:06:38Z', 'CONTRIBUTOR'],
[18, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/18', 'phinze', 37534, '2013-05-06T14:39:51Z', 'CONTRIBUTOR'],
[18, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/18', 'jfsiii', 57655, '2013-05-11T23:10:27Z', 'CONTRIBUTOR'],
[18, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/18', 'phinze', 37534, '2013-05-11T23:45:00Z', 'CONTRIBUTOR'],
[18, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/18', 'jfsiii', 57655, '2013-05-12T00:13:39Z', 'CONTRIBUTOR'],
[18, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/18', 'jfsiii', 57655, '2013-05-12T04:39:20Z', 'CONTRIBUTOR'],
[17, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/17', 'phinze', 37534, '2012-10-13T22:03:08Z', 'CONTRIBUTOR'],
[16, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/16', 'passcod', 155787, '2013-02-18T06:35:50Z', 'CONTRIBUTOR'],
[15, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/15', 'passcod', 155787, '2013-02-18T06:35:58Z', 'CONTRIBUTOR'],
[14, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/14', 'phinze', 37534, '2013-05-12T04:04:06Z', 'CONTRIBUTOR'],
[14, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/14', 'Crazor', 128295, '2013-05-12T13:27:34Z', 'CONTRIBUTOR'],
[14, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/14', 'vitorgalvao', 1699443, '2013-05-13T03:18:56Z', 'MEMBER'],
[14, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/14', 'passcod', 155787, '2013-05-13T06:26:32Z', 'CONTRIBUTOR'],
[14, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/14', 'Crazor', 128295, '2013-05-13T20:23:59Z', 'CONTRIBUTOR'],
[14, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/14', 'phinze', 37534, '2013-05-13T20:44:55Z', 'CONTRIBUTOR'],
[14, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/14', 'Crazor', 128295, '2013-05-14T10:10:59Z', 'CONTRIBUTOR'],
[14, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/14', 'vitorgalvao', 1699443, '2013-05-14T16:25:43Z', 'MEMBER'],
[14, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/14', 'muescha', 184316, '2013-05-14T17:07:09Z', 'CONTRIBUTOR'],
[14, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/14', 'phinze', 37534, '2013-05-14T18:09:29Z', 'CONTRIBUTOR'],
[14, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/14', 'phinze', 37534, '2013-06-15T19:39:13Z', 'CONTRIBUTOR'],
[12, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/12', 'passcod', 155787, '2012-09-24T02:25:51Z', 'CONTRIBUTOR'],
[12, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/12', 'phinze', 37534, '2012-09-24T20:16:50Z', 'CONTRIBUTOR'],
[9, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/9', 'XL64', 1560114, '2012-08-24T09:59:48Z', 'NONE'],
[9, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/9', 'XL64', 1560114, '2012-08-24T10:07:07Z', 'NONE'],
[9, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/9', 'phinze', 37534, '2012-08-24T16:13:26Z', 'CONTRIBUTOR'],
[9, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/9', 'phinze', 37534, '2012-08-26T02:38:07Z', 'CONTRIBUTOR'],
[9, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/9', 'XL64', 1560114, '2012-08-27T06:29:53Z', 'NONE'],
[7, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/7', 'phinze', 37534, '2013-04-12T13:39:04Z', 'CONTRIBUTOR'],
[6, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/6', 'chdiza', 3311113, '2013-05-16T18:32:46Z', 'NONE'],
[6, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/6', 'ShaneDelmore', 4604933, '2013-07-15T22:53:17Z', 'CONTRIBUTOR'],
[6, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/6', 'passcod', 155787, '2013-07-16T15:37:38Z', 'CONTRIBUTOR'],
[6, 'https://api.github.com/repos/Homebrew/homebrew-cask/issues/6', 'passcod', 155787, '2013-08-06T04:46:06Z', 'CONTRIBUTOR']
]
'''


# identify an issue's all participant, form a dict structure, then put into a list
def extract_participants(comment_info):
    participants = []
    i = 0
    while i < len(comment_info):
        issue_index = comment_info[i][0]
        j = 0
        temp_participant = []
        while issue_index == comment_info[i + j][0]:
            temp_participant.append(comment_info[i + j][2])
            j = j + 1
            if i + j == len(comment_info):
                break
        participants.append({'issue': issue_index, 'commentor': temp_participant})
        # print({'issue': issue_index, 'commentor': temp_participant})
        i = i + j
    return participants


# build network, represented in the form: edge, edge count(no of edges)
def build_network(participants, repo):
    edges = []
    network_weightedge = []
    # Change the list to set to remove the duplicated items
    for i in range(0, len(participants)):
        participants[i]['commentor'] = set(participants[i]['commentor'])
        participants[i]['commentor'] = list(participants[i]['commentor'])
        participants[i]['commentor'] = sorted(participants[i]['commentor'])
        if len(participants[i]['commentor']) > 1:
            temp = list(combinations(participants[i]['commentor'], 2))
            for item in temp:
                edges.append(item)
    unique_edges = sorted(list(set(edges)))
    for item in unique_edges:
        edge_count = edges.count(item)
        network_weightedge.append([item, edge_count])
    outputfilename = repo + "_network_weightedge"
    outpufile = newoutputfile(outputfilename, "_networkdata")
    with open(outpufile, 'a+', encoding='utf-8') as f:
        for item in network_weightedge:
            f.write("%s\n" % item)
    return network_weightedge

# get owers' and repos' list from ower_repo_ist, then transfor them to string
def get_ower_repo_list(index):
    with open("../data/ower_repo_list", 'r+', encoding='utf-8') as f:
        owers_list = f.readline()
        repos_list = f.readline()
    # for line in lines:
    #     print(line)
    owers = ast.literal_eval(owers_list)
    repos = ast.literal_eval(repos_list)
    if (index == "owers"):
        return owers
    if (index == "repos"):
        return repos
    # print(owers)
    # print(repos)

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