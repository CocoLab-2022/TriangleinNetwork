import ast
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta
import pandas as pd

from network_extraction_from_issue_comment import get_ower_repo_list, newoutputfile

# Author: Zhijie Wan

GITHUB_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

# get a repo's min create time and max closed time to get open time of a repo
def get_min_and_max_month(repo):
    issue_quality = []
    path = "../data/issue_to_quality/" + repo + "_issue"
    with open(path, 'r+', encoding='utf-8') as f:
        for line in f:
            issue_quality_list = ast.literal_eval(line)
            issue_quality.append(issue_quality_list)
    min = dt.strptime(issue_quality[0]["created_at"], GITHUB_TIME_FORMAT)
    max = dt.strptime(issue_quality[0]["closed_at"], GITHUB_TIME_FORMAT)
    for i in range(0, len(issue_quality)):
        if issue_quality[i]["closed_at"]:
            created_at = dt.strptime(issue_quality[i]["created_at"], GITHUB_TIME_FORMAT)
            closed_at = dt.strptime(issue_quality[i]["closed_at"], GITHUB_TIME_FORMAT)
            if max < closed_at:
                max = closed_at
            if min > created_at:
                min = created_at
    # temp = dt.strptime(temp, "%Y%m%dT%H:%M:%SZ")
    min_and_max = [min, max]
    # print(min)
    # print(max)
    # print(max-min)
    return min_and_max

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

# get month's count of a repo's building time
# we can gain every repo's monthes[month_count]
def get_repos_monthes(repo):
    min_and_max = get_min_and_max_month(repo)
    min_time = change_date_to_YYMM(min_and_max[0])
    max_time = change_date_to_YYMM(min_and_max[1])
    month_count = get_month(max_time, min_time)
    monthes = [''] * month_count
    for i in range(month_count):
        index = min_and_max[0] + relativedelta(months=+i+1)
        temp = change_date_to_YYMM(index)
        # print(temp)
        monthes[i] = temp
    outputfilename = "repo_monthes"
    outputfile = newoutputfile(outputfilename, "qualitydata")
    with open(outputfile, 'a+', encoding='utf-8') as f:
        f.write("%s\n" % monthes)
    print(monthes)

# get_repos_monthes(get_min_and_max_month("chi"))
# get_min_and_max_month("chi")

change_date_to_YYMM(get_min_and_max_month("chi")[0])
if __name__ == "__main__":
    repos = get_ower_repo_list("repos")
    # print(owers)
    # print(repos)
    print(repos[0])
    for i in range(0, 200):
        get_repos_monthes(repos[i])