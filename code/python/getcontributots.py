'''
coding: utf-8
@author: WanZhijie
@create: 2023/5/22 21:53
'''

import ast
import os

import requests
from github import Github

from python.network_extraction_from_issue_comment import get_ower_repo_list, newoutputfile

# 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
# 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
# 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
Auth_token = os.getenv('GITHUB_TOKEN', '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')
IR = Github(Auth_token)

GITHUB_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

owners = get_ower_repo_list("owers")
repos = get_ower_repo_list("repos")

def get_contributors(owner, repo):
    query_url_by_id = f"https://api.github.com/repos/" + owner + "/" + repo + "/contributors"
    headers = {'Authorization': f'token {Auth_token}'}

    response = requests.get(query_url_by_id, headers=headers)
    if response.status_code == 200:
        contributors = response.json()
        for contributor in contributors:
            print(contributor['login'], contributor['id'])
            get_contributer_info_by_id(repo, str(contributor['id']))
            # if 'contributions' in contributor and contributor['contributions'] > 0:
            #     if start_date <= contributor['last'] < end_date:
            #         print(contributor['login'])

def get_contributer_info_by_id(repo, id):
    query_url_by_id = f"https://api.github.com/user/" + id
    headers = {'Authorization': f'token {Auth_token}'}
    outputfilename = repo + "_contributerdata_36monthes"
    outputfile = newoutputfile(outputfilename, "_contributerdata_36monthes")
    response = requests.get(query_url_by_id, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        # registration_time = datetime.strptime(user_data['created_at'], GITHUB_TIME_FORMAT)
        contributer_create_time = [id, user_data['created_at']]
        with open(outputfile, 'a+', encoding='utf-8') as f:
            f.write("%s\n" % contributer_create_time)
    else:
        print(repo, "id error")


if __name__ == "__main__":
    for i in range(0, 50):
        print(i)
        get_contributors(owners[i], repos[i])