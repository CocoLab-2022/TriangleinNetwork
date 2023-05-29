import ast
import csv
import json
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
import numpy as np
import pandas as pd

from network_extraction_from_issue_comment import newoutputfile

from network_extraction_from_issue_comment import get_ower_repo_list

"""
Change these variables
"""
issue_root = "../data/_issuedata_36monthes/"
commit_root = "../data/_commitdata_36monthes/"
######################################################################


GITHUB_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


class Issue:

    def __init__(self,type, state, create_time, closed_time):
        """
        self.create_at = "YYYY-MM-DDTHH:mm:ssZ"， inclusively
        self.closed_at = "YYYY-MM-DDTHH:mm:ssZ", exclusively

        """
        self.type = type # bug, new feature request, enhancement
        self.state = state
        self.create_at = create_time
        self.closed_at = closed_time

    def get_process_time_cost(self):
        """
        :return: elapse seconds
        """
        open_time = dt.strptime(self.create_at, GITHUB_TIME_FORMAT)
        fix_time = dt.strptime(self.closed_at, GITHUB_TIME_FORMAT)
        interval = fix_time - open_time
        return interval.seconds


def computing_monthly_bug_fix_num(projectname, monthes):
    """
    :param projectname:
    :param from_t: "%Y%m"， inclusively
    :param to_t: "%Y%m"， inclusively
    :return:
    """

    path = issue_root + projectname + "_issues_36monthes"

    # new_issue_array = []
    bug_entity_count = {}

    outputfilename = "fix_bugs_num"
    outputfile = newoutputfile(outputfilename, "_qualitydata")
    counter = 0
    while counter < len(monthes):
        # print(from_date)
        # print(counter)
        from_date = dt.strptime(monthes[counter], "%Y%m")
        tmp = from_date + relativedelta(months=+1)
        bug_entities_num = len(query_monthly_bug_fix_timecost(path, from_date, tmp))
        # new_issue_array.append(new_issue_size)
        bug_entity_count[monthes[counter]] = bug_entities_num
        counter = counter + 1

    projectname_fix_bug_num_list = {projectname: bug_entity_count}
    with open(outputfile, 'a+', encoding='utf-8') as f:
        f.write("%s\n" % projectname_fix_bug_num_list)
    # print(new_issue_array)
    return bug_entity_count

def computing_monthly_avg_bug_fix_time_cost(projectname, monthes):
    """
    :param projectname:
    :param from_t: "%Y%m"， inclusively
    :param to_t: "%Y%m"， inclusively
    :return:
    """

    path = issue_root + projectname + "_issues_36monthes"

    # new_issue_array = []
    bug_entity_dict = {}

    outputfilename = "avg_fix_bugs_time"
    outputfile = newoutputfile(outputfilename, "_qualitydata")
    counter = 0
    while counter < len(monthes):
        # print(from_date)
        # print(counter)
        from_date = dt.strptime(monthes[counter], "%Y%m")
        tmp = from_date + relativedelta(months=+1)
        bug_entities = query_monthly_bug_fix_timecost(path, from_date, tmp)
        sum_rt = 0
        if bug_entities:
            for i in range(len(bug_entities)):
                sum_rt = sum_rt + bug_entities[i]
            avg_bug_fix_time = sum_rt / len(bug_entities)
        else:
            avg_bug_fix_time = 0
        # new_issue_array.append(new_issue_size)
        bug_entity_dict[monthes[counter]] = avg_bug_fix_time
        counter = counter + 1

    projectname_fix_bug_time_list = {projectname: bug_entity_dict}
    with open(outputfile, 'a+', encoding='utf-8') as f:
        f.write("%s\n" % projectname_fix_bug_time_list)
    # print(new_issue_array)
    return bug_entity_dict

