from django.shortcuts import render

import requests
import json

# Create your views here.



def home(request):
    a="https://newsapi.org/v2/top-headlines?country=us&apiKey=d467b7308ddb4df28ed059c6b55f6203"
    r=requests.get(a).json()
    headline=r['articles']
    
    q=[]
    for i in headline:
        q.append(i['urlToImage'])
    img=[]
    for val in q:
        
        '''ifurlToImage is not None'''
        if val != None :
            img.append(val)
    context={
        "image":img
    }
    
        
    return render(request,"news/first.html",context)

def second(request):
    a="https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=d467b7308ddb4df28ed059c6b55f6203"
    r=requests.get(a).json()
    headline=r['articles']
    
    q=[]
    for i in headline:
        q.append(i['urlToImage'])
    img=[]
    for val in q:
        if val != None :
            img.append(val)
    context={
        "image":img
    }
    
    return render(request,"news/second.html",context)

def third(request):
    a="https://newsapi.org/v2/top-headlines?country=de&category=business&apiKey=d467b7308ddb4df28ed059c6b55f6203"
    r=requests.get(a).json()
    headline=r['articles']
    
    q=[]
    for i in headline:
        q.append(i['urlToImage'])
    img=[]
    for val in q:
        if val != None :
            img.append(val)
    context={
        "image":img
    }
    
    return render(request,"news/third.html",context)
#chekc to _ misiing
def fourth(request):
    a="https://newsapi.org/v2/top-headlines?q=trump&apiKey=d467b7308ddb4df28ed059c6b55f6203"
    r=requests.get(a).json()
    headline=r['articles']
    
    q=[]
    for i in headline:
        q.append(i['urlToImage'])
    img=[]
    for val in q:
        if val != None :
            
            img.append(val)
    print(img)
    context={
        "image":img
    }
    
    return render(request,"news/fourth.html",context)
    
