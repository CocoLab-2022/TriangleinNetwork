import ast
import os
from datetime import datetime

from python.network_extraction_from_issue_comment import get_ower_repo_list, newoutputfile

repos = get_ower_repo_list("repos")
GITHUB_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


def get_min_month(repo, file, filename, dataindex):
    lists = []
    path = "../data/"+ file + "/" + repo + filename
    with open(path, 'r+', encoding='utf-8') as f:
        for line in f:
            list = ast.literal_eval(line)
            lists.append(list)
    if dataindex == "issue":
        min = datetime.strptime(lists[0]["created_at"], GITHUB_TIME_FORMAT)
        for i in range(0, len(lists)):
            created_at = datetime.strptime(lists[i]["created_at"], GITHUB_TIME_FORMAT)
            if min > created_at:
                min = created_at
    elif dataindex == "comment":
        min = datetime.strptime(lists[0][4], GITHUB_TIME_FORMAT)
        for i in range(0, len(lists)):
            created_at = datetime.strptime(lists[i][4], GITHUB_TIME_FORMAT)
            if min > created_at:
                min = created_at
    elif dataindex == "commit":
        min = datetime.strptime(lists[0]['commit']['committer']['date'], GITHUB_TIME_FORMAT)
        for i in range(0, len(lists)):
            created_at = datetime.strptime(lists[i]['commit']['committer']['date'], GITHUB_TIME_FORMAT)
            if min > created_at:
                min = created_at
    return min

startTime =[]
for i in range(0, 197):
    start_time = get_min_month(repos[i], "issue_to_quality", "_issue", "issue")
    # print(repos[i], start_time)
    startTime.append(start_time)

def transCommentDataTo36Monthes():
    for i in range(0,200):
        comments = []
        path = "../data/issuedata/" + repos[i] + "_issue_comment"
        starttime = startTime[i]
        with open(path, 'r+', encoding='utf-8') as f:
            for line in f:
                comments_list = ast.literal_eval(line)
                comment_time = comments_list[4]
                endtime = datetime(int(comment_time[0:4]), int(comment_time[5:7]), int(comment_time[8:10]))
                monthes = (endtime.year - starttime.year) * 12 + endtime.month - starttime.month
                if monthes in range(0,36):
                    comments.append(comments_list)
        outputfilename = repos[i] + "_comments_36monthes"
        outputfile = newoutputfile(outputfilename, "_commentdata_36monthes")
        with open(outputfile, 'a+', encoding='utf-8') as f:
            for item in comments:
                f.write("%s\n" % item)

def transIssueDataTo36Monthes():
    for i in range(0,200):
        issues = []
        path = "../data/issue_to_quality/" + repos[i] + "_issue"
        start_time = get_min_month(repos[i], "issue_to_quality", "_issue", "issue")
        print(repos[i], start_time)
        with open(path, 'r+', encoding='utf-8') as f:
            for line in f:
                issues_list = ast.literal_eval(line)
                create_time = issues_list['created_at']
                end_time = datetime(int(create_time[0:4]), int(create_time[5:7]), int(create_time[8:10]))
                monthes = (end_time.year - start_time.year) * 12 + end_time.month - start_time.month
                if monthes in range(0,36):
                #     print(monthes)
                    issues.append(issues_list)
        outputfilename = repos[i] + "_issues_36monthes"
        outputfile = newoutputfile(outputfilename, "_issuedata_36monthes")
        with open(outputfile, 'a+', encoding='utf-8') as f:
            for item in issues:
                f.write("%s\n" % item)

def transIssueData_contain_colosed_time_To36Monthes():
    for i in range(0,197):
        issues = []
        path = "../data/issue_to_quality/" + repos[i] + "_issue"
        start_time = get_min_month(repos[i], "issue_to_quality", "_issue", "issue")
        print(repos[i], start_time)
        with open(path, 'r+', encoding='utf-8') as f:
            for line in f:
                issues_list = ast.literal_eval(line)
                create_time = issues_list['created_at']
                # closed_time = issues_list['closed_at']
                end_time_created = datetime(int(create_time[0:4]), int(create_time[5:7]), int(create_time[8:10]))
                monthes_created = (end_time_created.year - start_time.year) * 12 + end_time_created.month - start_time.month
                # end_time_closed = datetime(int(closed_time[0:4]), int(closed_time[5:7]), int(closed_time[8:10]))
                # monthes_closed = (end_time_closed.year - start_time.year) * 12 + end_time_closed.month - start_time.month
                if monthes_created in range(0, 36):
                #     print(monthes)
                    issues.append(issues_list)
                # elif monthes_closed in range(0,36):
                #     print("有了")
                #     issues.append(issues_list)
        outputfilename = repos[i] + "_issues_36monthes"
        outputfile = newoutputfile(outputfilename, "_issuedata_36monthes")
        with open(outputfile, 'a+', encoding='utf-8') as f:
            for item in issues:
                f.write("%s\n" % item)

