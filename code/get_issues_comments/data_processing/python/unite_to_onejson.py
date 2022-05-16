import os
import json

# 获取目标文件夹的路径
filedir = '../data/json/1'
# 获取当前文件夹中的文件名称列表
filenames = os.listdir(filedir)
# 打开当前目录下的result.json文件，如果没有则创建

with open('../data/result_json/result.json', "w", encoding="utf-8") as f0:  # 结果文件
    y = 0
    f0.write('[')
    f0.write('\n')
    for filename in filenames:
        # 文件的个数
        filepath = filedir + '/' + filename
        # 该文件中line有多少行
        print(filepath + "开始访问...")
        with open(filepath, 'r', encoding='utf-8')as fp1:
            y = y + 1
            print(y)
            x = 0
            for line in fp1.readlines():
                x = x + 1
                with open(filepath, 'r', encoding='utf-8')as fp:
                    s = fp.read()
                    js1 = json.loads(json.dumps(eval(s)))  # 是列表
                    js2 = json.dumps(line, ensure_ascii=False)
                    #  print(js2)
                    # s=js2.replace('\n    ','')
                    # print(s)
                    js2.replace("\\n", "\n")
                    js2.replace("\n", "").replace('\r', '')
                    b = eval(js2)  # 处理完数据了
                    if (b == '[' + '\n'):
                        b = ''
                    if(y==101):
                        if (b==']'):
                            f0.write(']')
                    else:
                        if (b == ']'):
                            b = ','
                        if (b == ']' + '\n'):
                            b = ','

                    if (b != '['):
                        if (b != ']'):
                            f0.write(b)
                        # else: f0.write(']')

                    #    print(b)
                    fp.close()

        print(filepath + "加载入文件完成...")

    f0.close()
