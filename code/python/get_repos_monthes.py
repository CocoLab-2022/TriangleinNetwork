import ast
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
import pandas as pd

from network_extraction_from_issue_comment import get_ower_repo_list, newoutputfile

# Author: Zhijie Wan

GITHUB_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

def get_min_month(repo, file, filename, dataindex):
    lists = []
    path = "../data/"+ file + "/" + repo + filename
    with open(path, 'r+', encoding='utf-8') as f:
        for line in f:
            list = ast.literal_eval(line)
            lists.append(list)
    if dataindex == "issue":
        min = dt.strptime(lists[0]["created_at"], GITHUB_TIME_FORMAT)
        for i in range(0, len(lists)):
            created_at = dt.strptime(lists[i]["created_at"], GITHUB_TIME_FORMAT)
            if min > created_at:
                min = created_at
    elif dataindex == "comment":
        min = dt.strptime(lists[0][4], GITHUB_TIME_FORMAT)
        for i in range(0, len(lists)):
            created_at = dt.strptime(lists[i][4], GITHUB_TIME_FORMAT)
            if min > created_at:
                min = created_at
    elif dataindex == "commit":
        min = dt.strptime(lists[0]['commit']['committer']['date'], GITHUB_TIME_FORMAT)
        for i in range(0, len(lists)):
            created_at = dt.strptime(lists[i]['commit']['committer']['date'], GITHUB_TIME_FORMAT)
            if min > created_at:
                min = created_at
    return min

# %Y-%m-%dT%H:%M:%SZ -> YM
# 2015-10-01 11:51:24 -> 201510
def change_date_to_YYMM(date):
    date_index = str(date)
    date_ym = date_index.split(' ')[0]
    year = date_ym.split('-')[0]
    month = date_ym.split('-')[1]
    date_YYMM = year + month
    # date_YYMM = dt.strptime(date_YYMM, "%Y%m")
    # print(date_YYMM)
    return date_YYMM

# we get a repo's min create time and max closed time
# then max_month - min_month = days
# transform days to monthes
def get_month(end_time, start_date):
    v_end_date = end_time
    v_start_date = start_date
    v_year_end = dt.strptime(v_end_date, '%Y%m').year
    v_month_end = dt.strptime(v_end_date, '%Y%m').month
    v_year_start = dt.strptime(v_start_date, '%Y%m').year
    v_month_start = dt.strptime(v_start_date, '%Y%m').month
    interval = (v_year_end - v_year_start) * 12 + (v_month_end - v_month_start)
    print(interval)
    return interval

def add_one_month(start_time):
    v_month = dt.strptime(start_time, '%Y^m').month

# get month's count of a repo's building time
# we can gain every repo's monthes[month_count]
def get_repo_monthes(repo):
    issue_quality = []
    monthes =[]
    min_time = get_min_month(repo, "_issuedata_36monthes", "_issues_36monthes", "issue")
    print(min_time)
    for i in range(0,36):
        index = min_time + relativedelta(months=+i)
        temp = change_date_to_YYMM(index)
        monthes.append(temp)
    print(monthes)
    print(len(monthes))

    # path = "../data/" + "_issuedata_36monthes" + "/" + repo + "_issues_36monthes"
    # with open(path, 'r+', encoding='utf-8') as f:
    #     for line in f:
    #         issue_quality_list = ast.literal_eval(line)
    #         issue_quality.append(issue_quality_list)
    #         monthes.append(change_date_to_YYMM(issue_quality_list["created_at"]))
    # monthes = set(monthes)
    # monthes = sorted(monthes)
    # print(repo, monthes)
    # print(len(monthes))
    outputfilename = "repo_monthes"
    outputfile = newoutputfile(outputfilename, "_qualitydata")
    with open(outputfile, 'a+', encoding='utf-8') as f:
        f.write("%s\n" % monthes)

if __name__ == "__main__":
    repos = get_ower_repo_list("repos")
    # print(owers)
    # print(repos)
    # print(repos[0])
    for i in range(0, 197):
        get_repo_monthes(repos[i])