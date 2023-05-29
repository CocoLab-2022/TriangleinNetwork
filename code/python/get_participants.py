import ast
import os

from python.network_extraction_from_issue_comment import extract_participants, get_ower_repo_list, newoutputfile

#Author: Zhijie Wan

def get_participants(filename):
    comments_info = []
    path = "../data/_commentdata_36monthes/" + filename + "_comments_36monthes"
    with open(path, 'r+', encoding='utf-8') as f:
        for line in f:
            comments_info_list = ast.literal_eval(line)
            comments_info.append(comments_info_list)
    participants = extract_participants(comments_info)
    outputfilename = filename + "_participants"
    outpufile = newoutputfile(outputfilename, "_participantsdata")
    with open(outpufile, 'a+', encoding='utf-8') as f:
        for item in participants:
            f.write("%s\n" % item)


if __name__ == "__main__":
    repos = get_ower_repo_list("repos")
    # get_participants('fabio')
    # print(repos)
    for i in range(0, 200):
        get_participants(repos[i])
        print("已完成第%d个" % i)