def computing_monthly_issue_close_num(projectname, monthes):
    """
    :param projectname:
    :param from_t: "%Y%m"， inclusively
    :param to_t: "%Y%m"， inclusively
    :return:
    """

    path = issue_root + projectname + "_issues_36monthes"

    # new_issue_array = []
    issue_closed_entity_count = {}

    outputfilename = "close_issue_num"
    outputfile = newoutputfile(outputfilename, "_qualitydata")
    counter = 0
    while counter < len(monthes):
        # print(from_date)
        # print(counter)
        from_date = dt.strptime(monthes[counter], "%Y%m")
        tmp = from_date + relativedelta(months=+1)
        issue_closed_entities_num = len(query_monthly_issue_close_timecost(path, from_date, tmp))
        # new_issue_array.append(new_issue_size)
        issue_closed_entity_count[monthes[counter]] = issue_closed_entities_num
        counter = counter + 1

    projectname_issue_closed_num_list = {projectname: issue_closed_entity_count}
    with open(outputfile, 'a+', encoding='utf-8') as f:
        f.write("%s\n" % projectname_issue_closed_num_list)
    # print(new_issue_array)
    return issue_closed_entity_count

def computing_monthly_avg_issue_close_time_cost(projectname, monthes):
    """
    :param projectname:
    :param from_t: "%Y%m"， inclusively
    :param to_t: "%Y%m"， inclusively
    :return:
    """

    path = issue_root + projectname + "_issues_36monthes"

    issue_entity_dict = {}

    outputfilename = "avg_close_issue_time"
    outputfile = newoutputfile(outputfilename, "_qualitydata")

    counter = 0
    while counter < len(monthes):
        # print(from_date)
        # print(counter)
        from_date = dt.strptime(monthes[counter], "%Y%m")
        tmp = from_date + relativedelta(months=+1)
        issue_entities = query_monthly_issue_close_timecost(path, from_date, tmp)
        sum_rt = 0
        if issue_entities:
            for i in range(len(issue_entities)):
                sum_rt = sum_rt + issue_entities[i]
            avg_issue_closed_time = sum_rt / len(issue_entities)
        else:
            avg_issue_closed_time = 0
        issue_entity_dict[monthes[counter]] = avg_issue_closed_time
        counter = counter + 1

    with open(outputfile, 'a+', encoding='utf-8') as f:
        f.write("%s\n" % issue_entity_dict)
    # print(new_issue_array)
    return issue_entity_dict

def counting_monthly_new_commit_number(projectname, monthes):
    """
    :param projectname:
    :param from_t: "%Y%m"， inclusively
    :param to_t: "%Y%m"， inclusively
    :return:
    """
    path = commit_root + projectname + "_commits_36monthes"

    # new_commits_array = []
    new_commits_dict = {}
    # from_date = dt.strptime(monthes[0], "%Y%m")
    # to_date = dt.strptime(monthes[-1], "%Y%m")

    outputfilename = "new_commits_num"
    outputfile = newoutputfile(outputfilename, "_qualitydata")
    counter = 0
    # while from_date <= to_date:
    while counter < len(monthes):
        from_date = dt.strptime(monthes[counter], "%Y%m")
        tmp = from_date + relativedelta(months=+1)
        new_commit_size = query_monthly_new_commits(path, from_date, tmp)
        # new_commits_array.append(new_commit_size)
        new_commits_dict[monthes[counter]] = new_commit_size
        counter = counter + 1

    projectname_new_commits_list = {projectname: new_commits_dict}
    with open(outputfile, 'a+', encoding='utf-8') as f:
        f.write("%s\n" % projectname_new_commits_list)

    return new_commits_dict

def computing_monthly_new_bug_num(projectname, monthes):
    """
    :param projectname:
    :param from_t: "%Y%m"， inclusively
    :param to_t: "%Y%m"， inclusively
    :return:
    """

    path = issue_root + projectname + "_issues_36monthes"

    # new_issue_array = []
    new_issues_dict = {}

    # from_date = dt.strptime(monthes[0], "%Y%m")
    # to_date = dt.strptime(monthes[-1], "%Y%m")

    outputfilename = "new_bugs_num"
    outputfile = newoutputfile(outputfilename, "_qualitydata")
    counter = 0
    while counter < len(monthes):
        # print(from_date)
        # print(counter)
        from_date = dt.strptime(monthes[counter], "%Y%m")
        tmp = from_date + relativedelta(months=+1)
        new_bug_size = query_new_bug_num(path, from_date, tmp)
        # new_issue_array.append(new_issue_size)
        new_issues_dict[monthes[counter]] = new_bug_size
        counter += 1
    projectname_new_bug_list = {projectname: new_issues_dict}
    with open(outputfile, 'a+', encoding='utf-8') as f:
        f.write("%s\n" % projectname_new_bug_list)


