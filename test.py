import json
from difflib import get_close_matches
from difflib import SequenceMatcher
data = json.load(open("data.json"))
#datanew = {"rollno1":"veena","rollno2":"sheena","rollno3":"teena","rollno4":"meena"}
#print(datanew['rollno3'])

def translate(word):
    word = word.lower()
    #print(word)
    if word in data:
        return data[word]
    elif word.title() in data :
        return data[word.title()]
    elif word.upper() in data :
        return data[word.upper()]
    elif len(word)>0:
        result = get_close_matches(word, data.keys(), n=5)
        index =  input("Did you mean any of these %s .Please enter index of the word {Staring from 1.}"%result)
        index = int(index)
        if (index)>len(result):
            return "Sorry , Invalid !!"
        else:
            return data[result[index - 1]]


    else :
        return "word does not exist please recheck!!!"





word = input("Enter word : ")
output = translate(word)

if type(output) == list :
    for val in output:
        print("-> " + val)
else :
    print(output)





