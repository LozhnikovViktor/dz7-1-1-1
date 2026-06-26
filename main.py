from collections import defaultdict


def group_words_by_length(words):


    groups = defaultdict(list)


    for word in words:
        groups[len(word)].append(word)


    return dict(groups)



words = ["apple", "bat", "car", "dog", "elephant", "fish"]
result = group_words_by_length(words)
print(result)