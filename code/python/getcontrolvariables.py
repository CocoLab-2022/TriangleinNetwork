'''
coding: utf-8
@author: WanZhijie
@create: 2023/5/15 22:24
'''
import ast
import json
import os
from datetime import datetime

import requests
from github import Github

from python.calculatenetworkproperty import rewrite_data_to_csv
from python.dataTo36monthes import get_min_month
from python.get_commit_info import get_repo_start_end_date
from python.network_extraction_from_issue_comment import get_ower_repo_list, newoutputfile

Auth_token = os.getenv('GITHUB_TOKEN', '')
IR = Github(Auth_token)
GITHUB_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
repos = get_ower_repo_list("repos")

startTime = []
for i in range(0, 197):
    start_time = get_min_month(repos[i], "issue_to_quality", "_issue", "issue")
    # print(repos[i], start_time)
    startTime.append(start_time)

def get_projectcontributer(repo):
    lists = []
    ID = []
    fullname = []
    path = "../data/_commitdata_36monthes/" + repo + "_commits_36monthes"
    if is_file_empty(path):
        print(repo, "文件为空")
        ID = []
        fullname = []
    else:
        with open(path, 'r+', encoding='utf-8') as f:
            for line in f:
                # print(line)
                list = ast.literal_eval(line)
                if list['commit']['committer']['login'] != "None":
                    ID.append(list['commit']['committer']['id'])

                else:
                    item = [list['commit']['committer']['name'], list['commit']['committer']['date']]
                    fullname.append(item)

    ID = set(ID)
    ID = sorted(ID)
    fullname = delete_same_value(fullname)
    lists.append(ID)
    lists.append(fullname)
    print(repo, len(ID) + len(fullname))
    return lists

def get_experience(repo, project_start_time):
    experience = []
    sum_experience = 0
    count = 0
    path = "../data/_contributerdata_36monthes/" + repo + "_contributerdata_36monthes"
    with open(path, 'r+', encoding='utf-8') as f:
        for line in f:
            list = ast.literal_eval(line)
            menber_created_time = datetime.strptime(list[1], GITHUB_TIME_FORMAT)
            experience.append((project_start_time - menber_created_time).total_seconds()/86400)
    for item in experience:
        if item > 0:
            sum_experience = sum_experience + item
            count = count + 1
    avg_experience = sum_experience / count
    return avg_experience

def delete_same_value(array):
    global key, row
    unique_dict = {}
    for row in array:
        key = row[0]
        # print(row[0])
        if key in unique_dict:
            if row[1] < unique_dict[key][1]:
                unique_dict[key] = row
        if key not in unique_dict:
            unique_dict[key] = row

    unique_array = list(unique_dict.values())
    # print(unique_array)
    return unique_array


# def get_response_data(query_url, auth_token):
#     global data
#     headers = {'Authorization': f'token {auth_token}'}
#     response = requests.get(query_url, headers=headers)
#     if response.status_code == 200:
#         data = response.json()
#     return data

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


def get_contributer_info_by_fullname(repo, fullname, date):
    nameinfo = []
    index = 0
    query_url_by_id = f"https://api.github.com/search/users?q=" + fullname + "created:%3C%3D" + date
    headers = {'Authorization': f'token {Auth_token}'}
    response = requests.get(query_url_by_id, headers=headers)
    if response.status_code == 200:
        user_data = response.json()
        # print(user_data)
        for item in user_data["items"]:
            nameinfo.append(item)
        if len(nameinfo) == 1:
            get_contributer_info_by_id(repo, str(nameinfo[0]['id']))
        elif len(nameinfo) > 1:
            print("相同fullname个数是", len(nameinfo))
            for i in range(len(nameinfo)):
                if developer_repo(str(nameinfo[i]['id']), repo):
                    print("查到了")
                    index = 1
                    get_contributer_info_by_id(repo, str(nameinfo[0]['id']))
                    break
                else:
                    index = 0
            if index == 0:
                print("没查到")
    else:
        print(repo, "fullname error")

def developer_repo(id, repo):
    global repos_data
    query_url = f"https://api.github.com/user/" + id + "/repos"
    headers = {'Authorization': f'token {Auth_token}'}
    response = requests.get(query_url, headers=headers)
    if response.status_code == 200:
        repos_data = response.json()
        # print(repos_data)
    for repodata in repos_data:
        if repodata['name'] == repo:
            print("repo查询了")
            # print(repodata)
            return True

def is_file_empty(file_path):
    return os.stat(file_path).st_size == 0

if __name__ == "__main__":
    # delete_same_value([['a', "2015-02-28T14:21:58Z"],['a', "2014-02-28T14:21:58Z"],['b', "2010-02-28T14:21:58Z"],['d', "2011-02-28T14:21:58Z"]])
    # developer_repo("49682", "homebrew-cask")
    # get_contributer_info_by_fullname("homebrew-cask", "Pierre Bernard", "2015-02-28T14:21:58Z")
    # get_contributer_info_by_id("homebrew-cask", "3359850")
    size = []
    Avg_experience = []
    for i in range(0,197):
        # print("第", i+1, "个")
        # lists = get_projectcontributer(repos[i])
        # projectsize = len(lists[0]) + len(lists[1])
        # size.append(projectsize)
        # # print(list[0])
        # print("id开始了")
        # for j in range(0, len(lists[0])):
        #     get_contributer_info_by_id(repos[i], str(lists[0][j]))
        #     print(j)
        # print("fullname开始了")
        # for k in range(0, len(lists[1])):
        #     print(k)
        #     get_contributer_info_by_fullname(repos[i], lists[1][k][0], lists[1][k][1])

        avg_experience = get_experience(repos[i], startTime[i])
        Avg_experience.append(avg_experience)

    # print(size)
    # rewrite_data_to_csv("size", size)

    print(Avg_experience)
    rewrite_data_to_csv("experience", Avg_experience)
