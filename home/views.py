
from unittest import skip
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template , Context

def result(request):
    return HttpResponse("This is result page")

from bs4 import BeautifulSoup
import requests
import csv


def flipkart(key, mainData):
    def url_generator(query):
        url="https://www.flipkart.com/search?q="+query.replace(' ','%20')+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        return url
    url=url_generator(key)
    page=requests.get(url)
    soup= BeautifulSoup(page.content,'html.parser')
    lists = soup.find_all('div', class_="_1xHGtK _373qXS")
    try:
        for i in lists:
            title = i.find('a', class_= "IRpwTa").text
            price= i.find('div',class_="_30jeq3").text
            links=i.find('a',class_="_2UzuFa").get('href')
            image=i.find('img')
            image['src']=image['src'].replace("/0/0","/580/696")
            mainData[image['src']] = [price, "https://www.flipkart.com"+links,title]
    except:
            return mainData
    return mainData



def flipkart_elec(key, mainData):
    def url(query):
        url="https://www.flipkart.com/search?q="+query.replace(' ','%20')+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        return url
    url=url(key)
    page=requests.get(url)
    soup= BeautifulSoup(page.content,'html.parser')
    lists = soup.find_all('a', class_="_1fQZEK")

    for i in lists:
        title = i.find('div', class_= "_4rR01T").text
        price= i.find('div',class_="_30jeq3 _1_WHN1").text
        image=i.find('img')
        if (i!='#'):
            all_links="https://www.flipkart.com"+i.get('href')
        mainData[image['src']] = [price, all_links,title]
    return mainData

def snapdeal(key, mainData):
    mainData={}
    count=0
    def url(query):
        url="https://www.snapdeal.com/search?keyword="+query.replace(' ','%20')+"&santizedKeyword=shoes&catId=0&categoryId=0&suggested=true&vertical=p&noOfResults=20&searchState=&clickSrc=suggested&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=ALL&url=&utmContent=&dealDetail=&sort=rlvncy"
        return url
    url=url(key)
    page=requests.get(url)
    soup= BeautifulSoup(page.content,'html.parser')
    lists = soup.find_all('div', class_="product-tuple-description")
    if soup.find('span', class_="nnn").text=="Sorry, we've got no results for "f'{key}':
        return mainData
    else:
        for i in lists:
            title = i.find('p', class_= "product-title").text
            price= i.find('span',class_="lfloat product-price").text
            link=i.find('a', class_="dp-widget-link noUdLine").get('href')
            mainData[count] = [price, link, title]
            count+=1
    return (mainData)
  

def bewakoof(key, mainData):
    mainData={}
    def url(query):
        url="https://www.bewakoof.com/search/"+query.replace(' ','%20')+"?ga_q="+query.replace(' ','%20')
        return url

    response = requests.get(url(key))

    soup = BeautifulSoup(response.content, 'html.parser')

    posts = soup.find_all(class_="productCardBox")
    prefix = "https://www.bewakoof.com"


    try:
        for post in posts:
            title = post.find('div', class_="clr-shade4 h3-p-name").get_text().replace('\n', '')
            price = post.select('.discountedPriceText')[0].get_text()
            link = prefix + post.find_parent('a')['href']
            image=post.find('div', class_="productImg").img  
            mainData[image['src']]=[price, link, title] 
        return mainData
    except:
        return mainData
    
def search(request):
    d = request.POST
    term = d['text']
    print(term)
    mainData = {}
    mainData = snapdeal(term, mainData)
    mainData = bewakoof(term, mainData)
    mainData = flipkart(term, mainData)
    mainData = flipkart_elec(term, mainData)
    

    context = {'data': mainData}
    return render(request, "result.html", context)



def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'result.html')
def about(request):
    return render(request, 'about.html')
