import ast
import csv

from network_extraction_from_issue_comment import newoutputfile, get_ower_repo_list

#Author: Zhijie Wan
from python.calculatenetworkproperty import rewrite_data_to_csv

repos = get_ower_repo_list("repos")

def get_data(filename):
    data = []
    path = "../data/" + filename
    with open(path, 'r+', encoding='utf-8') as f:
        for line in f:
            data_list = ast.literal_eval(line)
            data.append(data_list)
    return data

def transformonthlydata():
    QP = []
    NewB = []
    BFR = []
    NewC = []
    BCT = []

    new_bugs_num = get_data("_qualitydata/new_bugs_num")
    fix_bugs_time = get_data("_qualitydata/avg_fix_bugs_time")
    fix_bugs_num = get_data("_qualitydata/fix_bugs_num")
    # avg_issue_closed_time_cost = get_data("_qualitydata/avg_close_issue_time_cost")
    # issue_closed_num = get_data("_qualitydata/close_issue_num")
    new_commits_num = get_data("_qualitydata/new_commits_num")
    monthes = get_data("_qualitydata/repo_monthes")
    # print(monthes[0])


    for i in range(0, 197):
        sum_new_bug_num = 0
        sum_fix_bug_num = 0
        sum_new_commits_num = 0
        sum_fix_bug_time = 0

        months_new_nug_num = new_bugs_num[i][repos[i]]
        months_fix_bug_num = fix_bugs_num[i][repos[i]]
        months_new_commits_num = new_commits_num[i][repos[i]]
        months_fix_bug_time = fix_bugs_time[i][repos[i]]

        # print(months_new_nug_num['201203'])

        for month in monthes[i]:
            # print(month)
            sum_new_bug_num = sum_new_bug_num + months_new_nug_num[month]
            sum_fix_bug_num = sum_fix_bug_num + months_fix_bug_num[month]
            sum_new_commits_num = sum_new_commits_num + months_new_commits_num[month]
            sum_fix_bug_time = sum_fix_bug_time + months_fix_bug_time[month]
        # for i in range(0, 36):
        #     # print([monthes[i]])
        #     sum_new_bug_num = sum_new_bug_num + months_new_nug_num[monthes[i]]
        #     sum_fix_bug_num = sum_fix_bug_num + months_fix_bug_num[monthes[i]]
        #     sum_new_commits_num = sum_new_commits_num + months_new_commits_num[monthes[i]]
        #     sum_fix_bug_time = sum_fix_bug_time + months_fix_bug_time[monthes[i]]

        avg_new_bug_num = sum_new_bug_num / 36
        avg_fix_bug_num = sum_fix_bug_num / 36
        avg_new_commits_num = sum_new_commits_num / 36
        avg_fix_bug_time = sum_fix_bug_time / 36

        NewB.append(avg_new_bug_num)
        BFR.append(avg_fix_bug_num / avg_new_bug_num)
        NewC.append(avg_new_commits_num)
        BCT.append(avg_fix_bug_time)

        QP.append(NewB)
        QP.append(BFR)
        QP.append(NewC)
        QP.append(BCT)
    return QP


def main():
    QP = transformonthlydata()
    rewrite_data_to_csv("NewC", QP[2])
    rewrite_data_to_csv("BCT", QP[3])
    rewrite_data_to_csv("NewB", QP[0])
    rewrite_data_to_csv("BFR", QP[1])

if __name__ == "__main__":
    main()