########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################
########################################################################################################################################################################


def query_monthly_bug_fix_timecost(issue_json_path, from_t, to_t):
    """
        :param issue_json_path
        :param from_t: python date type, "%Y%m"， inclusively
        :param to_t: python date type, "%Y%m"， exclusively
        :return:
    """

    bug_related_keywords = ['defect', 'error', 'bug', 'issue', 'mistake', 'incorrect', 'fault', 'flaw']

    # with open(issue_json_path) as f:
    #     data = json.load(f)

    data = []
    with open(issue_json_path, 'r+', encoding='utf-8') as f:
        for line in f:
            data_list = ast.literal_eval(line)
            data.append(data_list)

    from_date = from_t
    to_date = to_t

    rt = []

    for i in range(0, len(data)):
        # print("processing No. "+str(i+1)+" issue.............")
        issue_item = data[i]

        if issue_item["state"] == "closed" and issue_item["closed_at"]!=None:

            closed_date = issue_item["closed_at"]

            a = dt.strptime(closed_date, GITHUB_TIME_FORMAT)

            flag = False
            if (a >= from_date) and (a < to_date):
                labels = issue_item["labels"]

                for bug_kw in bug_related_keywords:
                    if bug_kw in issue_item["title"]:
                        # rt.append(issue_item["title"])
                        issue = Issue("bug", issue_item["state"], issue_item["created_at"], issue_item["closed_at"]).get_process_time_cost()
                        rt.append(issue)
                        flag = True
                        break

                if flag:
                    continue

                if labels:
                    for bug_kw in bug_related_keywords:
                        if bug_kw in labels["name"].lower():
                            # rt.append(issue_item["title"])
                            issue = Issue("bug", issue_item["state"], issue_item["created_at"], issue_item["closed_at"]).get_process_time_cost()
                            rt.append(issue)
                            flag = True
                            break

                    if flag:
                        break
    return rt

def query_monthly_issue_close_timecost(issue_json_path, from_t, to_t):
    """
        :param issue_json_path
        :param from_t: python date type, "%Y%m"， inclusively
        :param to_t: python date type, "%Y%m"， exclusively
        :return:
    """

    # with open(issue_json_path) as f:
    #     data = json.load(f)

    data = []
    with open(issue_json_path, 'r+', encoding='utf-8') as f:
        for line in f:
            data_list = ast.literal_eval(line)
            data.append(data_list)

    from_date = from_t
    to_date = to_t

    rt = []

    for i in range(0, len(data)):
        # print("processing No. "+str(i+1)+" issue.............")
        issue_item = data[i]

        if issue_item["state"] == "closed" and issue_item["closed_at"]!=None:

            closed_date = issue_item["closed_at"]
            a = dt.strptime(closed_date, GITHUB_TIME_FORMAT)
            if (a >= from_date) and (a < to_date):
                    issue = Issue("issue", issue_item["state"], issue_item["created_at"], issue_item["closed_at"]).get_process_time_cost()
                    rt.append(issue)

    return rt


