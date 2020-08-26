# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

#replacing input words in email_one with censored word
def censored_words(email_one, input_word):
    censored_word = " "
    for x in range(0, len(input_word)):
        if input_word[x] == " ":
            censored_word = censored_word + " "
        else:
            censored_word = censored_word + "#"
    
    return email_one.replace(input_word, censored_word)

#print(censored_words(email_one, "learning algorithms"))

#censor and replace proprietery item list from email_two
def censor_prop(email_two, input_list):
    for word in input_list:
       censored_word = " "
       for x in range(0, len(word)):
           if word[x] == " ":
               censored_word = censored_word + " "
           else:
               censored_word = censored_word + "%"
    
       email_two = email_two.replace(word, censored_word)
    return email_two
            
    
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
#print(censor_prop(email_two, proprietary_terms))

#to check if words exist in proprietary list and negative words, and censor
def censor_both_prop_neg(input_text, prop_words, neg_words):
    input_text_words = []
    for x in input_text.split(" "): #this returns a list of strings
        x1 = x.split("\n") #further sublist is created and each word is retrieved as a single list
        #print(x1)
        for word in x1:
            input_text_words.append(word) #adding every string from email three to empty list
    
    # to check with proprietary words
    for i in range(0, len(input_text_words)):
        if input_text_words[i] in prop_words:
            word_clean = input_text_words[i]
            #print(word_clean) 
            censored_words = " "
            for i in range(0, len(word_clean)):
                censored_words = censored_words + "@"
                #print(censored_words) #the list of prop words are converted to censored word (@)
            input_text_words[i].replace(word_clean, censored_words) #replacing every word of proprietary in email three with censored word
            print(input_text_words)
    
    #to check if word is in negative words , count accordingly, if count is > 2, assign to a variable
        count = 0
        for i in range(0, len(input_text_words)):
            if (input_text_words[i] in negative_words) == True:
                count +=1
                if count > 2:
                    word_clean = input_text_words[i]
                    for x in punctuation:
                        word_clean = word_clean.strip(x)
                        
                    censored_word = ""
                    for x in range(0,len(word_clean)):
                        censored_word = censored_word + "X"
                    input_text_words[i] = input_text_words[i].replace(word_clean, censored_word)
    return " ".join(input_text_words)

punctuation = [",", "!", "?", ".", "%", "/", "(", ")"]
negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]
#print(censor_both_prop_neg(email_three, proprietary_terms, negative_words))

#to censor all the words from negative words and proprietary words in email four and any words before and after a term from those list.
def censor_bothneg_prop_before_and_after(input_text, censored_list):
    input_text_words = []
    for x in input_text.split():
        x1 = x.split("\n")
        for word in x1:
            input_text_words.append(word)
    for i in range(0, len(input_text_words)):
        checkedword = input_text[i].lower()
        for x in punctuation:
            checkedword = checkedword.strip(x)
        if checkedword in censored_list:
            word_clean = input_text_words[i]
            censored_word = "" 
            for x in punctuation:
                word_clean = word_clean.strip(x)
            for x in range(0, len(word_clean)):
                censored_word = censored_word + '#'
            input_text_words[i] = input_text_words[i].replace(word_clean, censored_word)
            
            word_before = input_text_words[i-1]
            for x in punctuation:
                word_before = word_before.strip(x)
            censored_word_before = censored_word_before + '#'
            
            word_after = input_text_words[i+1]
            for x in punctuation:
                word_after = word_after.strip(x)
            censored_word_after = ""
            for x in range(0, len(word_after)):
                censored_word_after = censored_word_after + "X"
            input_text_words[i+1] = input_text_words[i+1].replace(word_after, censored_word_after)
    return " ".join(input_text_words)

censor_all = proprietary_terms + negative_words


censor_bothneg_prop_before_and_after(email_four, censor_all)



























