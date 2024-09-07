import json

with open('tree.json') as json_file:
    data = json.load(json_file)
    raw_query = input("Enter 7 letters with first letter being required: ").strip()
    special_letter = raw_query[0]
    query = ''.join(sorted(list(raw_query)))
    if query in data.keys():
        subkeys = data[query]
        with open('result.json') as result_file:
            results = json.load(result_file)
            words = set()
            for key in subkeys:
                words.update(results[key])

        final_words = sorted([word for word in words if special_letter in word])

        print("Here's the valid words:")
        for word in final_words:
            print(word)

    else:
        print("none found")