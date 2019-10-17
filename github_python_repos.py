import requests
import json


def retr_itemkeyvalues(key_name, fileout=False):
    keyvaluelist = []  # for storing the values of provide key
    # for numbering keyvalue list
    for data in git_starred_py_dict['items']:
        # storing key value in a variable and appending to the list
        # print(type(data))
        # print(type(data[key_name]))
        value_str = data[key_name]
        keyvaluelist.append(value_str)

    # write in file
    if fileout:

        with open(str(key_name + '.txt'), 'w+') as outfile:
            file_num = 0
            for i in keyvaluelist:
                try:
                    outfile.write(f"{file_num}. {str(i)} \n")
                except:
                    outfile.write(f"{file_num}. BLANK BLANK \n")
                file_num += 1
    return keyvaluelist


git_starred_py_apirequrl = 'https://api.github.com/search/repositories?q=language:python&sort=s'

v3_header = {'Accept': 'application/vnd.github.v3+json'}

# request api
apireq = requests.get(git_starred_py_apirequrl, headers=v3_header)

print(f"Status Code: {apireq.status_code}")

# retrieve info from json
git_starred_py_dict = apireq.json()

# process results
v = retr_itemkeyvalues('name', fileout=True)
# for i in v:
#     print(i)
