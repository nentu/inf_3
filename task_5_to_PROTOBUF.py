f = open("original.yml", 'r', encoding="utf-8").readlines()

def if_need_comma(i: int, dict: dict):
    return int(i != list(dict.keys())[-1])

counters = dict()

def get_value_id(layer_number:int):
    if layer_number in counters:
        counters[layer_number]+=1
    else:
        counters[layer_number]=1
    return counters[layer_number]

def get_type(s: str) -> str:
    if s.isdigit():
        return "int32"
    if s.replace('.', "2", 1).isdigit():
        return "float"
    return "string"

def print_branch(dic: dict, layer: int, f):
    global counter
    for i in dic.keys():
        if type(dic[i]) == str:
            counter+=1
            sting = "   "*(layer) + f'required {get_type(dic[i])} {i} = {get_value_id(layer)};' #TODO id of memory and type
            f.write(sting+'\n')
            #print(sting)
        else:
            counter = 0
            sting = "   "*(layer)+f'message {i.upper()} '+'{'
            f.write(sting+'\n')
            #print(sting)
            print_branch(dic[i], layer+1, f)
    if layer!=0:
        sting = "   " * (layer - 1) +'}'
        f.write(sting + '\n')
        #print(sting)


def print_dict(main: dict, file_name: str):
    f = open(file_name, 'w', encoding='utf-8')

    print_branch(main, 0, f)
    f.close()

def get_level(s: str):
    ans = 0
    for i in s:
        if i==' ':
            ans+=1
        else:
            break
    return ans//2


if __name__ == "__main__":
    main = dict()
    for i in f:
        layer = get_level(i)
        i = i.replace('\n', '')
        i = i.strip()
        if ':' == i[-1]:
            i = i[:-1]

            t = main
            for _ in range(layer):
                t = t[list(t.keys())[-1]]

            t[i] = dict()
            ##print(layer, i)
        else:
            key, value = i.split(": ")

            t = main
            for _ in range(layer):
                t = t[list(t.keys())[-1]]

            t[key] = value
    ##print(main)
    print_dict(main, "task_5.proto")
    #print_dict(main, "task_1.json")

