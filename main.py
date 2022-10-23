
from bs4 import BeautifulSoup
import requests
import re
import json
from summarizer import *

REDUCTION=0.2

search=str(input())

session=requests.Session()
url="https://en.wikipedia.org/w/api.php"

PARAMS_titles={
    "action":"query",
    "list":"search",
    "srsearch":search,
    "format":"json"
}

title_results=session.get(url=url,params=PARAMS_titles)
title_results=title_results.json()

titles=title_results['query']['search']
print("Choose the exact search term: ")

for i in range(len(titles)):
    print(f"    {i}) {titles[i]['title']}")

title_index=int(input())

title=titles[title_index]['title']



PARAMS = {
    "action": "query",
    "prop":"extracts",
    "explaintext":1,
    "namespace": "0",
    "titles": title,
    "format": "json",
    "exintro":""
}


result=session.get(url=url,params=PARAMS)
print(title)
print(result)

content=result.json()

content=content['query']['pages']

ind=list(content)[0]

content=str(content[ind]['extract'].encode('utf-8'))

with open("output.txt",mode="w") as file:
    file.write(content)

#print(type(punctuation))
#content=re.sub("[.!?\\(\\n)-]","",content)

sent_tokens=to_sent_tokens(content)
word_freqs=create_freq_table(content)
normalize_freq(word_freqs)
sent_score=sent_scores(sent_tokens,word_freqs)

summary=summarize(sent_tokens,sent_score,REDUCTION)


if (len(summary)!=0):
    print(summary)
else:
    print(content)

print(f"Original_size: {len(content.split(' '))} Summarized:{len(summary.split(' '))}")

with open("summary.txt",mode="w") as file:
    file.write(summary)
















#_________________________________________
#content=requests.get(url).text
#soup=BeautifulSoup(content,features="html.parser")
#soup=soup.find('div',class_='')
#f=open(f'svg.txt','w')
#f.write(str(soup.find('svg')))
