import ast
import csv

from network_extraction_from_issue_comment import newoutputfile, get_ower_repo_list

#Author: Zhijie Wan

def get_data(filename):
    data = []
    path = "../data/" + filename
    with open(path, 'r+', encoding='utf-8') as f:
        for line in f:
            data_list = ast.literal_eval(line)
            data.append(data_list)
    return data

# quality data is disorder
# so we write these quality data to a csv
############################################################################################################
# Project,Time,ID,New_Commits,New_Bugs,Avg_Issue_Resolved_Time,Avg_Bug_Fix_Time,Resolved_Issues,Fixed_Bugs
# homebrew-cask,201204,1,2,0,0,0,0,0
# homebrew-cask,201205,2,0,0,0,0,0,0
############################################################################################################
def write_quality_data_to_csv():
    new_bugs_num = get_data("qualitydata/new_bugs_num")
    avg_fix_bugs_time = get_data("qualitydata/avg_fix_bugs_time")
    fix_bugs_num = get_data("qualitydata/fix_bugs_num")
    avg_issue_closed_time_cost = get_data("qualitydata/avg_issue_closed_time_cost")
    issue_closed_num = get_data("qualitydata/issue_closed_num")
    new_commits_num = get_data("qualitydata/new_commits_num")
    monthes = get_data("qualitydata/repo_monthes")
    repos = get_ower_repo_list("repos")

    outputfilename = "all_data_with_quality_metrics.csv"
    outputfile = newoutputfile(outputfilename, "csvdata")

    header = ['Project', 'Time', 'ID', 'New_Commits', 'New_Bugs', 'Avg_Issue_Resolved_Time', 'Avg_Bug_Fix_Time',
              'Resolved_Issues', 'Fixed_Bugs']
    data = []
    for i in range(200):
        ID = 0
        for j in range(len(monthes[i])):
            ID += 1
            each_data = [repos[i], monthes[i][j], ID, new_commits_num[i][repos[i]][monthes[i][j]], new_bugs_num[i][repos[i]][monthes[i][j]],
                         avg_issue_closed_time_cost[i][repos[i]][monthes[i][j]], avg_fix_bugs_time[i][repos[i]][monthes[i][j]],
                         issue_closed_num[i][repos[i]][monthes[i][j]], fix_bugs_num[i][repos[i]][monthes[i][j]]]
            data.append(each_data)
            # data = each_data
    # print(data)
    with open(outputfile, 'w', encoding='utf-8', newline='') as f:
        # write
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        for row in data:
            writer.writerow(row)

# graph data is also disorder
# so we write these graph data to a csv
############################################################################################################
# Project,triangleCount,quadrangleCount,pentagonCount,stars>3Count,stars>4Count,stars>5Count
# homebrew-cask,20192,46767,104107,1357,1024,797
# Cataclysm-DDA,260644,1508946,6610178,2524,2195,1931
# framework,284811,951442,2817144,9140,7881,6875
############################################################################################################
def write_graph_count_data_to_csv():
    pentagon_count = get_data("count/pentagon_count")
    quadrangle_count = get_data("count/quadrangle_count")
    trangle_count = get_data("count/trangle_count")
    star_3_count = get_data("count/stars_3_count")
    star_4_count = get_data("count/stars_4_count")
    star_5_count = get_data("count/stars_5_count")
    repos = get_ower_repo_list("repos")

    outputfilename = "all_data_with_graph_count_data.csv"
    outputfile = newoutputfile(outputfilename, "csvdata")

    header = ['Project', 'triangleCount', 'quadrangleCount', 'pentagonCount', 'stars>3Count', 'stars>4Count', 'stars>5Count']
    data = []
    for i in range(200):
        each_data = [repos[i], trangle_count[i][repos[i]], quadrangle_count[i][repos[i]], pentagon_count[i][repos[i]],
                     star_3_count[i][repos[i]], star_4_count[i][repos[i]], star_5_count[i][repos[i]]]
        data.append(each_data)

    with open(outputfile, 'w', encoding='utf-8', newline='') as f:
        # write
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        for row in data:
            writer.writerow(row)

def main():
    write_quality_data_to_csv()
    write_graph_count_data_to_csv()

if __name__ == "__main__":
    main()