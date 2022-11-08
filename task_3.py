import re
from task_1 import print_dict


def get_level(i):
    return len(re.search('^( *)[^ ]', i).group(1))//2

main = dict()

f = open("original.yml", 'r', encoding="utf-8").readlines()

find_key_value = re.compile(r'(.*): (".*")')
find_header = re.compile(r'(.*):')

for i in f:
    layer = get_level(i)
    i = i.replace('\n', '')
    i = i.strip()
    if ':' == i[-1]:
        i = find_header.search(i).group(1)

        t = main
        for _ in range(layer):
            t = t[list(t.keys())[-1]]

        t[i] = dict()
        # print(layer, i)
    else:
        key, value = find_key_value.search(i).groups()

        t = main
        for _ in range(layer):
            t = t[list(t.keys())[-1]]

        t[key] = value
# print(main)
print_dict(main, "task_3.json")

