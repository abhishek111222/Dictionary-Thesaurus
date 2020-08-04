def myFun(word, data):
    if word.islower() and word in data:
        return data[word]
    elif word.isupper() and word in data:
        return data[word]
    elif word.istitle() and word in data:
        return data[word]
    elif word.lower() in data:
        return data[word.lower()]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    else:
        a = check_word(word)
        #print(f"After checking the word is : {a}")
        if a == False:
            return "The word is not in the List. Please re-check"
        elif a == "wrong choice":
            print("Unknown Response")
            return
        else:
            a = myFun(a, data)                                                 
    
    return a                             
    
                                   

        #print(f"The main word is : {a} ")
       
        #print(type(a))
        #print(type(data))

def check_word(word):
    
    if(difflib.get_close_matches(word,data, n = 1)):
        main_word = difflib.get_close_matches(word,data, n = 1, cutoff = 0.1)[0]
    else:
        return 0
    #print(type(main_word))
    #print(main_word)

    decision = input(f"Did you mean : {main_word}. Press Y for Yes and N for No : ")
    if decision in ["Y","y"]:
        return main_word
        #print(f"The type of the return is {type(a)}")
    elif decision in ["N", "n"]:
        return 0
    else:
        return "wrong choice"
        
    

import json
import difflib

data = json.load(open("Files/Dictionary+data+inside/data.json"))

word = input("Word you want to find out : ")
#print(f"The type of main word is : {type(word)}")


b = myFun(word,data)

if type(b) == list:
    for i,j in enumerate(b,1):
        print(i,j)

#print(type(a))
#print(data)

