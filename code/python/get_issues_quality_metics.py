import ast
from xml.etree.ElementTree import tostring
from github import Github
import requests
import os

from network_extraction_from_issue_comment import newoutputfile, get_ower_repo_list

from get_issue_lastnumber import get_issue_lastnumber

Auth_token = os.getenv('GITHUB_TOKEN', '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')
IR = Github(Auth_token)



# get all issues and keep necessary information
# note that only keep the issue 'title', 'state' 'created_at', 'closed_at' and 'labels name' information
# you can get these data before, the reason why I get them again is that I forget informations to count quality.
def get_issues_quality(owner, repo):
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
    outputfilename = repo + "_issue"
    outputfile = newoutputfile(outputfilename, "issue_to_quality")
    issue = []
    # page_no = 1200
    lastnumber = get_issue_lastnumber()
    # lastnumber = [124003, 57866, 42477, 39093, 25199, 35968, 20810, 20129, 18374, 21594,
    #               12857, 14125, 13705, 14916, 11870, 17406, 14760, 9188, 12076, 9991, 31165,
    #               8894, 6553, 7803, 11191, 14540, 6088, 8629, 8937, 8015, 4990, 21581, 10376,
    #               12157, 6701, 7022, 6707, 6693, 7807, 6979, 5002, 9931, 11717, 5319, 7052,
    #               4354, 5371, 4801, 4607, 5153, 4608, 6424, 7199, 53072, 3795, 13542, 4969,
    #               3634, 4806, 11187, 4549, 5157, 3716, 6667, 5011, 2112, 2946, 5110, 2481,
    #               2190, 2878, 3015, 2573, 3077, 1824, 1876, 2950, 2756, 3294, 4297, 3063,
    #               2225, 4981, 4526, 5002, 3200, 2830, 4436, 3583, 1738, 1880, 1472, 1450,
    #               1751, 7889, 4375, 1501, 2221, 2190, 2205, 1759, 1695, 1663, 2474, 2638,
    #               4607, 1827, 2715, 6261, 1268, 2254, 1207, 5742, 2183, 1286, 1971, 1998,
    #               1007, 1527, 1449, 3861, 1854, 1683, 2049, 1086, 2080, 1801, 1096, 3132,
    #               1089, 1970, 1347, 1744, 1439, 1230, 2679, 872, 1773, 1137, 4312, 2334,
    #               1048, 2666, 968, 1075, 931, 949, 1529, 2883, 681, 782, 923, 957, 1260,
    #               1185, 2725, 1294, 1463, 1151, 917, 5159, 2326, 887, 756, 825, 680, 729,
    #               813, 1238, 936, 816, 437, 594, 1249, 644, 10566, 486, 865, 752, 598, 829,
    #               880, 1185, 875, 903, 1085, 1273, 361, 285, 354, 482, 1176, 929, 456, 226,
    #               735, 349, 379, 1815, 1422]
    for page_no in range(1, total_pages):
        params_local = {
            "state": "closed",
            "per_page": 100,
            "page": page_no
        }
        print(page_no)
        response = requests.get(query_url, headers=headers, params=params_local)
        json_data_per_page = response.json()
        for j in range(0, len(json_data_per_page)):
            if 'pull' not in json_data_per_page[j]['html_url']:
                # json_data_per_page_cleaned.append(json_data_per_page[j])
                # print([json_data_per_page[j]['number'],json_data_per_page[j]['comments_url']])
                if (json_data_per_page[j]['number'] <= lastnumber[i]):
                    # beacuse the issue will update, we need delete some data and save the data below the last number
                    if (json_data_per_page[j]["labels"]):
                        item = {"issuenumber": json_data_per_page[j]['number'], "title": json_data_per_page[j]["title"],
                                "state": json_data_per_page[j]["state"],
                                "created_at": json_data_per_page[j]["created_at"],
                                "closed_at": json_data_per_page[j]["closed_at"],
                                "labels": {"name": json_data_per_page[j]["labels"][0]["name"]}}
                        with open(outputfile, 'a+', encoding='utf-8') as f:
                            f.write("%s\n" % item)
                    else:
                        item = {"issuenumber": json_data_per_page[j]['number'], "title": json_data_per_page[j]["title"],
                                "state": json_data_per_page[j]["state"],
                                "created_at": json_data_per_page[j]["created_at"],
                                "closed_at": json_data_per_page[j]["closed_at"],
                                "labels": json_data_per_page[j]["labels"]}
                        with open(outputfile, 'a+', encoding='utf-8') as f:
                            f.write("%s\n" % item)

###########################################################################################################################################################################################################################################################
# {'issuenumber': 1075, 'title': "Tag queries are performed even though I'm not calling / using the tags", 'state': 'closed', 'created_at': '2022-01-19T16:22:39Z', 'closed_at': '2022-01-19T18:19:48Z', 'labels': []}
# {'issuenumber': 1070, 'title': 'Cant find version 9 on ruby gems', 'state': 'closed', 'created_at': '2022-01-04T22:07:21Z', 'closed_at': '2022-01-04T22:13:02Z', 'labels': []}
# {'issuenumber': 1062, 'title': "Can't find 9.0 on rubygems, 8.1 not support Rails 7.0.0.alpha2, but 5.0.0 installs ok and migrations passed", 'state': 'closed', 'created_at': '2021-11-20T21:21:21Z', 'closed_at': '2022-01-06T00:55:48Z', 'labels': []}
# {'issuenumber': 1057, 'title': 'Easier access to all tags for a Class: any drawback on `class Tagging < ApplicationRecord` ?', 'state': 'closed', 'created_at': '2021-10-26T14:14:11Z', 'closed_at': '2021-10-26T15:05:35Z', 'labels': []}
# {'issuenumber': 1050, 'title': "I don't know how to uninstall", 'state': 'closed', 'created_at': '2021-10-06T07:57:28Z', 'closed_at': '2022-01-16T23:29:28Z', 'labels': []}
###########################################################################################################################################################################################################################################################

if __name__ == "__main__":
    owers = get_ower_repo_list("owers")
    repos = get_ower_repo_list("repos")
    # print(owers)
    # print(repos)
    print(owers[0])
    print(repos[0])
    for i in range(0, 200):
        get_issues_quality(owers[i], repos[i])
# test("Homebrew", "homebrew-cask")
# issue_quality = []
# path_2 = "../data/issue_to_quality/homebrew-cask_issue"
# with open(path_2, 'r+', encoding='utf-8') as f:
#     for line in f:s
#         issue_quality_list = ast.literal_eval(line)
#         issue_quality.append(issue_quality_list)
# print(issue_quality[0]["title"])