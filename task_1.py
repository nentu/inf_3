f = open("original.yml", 'r', encoding="utf-8").readlines()

def if_need_comma(i: int, dict: dict) -> int:
    return int(i != list(dict.keys())[-1])

def print_branch(dic: dict, layer: int, if_comma:int, f):
    for i in dic.keys():
        if type(dic[i]) == str:
            sting = "   "*(layer+1) + f'"{i}": {dic[i]}' + \
                    "," * if_need_comma(i, dic)
            f.write(sting+'\n')
        else:
            sting = "   "*(layer+1)+f'"{i}":'+'{'
            f.write(sting+'\n')
            print_branch(dic[i], layer + 1, if_need_comma(i, dic), f)

    sting = "   " * (layer) +'}' + ','*if_comma
    f.write(sting + '\n')


def print_dict(main: dict, file_name: str) -> None:
    f = open(file_name, 'w', encoding='utf-8')
    f.write('{\n')
    print_branch(main, 0, 0, f)
    f.close()

def get_level(s: str) -> int:
    ans = 0
    for i in s:
        if i==' ':
            ans+=1
        else:
            break
    return ans//2

def ch_values(s: str) -> str:
    if s[0]!= '"':
        s = '"' + s
    if s[-1]!='"':
        s+='"'
    return s

if __name__ == "__main__":
    main = dict()
    for i in f:
        layer = get_level(i)
        i = i.replace('\n', '')
        i = i.strip()
        if i == "":
            continue
        if ':' == i[-1]:
            i = i[:-1]

            t = main
            for _ in range(layer):
                t = t[list(t.keys())[-1]]

            t[i] = dict()
        else:
            key, value = i.split(": ")

            value = ch_values(value)

            t = main
            for _ in range(layer):
                t = t[list(t.keys())[-1]]

            t[key] = value
    print_dict(main, "task_1.json")

