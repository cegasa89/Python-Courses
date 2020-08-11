import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("press y for yes or n for no: ")
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "n": 
            return("pugger your paw steps on wrong keys.")
        else:
            return("you have entered wrong input please enter just y or n.")
    else:
        print("wrong key")


if __name__ == "__main__":
    word = input("Enter the word that you want to search: ")
    output = translate(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)


