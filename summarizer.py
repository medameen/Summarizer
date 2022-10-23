import nltk
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from heapq import nlargest 

stop_words=stopwords.words('english')
punctuation=punctuation+'\n'

def summarize(sent_token,sent_score,REDUCTION):
    length=int(len(sent_token)*REDUCTION)
    summary=nlargest(length,sent_score,key=sent_score.get)
    final=[_ for _ in summary]
    summary=' '.join(final)
    return summary

def to_sent_tokens(content):
    return sent_tokenize(content)

def sent_scores(sent_tokens,word_freqs):
    sent_score={}
    for _ in sent_tokens:
        sentence=_.split(' ')
        for word in sentence:
            if word.lower() in word_freqs.keys():
                if _ not in sent_score.keys():
                    sent_score[_]=word_freqs[word.lower()]
                else:
                    sent_score[_]+=word_freqs[word.lower()]
    return sent_score

def create_freq_table(content):
    tokens=word_tokenize(content)
    word_freqs={}
    for word in tokens:
        if word.lower() not in stop_words:
            if word.lower() not in punctuation:
                if word not in word_freqs.keys():
                    word_freqs[word]=1
                else:
                    word_freqs[word]+=1
    return word_freqs


def normalize_freq(word_freqs):
    MAX_FREQ=max(word_freqs.values())
    for _ in word_freqs.keys():
        word_freqs[_]=word_freqs[_]/MAX_FREQ