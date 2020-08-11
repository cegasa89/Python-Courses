import json

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]


if __name__ == "__main__":
    word = input("Enter the word that you want to search: ")
    output = translate(word)
    print(output)