def transCommitDataTo36Monthes():
    for i in range(0,200):
        commits = []
        path = "../data/commitdata/" + repos[i] + "_commit"
        starttime = startTime[i]
        with open(path, 'r+', encoding='utf-8') as f:
            for line in f:
                commit_list = ast.literal_eval(line)
                commit_date = commit_list['commit']['committer']['date']
                endtime = datetime(int(commit_date[0:4]), int(commit_date[5:7]), int(commit_date[8:10]))
                monthes = (endtime.year - starttime.year) * 12 + endtime.month - starttime.month
                if monthes in range(0,36):
                    commits.append(commit_list)
        outputfilename = repos[i] + "_commits_36monthes"
        outputfile = newoutputfile(outputfilename, "_commitdata_36monthes")
        with open(outputfile, 'a+', encoding='utf-8') as f:
            for item in commits:
                f.write("%s\n" % item)

# def transDataTo36Monthes(dataFileFolder, dataFile, time):
#     for i in range(0,200):
#         lists = []
#         lastline = getLastLine(repos[i], dataFileFolder, dataFile)
#         # start_time = lastline[]
#         path = "/data/" + dataFileFolder + "/" + repos[i] + dataFile
#         with open(path, "r+", encoding='utf-8') as f:
#             f.seek(0, 2)
#             last_line = f.readline()
#             list = ast.literal_eval(last_line)
#             start_time = datetime(int(time[0:4]), int(time[5:7]), int(time[8:10]))
#             end_position = f.tell()
#             while True:
#                 end_position -= 1
#                 f.seek(end_position)
#
#                 if end_position <= 0:
#                     f.seek(0)
#                     break
#                 current_line = f.readline()
#                 list = ast.literal_eval(current_line)
#                 end_time = datetime(int(time[0:4]), int(time[5:7]), int(time[8:10]))
#                 monthes = (end_time.year - start_time.year) * 12 + end_time.month - start_time.month
#                 if monthes in range(0, 36):
#                     lists.append(list)
#
#         outputfilename = repos[i] + + dataFile+ "_36monthes"
#         outputfile = newoutputfile(outputfilename, dataFile + "data_36monthes")
#         with open(outputfile, 'a+', encoding='utf-8') as f:
#             for item in lists:
#                 f.write("%s\n" % item)
#
# def getLastLine(repos, dataFileFolder, dataFile):
#     path = "../data/" + dataFileFolder + "/" + repos + dataFile
#     with open(path, "rb") as f:
#         f.seek(-2, os.SEEK_END)
#         while f.read(1) != b'\n':
#             f.seek(-2, os.SEEK_CUR)
#         last_line = f.readline().decode()
#         lastline = ast.literal_eval(last_line)
#         return lastline

if __name__  == "__main__":
    # print(getLastLine("anki", "issuedata", "_issue_comment"))
    # lists = []
    # lastline = getLastLine("anki", "issuedata", "_issue_comment")
    # start_time = lastline[4]
    # print(start_time)
    # path = "../data/" + "issuedata" + "/" + "anki" + "_issue_comment"
    # with open(path, "rb") as f:
    #     f.seek(0, 2)
    #     last_line = f.readline().decode()
    #     list = ast.literal_eval(last_line)
    #     start_time = datetime(int(list[4][0:4]), int(list[4][5:7]), int(list[4][8:10]))
    #     end_position = f.tell()
    #     while True:
    #         end_position -= 1
    #         f.seek(end_position)
    #
    #         if end_position <= 0:
    #             f.seek(0)
    #             break
    #         current_line = f.readline()
    #         list = ast.literal_eval(current_line)
    #         end_time = datetime(int(list[4][0:4]), int(list[4][5:7]), int(list[4][8:10]))
    #         monthes = (end_time.year - start_time.year) * 12 + end_time.month - start_time.month
    #         if monthes in range(0, 36):
    #             lists.append(list)

    # outputfilename = repos[i] + + "_issue_comment" + "_36monthes"
    # outputfile = newoutputfile(outputfilename, "_issue_comment" + "data_36monthes")
    # with open(outputfile, 'a+', encoding='utf-8') as f:
    #     for item in lists:
    #         f.write("%s\n" % item)

    # outputfilename = "annoy_comments_36monthes"
    # outputfile = newoutputfile(outputfilename, "commentdata_36monthes")
    # with open(outputfile, 'a+', encoding='utf-8') as f:
    #     for item in lists:
    #         f.write("%s\n" % item)
    # lottie - react - native
    # print(repos[183])
    # transCommentDataTo36Monthes()
    # transIssueDataTo36Monthes()
    # transCommitDataTo36Monthes()
    transIssueData_contain_colosed_time_To36Monthes()