#
# In the paper:
# Vasilescu, Bogdan, Yue Yu, Huaimin Wang, Premkumar Devanbu, and Vladimir Filkov.
# "Quality and productivity outcomes relating to continuous integration in GitHub."
# In Proceedings of the 2015 10th Joint Meeting on Foundations of Software Engineering, pp. 805-816. ACM, 2015.
#
# Productivity is defined as: the number of pull requests merged per month.
def query_monthly_new_commits(commits_path, from_t, to_t):
    """
       :param owner
       :param repo
       :param from_t: "%m/%d/%y"， exclusively
       :param to_t: "%m/%d/%y"， exclusively
       :return:
       """
    # with open(commits_path) as f:
    #     data = json.load(f)

    data = []
    with open(commits_path, 'r+', encoding='utf-8') as f:
        for line in f:
            data_list = ast.literal_eval(line)
            data.append(data_list)

    # from_date = dt.strptime(from_t, "%m/%Y")
    # to_date = dt.strptime(to_t, "%m/%Y")
    from_date = from_t
    to_date = to_t

    rt = []

    for i in range(0, len(data)):
        # print("processing No. "+str(i+1)+" issue.............")
        commit_item = data[i]
        create_date = commit_item["commit"]["committer"]["date"]
        a = dt.strptime(create_date, GITHUB_TIME_FORMAT)
        if (a > from_date) and (a < to_date):
            rt.append(commit_item)

    return len(rt)


# Quality is defined as: the number of bugs per unit time
# Note these two quotes here:
# "Since tagging is project specific, we started by manually reviewing how project managers used tags to label
# bugs in some highly active GitHub projects (e.g., rails, scipy), and compiled a list of bug-related keywords, i.e.,
# defect, error, bug, issue, mistake, incorrect, fault, and flaw, after lowercasing and Porter stemming. We then searched
# for these stems in issue tags in all projects, and labeled the issue as bug if any of its tags (potentially multiple) contained
# at least one stem."
def query_new_bug_num(issue_path, from_t, to_t):
    """
    :param issue_path
    :param from_t: python date type, "%Y%m"， inclusively
    :param to_t: python date type, "%Y%m"， exclusively
    :return:
    """
    bug_related_keywords = ['defect', 'error', 'bug', 'issue', 'mistake', 'incorrect', 'fault', 'flaw']

    # with open(issue_path) as f:
    #     data = json.load(f)

    data = []
    with open(issue_path, 'r+', encoding='utf-8') as f:
        for line in f:
            data_list = ast.literal_eval(line)
            data.append(data_list)

    # from_date = dt.strptime(from_t, "%m/%Y")
    # to_date = dt.strptime(to_t, "%m/%Y")
    from_date = from_t
    to_date = to_t

    rt = []

    for i in range(0, len(data)):
        # print("processing No. "+str(i+1)+" issue.............")
        issue_item = data[i]
        # print(issue_item)

        create_date = issue_item["created_at"]
        a = dt.strptime(create_date, GITHUB_TIME_FORMAT)

        flag = False
        if (a >= from_date) and (a < to_date):
            labels = issue_item["labels"]
            for bug_kw in bug_related_keywords:
                if bug_kw in issue_item["title"]:
                    rt.append(issue_item["title"])
                    flag = True
                    break

            if flag:
                continue

            if labels:
                for bug_kw in bug_related_keywords:
                    if bug_kw in labels["name"].lower():
                        rt.append(issue_item["title"])
                        flag = True
                        break

                if flag:
                    break
    return len(rt)

def main():
    # from_t = "01/2019"
    # to_t = "02/2019"
    # from_date = dt.strptime(from_t, "%m/%Y")
    # to_date = dt.strptime(to_t, "%m/%Y")


    monthes = []
    path = "../data/_qualitydata/" + "repo_monthes"
    with open(path, 'r+', encoding='utf-8') as f:
        for line in f:
            monthes_list = ast.literal_eval(line)
            monthes.append(monthes_list)

    owers = get_ower_repo_list("owers")
    repos = get_ower_repo_list("repos")
    # print(owers)
    # print(repos)
    print(owers[0])
    print(repos[0])
    for i in range(0, 197):
        # computing_monthly_new_bug_num(repos[i], monthes[i])
        # computing_monthly_avg_bug_fix_time_cost(repos[i], monthes[i])
        # computing_monthly_bug_fix_num(repos[i], monthes[i])
        counting_monthly_new_commit_number(repos[i], monthes[i])
        # computing_monthly_avg_issue_close_time_cost(repos[i], monthes[i])
        # computing_monthly_issue_close_num(repos[i], monthes[i])

if __name__ == "__main__":
    main()