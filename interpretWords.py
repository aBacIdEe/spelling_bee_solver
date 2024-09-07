import json

def is_subseq(haystack, needle):
    current_pos = 0
    for c in needle:
        current_pos = haystack.find(c, current_pos) + 1
        if current_pos == 0:
            return False
    return True

# maps 7 letter sequences to lesser ones that are subsequences
tree = {}

# Opening JSON file
with open('result.json') as json_file:
    data = json.load(json_file)
    keys = sorted(data.keys())
    for key in keys:
        if len(key) == 7:
            tree[key] = [key]
    for key in keys:
        if len(key) <= 6:
            for key2 in tree.keys():
                if is_subseq(key2, key):
                    tree[key2].append(key)

with open('tree.json', 'w') as fp:
    json.dump(tree, fp)