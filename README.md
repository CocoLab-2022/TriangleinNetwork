# TriangleinNetwork

This is the repository for the study of triangles in developer networks, the effect of the number of triangles on project quality.

- [Get owners and repositories](#Get owners and repositories)
  - [Get 200 random number](#Get 200 random number)
  - [Get 200 repositories from 2000 repositories](#Get 200 repositories from 2000 repositories)
- [Get All Issues](#Get All Issues)
- [Get All Comments](#Get All Comments)
- [Build Network](#Build Network)
- [Get Triangle Count](#Get Triangle Count)

# Get owners and repositories

We have 2000 repositories on Github, and we need to extract 200 for analysis from them.

## Get 200 random number

We have a csv file containing 2000 repositories and take a stratified sample of 200 repositories out of 2000.

```python
# get 200 random repos from 2000 repos
def get_random():
    list = []
    for i in range(200):
        m = random.randint(2 + 10 * i, 11 + 10 * i)
        list.append(m)
    print(list)
    return list
```

the random list is below:

list = [3, 16, 27, 33, 48, 55, 63, 77, 88, 93, 110, 113, 126, 141, 146, 161, 171, 174, 188, 199, 202, 221, 226, 239,
        249, 259, 271, 280, 282, 297, 309, 313, 329, 338, 345, 356, 365, 372, 382, 394, 403, 418, 425, 441, 444,
        456, 468, 473, 488, 492, 506, 520, 525, 541, 550, 558, 569, 576, 582, 600, 602, 620, 631, 637, 643, 657,
        662, 675, 690, 701, 705, 715, 729, 739, 743, 753, 763, 772, 790, 796, 808, 820, 828, 835, 848, 852, 862,
        872, 885, 893, 906, 916, 926, 935, 944, 954, 967, 974, 983, 999, 1006, 1016, 1031, 1038, 1047, 1055, 		 	    1069, 1078, 1088, 1100, 1106, 1116, 1130, 1134, 1143, 1158, 1163, 1176, 1189, 1199, 1205, 1221, 1223, 		1237, 1247, 1254, 1268, 1279, 1289, 1298, 1308, 1315, 1329, 1335, 1342, 1352, 1365, 1377, 1384, 1399, 		1411, 1414, 1426, 1437, 1446, 1452, 1470, 1474, 1491, 1493, 1510, 1512, 1524, 1541, 1542, 1555, 1569, 		1577, 1582, 1592, 1605, 1615, 1629, 1641, 1648, 1661, 1663, 1681, 1685, 1701, 1710, 1719, 1731, 1737, 		1748, 1760, 1770, 1775, 1789, 1792, 1810, 1819, 1827, 1840, 1842, 1857, 1863, 1872, 1890, 1901, 1907, 		1913, 1924, 1932, 1945, 1956, 1962, 1978, 1989, 1993]

## Get 200 repositories from 2000 repositories

After getting 200 random number, we need to index to the corresponding repository link in the csv file by the obtained list and get the specific strings. Then, write this data to a file, ower_repo_list.

```python
# get repos and owers from the link in csv
def tranfor_list():
    data = pd.read_csv(r'../data/2000_sample.csv')
    path = data[['path']]
    # print(path)
    path = np.array(path)
    # print(path)
    # strArr=[]
    strArr = [''] * 200
    owner_repo = [''] * 200
    owner = [''] * 200
    repo = [''] * 200
    list = get_random()
    # print(list)
    # print(len(list))
    for i in range(200):
        strArr[i] = path[list[i] - 2]
    # print(strArr[0][0])
    # strArr=np.array(strArr)
    for j in range(200):
        owner_repo[j] = strArr[j][0].replace('https://github.com/', '')
        owner[j] = owner_repo[j].split("/")[0]
        repo[j] = owner_repo[j].split("/")[1]
    # owner_repo=np.array(owner_repo)
    outputfilename = "ower_repo_list"
    outpufile = newoutputfile(outputfilename)
    with open(outpufile, 'w+', encoding='utf-8') as f:
        f.write(str(owner))
        f.write("\n"+str(repo))
    print(owner)
    print(repo)
```

owners:

['Homebrew', 'CleverRaven', 'laravel', 'istio', 'bitcoin', 'sourcegraph', 'ArduPilot', 'radareorg', 'openssl', 'numpy', 'chef', ...]

repositories:

['homebrew-cask', 'Cataclysm-DDA', 'framework', 'istio', 'bitcoin', 'sourcegraph', 'ardupilot', 'radare2', 'openssl', 'numpy', 'chef', ...]

# Get All Issues

We split into two steps, first get the issues and then get the comments through issues, we will explain why we do this later.

First, we get a set of sample data according to the URL https://docs.github.com/rest/overview/resources-in-the-rest-api#rate-limiting given by the official website of github.

Uncleaned issue:

{
        "html_url": "https://github.com/Homebrew/homebrew-cask/pull/8#issuecomment-5058283",
        "issue_url": "https://api.github.com/repos/Homebrew/homebrew-cask/issues/8",
        "id": 5058283,
        "node_id": "MDEyOklzc3VlQ29tbWVudDUwNTgyODM=",
        "user": {
            "login": "phinze",
            "id": 37534,
            "node_id": "MDQ6VXNlcjM3NTM0",
            "avatar_url": "https://avatars.githubusercontent.com/u/37534?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/phinze",
            "html_url": "https://github.com/phinze",
            "followers_url": "https://api.github.com/users/phinze/followers",
            "following_url": "https://api.github.com/users/phinze/following{/other_user}",
            "gists_url": "https://api.github.com/users/phinze/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/phinze/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/phinze/subscriptions",
            "organizations_url": "https://api.github.com/users/phinze/orgs",
            "repos_url": "https://api.github.com/users/phinze/repos",
            "events_url": "https://api.github.com/users/phinze/events{/privacy}",
            "received_events_url": "https://api.github.com/users/phinze/received_events",
            "type": "User",
            "site_admin": false
        },
        "created_at": "2012-04-10T22:49:36Z",
        "updated_at": "2012-04-10T22:49:36Z",
        "author_association": "CONTRIBUTOR",
        "body": ":thumbsup:\n",
        "reactions": {
            "url": "https://api.github.com/repos/Homebrew/homebrew-cask/issues/comments/5058283/reactions",
            "total_count": 0,
            "+1": 0,
            "-1": 0,
            "laugh": 0,
            "hooray": 0,
            "confused": 0,
            "heart": 0,
            "rocket": 0,
            "eyes": 0
        },
        "performed_via_github_app": null

}

As you can see, this set of data has too much redundant data, and we need to clean the data.

We delete the data of type "pull"and keep only the number of the issue and comment_url.

```python
# get all issues and keep necessary information
# note that only keep the issue 'number' and 'comment_url' information
# if need, may add other info. e.g., 'user'
# indeed, it is worth to keeping 'comments',
# which specifies how many comments an issue has, then, using it could reduce the no. of reqiests made in the next method.
def get_issues(owner, repo):
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
    outputfilename = repo + "_issue" + "_cleaned"
    outputfile = newoutputfile(outputfilename, "issuedata")
    comment_url = []
    # page_no = 1200
    for page_no in range(1, total_pages):
        params_local = {
            "state": "closed",
            "per_page": 100,
            "page": page_no
        }
        print(page_no)
        response = requests.get(query_url, headers=headers, params=params_local)
        json_data_per_page = response.json()
        json_data_per_page_cleaned = []
        for j in range(0, len(json_data_per_page)):
            if 'pull' not in json_data_per_page[j]['html_url']:
                # json_data_per_page_cleaned.append(json_data_per_page[j])
                # print([json_data_per_page[j]['number'],json_data_per_page[j]['comments_url']])
                comment_url.append([json_data_per_page[j]['number'], json_data_per_page[j]['comments_url']])
        # with open(outputfile, 'a+', encoding='utf-8') as f:
        #    json.dump(json_data_per_page_cleaned, f, ensure_ascii=False, indent=4)
        page_no = page_no + 1
        time.sleep(1)
    with open(outputfile, 'a+', encoding='utf-8') as f:
        for item in comment_url:
            f.write("%s\n" % item)
    return comment_url
```

issues:

[1075, 'https://api.github.com/repos/mbleigh/acts-as-taggable-on/issues/1075/comments']
[1070, 'https://api.github.com/repos/mbleigh/acts-as-taggable-on/issues/1070/comments']

...

# Get All Comments

Now explain why we need to get issues and comments separately.

The main purpose of this study is to get the comments, there are two ways to get them, one is to get the comments directly, and the other is to get the issues first, and then get the comments.
Each github repository has a lot of comments, and there are many issues of type "full", which are not needed, so first propose the type "full" issues, and then get the comments according to issues.
In addition, the api interface provided by github is called up to 5000 times per hour, so if we get the comments directly, we will generate a lot of unnecessary data, which will affect the acquisition of correct data.

Because the number of comments is too much, running a period of time will be disconnected, so here used 7 github personal token (get github data need token password). When a token fails, it can be replaced with the next token, or several programs can be run at the same time.

Similarly, the acquired data needs to be cleaned and remove  the redundant data.

```python
# get the necessary comment information
# written to the file is not necessary but worth to do
def get_issue_comment_info(comment_url, repo):
    headers = {'Authorization': f'token {Auth_token_0}'}
    outputfilename = repo + "_issue" + "_comment"
    outpufile = newoutputfile(outputfilename, "issuedata")
    for i in range(0, len(comment_url)):
        query_url = comment_url[i][1]
        response = requests.get(query_url, headers=headers)
        json_data_per_query = response.json()
        print(comment_url[i])
        if len(json_data_per_query) == 0:
            pass
        else:
            for j in range(0, len(json_data_per_query)):
                item  = [comment_url[i][0], json_data_per_query[j]['issue_url'], json_data_per_query[j]['user']['login'],
                     json_data_per_query[j]['user']['id'], json_data_per_query[j]['created_at'],
                     json_data_per_query[j]['author_association']]
                with open(outpufile, 'a+', encoding='utf-8') as f:
                    f.write("%s\n" % item)
        # time.sleep(0.8)
```

comments:

[1075, 'https://api.github.com/repos/mbleigh/acts-as-taggable-on/issues/1075', 'silva96', 4019924, '2022-01-19T17:38:40Z', 'NONE']
[1070, 'https://api.github.com/repos/mbleigh/acts-as-taggable-on/issues/1070', 'brobles82', 2970237, '2022-01-04T22:12:55Z', 'NONE']

...

# Build Network

After getting the comments, we start building the network.

First, read the comments file and get all the people who participated in the comments for each issue.

```python
# identify an issue's all participant, form a dict structure, then put into a list
def extract_participants(comment_info):
    participants = []
    i = 0
    while i < len(comment_info):
        issue_index = comment_info[i][0]
        j = 0
        temp_participant = []
        while issue_index == comment_info[i + j][0]:
            temp_participant.append(comment_info[i + j][2])
            j = j + 1
            if i + j == len(comment_info):
                break
        participants.append({'issue': issue_index, 'commentor': temp_participant})
        # print({'issue': issue_index, 'commentor': temp_participant})
        i = i + j
    return participants
```

participants:

{'issue': 1075, 'commentor': ['silva96']}
{'issue': 1070, 'commentor': ['brobles82']}
{'issue': 1062, 'commentor': ['SeanLF', 'seuros', 'tclaus', 'seuros', 'mjansing', 'oamike', 'seuros']}

...

The members of every two comments of an issue are connected into an edge and if this edge also exists in other issues, then let the weight add one.

for example: [(node1, node2), weight]

```python
# build network, represented in the form: edge, edge count(no of edges)
def build_network(participants, repo):
    edges = []
    network_weightedge = []
    # Change the list to set to remove the duplicated items
    for i in range(0, len(participants)):
        participants[i]['commentor'] = set(participants[i]['commentor'])
        participants[i]['commentor'] = list(participants[i]['commentor'])
        participants[i]['commentor'] = sorted(participants[i]['commentor'])
        if len(participants[i]['commentor']) > 1:
            temp = list(combinations(participants[i]['commentor'], 2))
            for item in temp:
                edges.append(item)
    unique_edges = sorted(list(set(edges)))
    for item in unique_edges:
        edge_count = edges.count(item)
        network_weightedge.append([item, edge_count])
    outputfilename = repo + "_network_weightedge"
    outpufile = newoutputfile(outputfilename, "networkdata")
    with open(outpufile, 'a+', encoding='utf-8') as f:
        for item in network_weightedge:
            f.write("%s\n" % item)
    return network_weightedge
```

network:

...

[('Yardboy', 'jontebol'), 1]
[('YavorIvanov', 'artemk'), 3]
[('YavorIvanov', 'bnferguson'), 1]
[('YavorIvanov', 'boddhisattva'), 1]

...

# Get Triangle Count

We get it through the existing python package networkx. By adding the constructed graph to networkx, call the function sum(nx.triangles(G).values()) // 3.

First, get nodes from participants. Specially, it need to de-duplication.

```python
# get nodes from participants
# need to de-duplication
def get_nodes(participants):
    nodes = []
    for i in range(0, len(participants)):
        for j in range(0, len(participants[i]['commentor'])):
            nodes.append(participants[i]['commentor'][j])
            # print(participants[i]['commentor'][j])
        nodes = list(set(nodes))
        nodes = sorted(nodes)
    # print(nodes)
    print(len(nodes))
    return nodes
```

The constructed network graph cannot call networkx functions yet, so you need to add the constructed graph to networkx.

```python
# The constructed network graph cannot call networkx functions yet, so you need to add the constructed graph to networkx
def build_graph_by_networkx(filename):
    network_weightedge = []
    path_1 = "../data/networkdata/" + filename + "_network_weightedge"
    with open(path_1, 'r+', encoding='utf-8') as f:
        for line in f:
            network_weightedge_list = ast.literal_eval(line)
            network_weightedge.append(network_weightedge_list)

    participants_info = []
    path_2 = "../data/participantsdata/" + filename + "_participants"
    with open(path_2, 'r+', encoding='utf-8') as f:
        for line in f:
            participants_info_list = ast.literal_eval(line)
            participants_info.append(participants_info_list)
    # print(participants)
    # build graph
    G = nx.Graph()
    # add nodes
    G.add_nodes_from(get_nodes(participants_info))
    # add weight
    e = network_weightedge
    # e = [(1, 2, 6), (2, 3, 2), (1, 3, 1), (3, 4, 7), (4, 5, 9), (5, 6, 3), (4, 6, 3)]
    for k in e:
        G.add_edge(k[0][0], k[0][1], weight=k[1])
    return G
```

Finally, we use sum(nx.triangles(build_graph_by_networkx(repos[i])).values()) // 3 to get triangle count for each network and then write them to file.

```python
owers = get_ower_repo_list("owers")
repos = get_ower_repo_list("repos")
# print(owers)
# print(repos)
outputfilename = "trangle_count"
outpufile = newoutputfile(outputfilename, "tranglecount")
# print(nx.triangles(build_graph_by_networkx("homebrew-cask")))
for i in range(0, 200):
    # print(nx.triangles(build_graph_by_networkx(repos[i])))
    # print({repos[i]: sum(nx.triangles(build_graph_by_networkx(repos[i])).values()) // 3})
    count = {repos[i]: sum(nx.triangles(build_graph_by_networkx(repos[i])).values()) // 3}
    print(count)
    with open(outpufile, 'a+', encoding='utf-8') as f:
        f.write("%s\n" % count)
```

triangle count:

{'homebrew-cask': 20192}
{'Cataclysm-DDA': 260644}
{'framework': 284811}
{'istio': 166046}
{'bitcoin': 55972}
{'sourcegraph': 18238}
{'ardupilot': 38070}

...
