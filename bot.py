import numpy as np
import nltk
import string
import random

f=open('chatbot.txt', 'r', errors= 'ignore')
raw_doc=f.read()
raw_doc=raw_doc.lower()
nltk.download('punk')
nltk.download('wordnet')
sent_tokens = nltk.sent_tokenize(raw_doc)
words_tokens = nltk.word_tokenize(raw_doc)

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(token):
    return[lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def response(user_response):
    robol_response=''
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    TfidfVec = TfidfVec.fit_transform(sent_tokens)
    vals= cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo1_response=robo1_response+"I am sorry! I dont understand you"
        return robo1_response
    else:
        robol_response=robo1_response+sent_tokens[idx]
        return robo1_response

    flag=True
    print("Bot: My name is Cindy. Let's have a conversation! Also, if you want to leave anytime, just type Leave!")
    while(flag==True):
        user_response = input()
        user_response=user_response.lower()
        if(user_response!='leave'):
            if(user_response=='thanks' or user_response=='thank you'):
                flag=False
                print("Bot: You are welcome..")
            else:
                if(greet(user_response)!=None):
                    print("Bot: "+greet(user_response))
                else:
                    sent_tokens.append(user_response)
                    words_tokens=words_tokens+nltk.word_tokenize(user_response)
                    final_words=list(set(words_tokens))
                    print("BOT:" ,end="")
                    print(response(user_response))
                    sent_tokens.remove(user_response)
            else:
                 flag=False
                 print("BOT: Goodbye! Take care <3 ")





