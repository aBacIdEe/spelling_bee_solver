import json

# creates potential sets from cleanWordList

setsToWords = {}
for line in open('cleanWordList.txt'):
    word = line.strip()
    sets = ''.join(sorted(list(set(list(word)))))
    if sets in setsToWords.keys() and len(word) >= 4:
        setsToWords[sets].append(word)
    elif len(sets) >= 2 and len(sets) <= 7 and len(word) >= 4:
        setsToWords[sets] = [word]

with open('result.json', 'w') as fp:
    json.dump(setsToWords, fp)


