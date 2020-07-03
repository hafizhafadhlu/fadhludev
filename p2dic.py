#dictonary
import json

data = json.load(open("dictionary.json"))
from difflib import get_close_matches

def mean(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0:
        print("did you mean %s instead " %get_close_matches(word , data.keys())[0])
        decide = input("y for yes or n for no : ")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n":
            return("didn't find the word")
        else:
            return("can't find the meaning")
    else:
        print("the dictionary can't find the meaning of that word")

word = input("What the meaning of ")
output = mean(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)