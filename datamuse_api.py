import requests
import json

def meanslike(str1):
    baseurl='https://api.datamuse.com/words?'
    d={'ml':str1,'max':'5'}
    urlh=requests.get(baseurl, params=d)
    print(urlh.url)
    urlh_json=urlh.json()
    return [d['word'] for d in urlh_json]

query_result=meanslike('Voila')
print(query_result)
