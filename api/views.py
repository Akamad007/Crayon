import urllib2
import bs4
from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from api.models import ApiFaviconUrl
from django.contrib import messages


stopValue = 240000
def getFavicon(request,url = "https://linkedin.com"):
    #print soupText    
    faviconRoot = favicon(url)
    
    if "http" in faviconRoot or "www" in faviconRoot or ".com" in faviconRoot or ".net" in faviconRoot:
        pass
    else:
        faviconRoot = url+faviconRoot
    return render(request,"api/api.html",{"faviconUrl":faviconRoot})

def favicon(url):
    
    faviconRoot = searchTag(url,"head link","href","favicon")      
    if faviconRoot is None:
        faviconRoot = searchTag(url,"head link","href","png")
    if faviconRoot is None:
        faviconRoot = searchTag(url,"head meta","content","favicon")
    if faviconRoot is None:
        faviconRoot = searchTag(url,"head meta","content",".ico")
    if faviconRoot is None:        
        faviconRoot = searchTag(url,"head meta","content",".png")
    if faviconRoot is None:
        faviconRoot = searchTag(url,"head link","href",".ico")  
    if faviconRoot is None:
        faviconRoot = searchTag(url,"head link","href","svg")
  
   
   
    return faviconRoot

import os
def uploadFile(request):  
    
    with open(os.path.abspath("crayon/api/top-1m.csv")) as f:
        for line in f:
            
            for value in line.split():            
                num,url =  value.split(",")
                
                if int(num)>stopValue:                
                    break
                elif int(num): 
                      
                    mainUrl = "https://"+url
                    print mainUrl
                    faviconUrl = favicon(mainUrl)  
                    if faviconUrl is None:
                        mainUrl = "http://"+url
                        faviconUrl = favicon(mainUrl)                                                 
                    if faviconUrl:                         
                        if "http" in faviconUrl or "www" in faviconUrl or ".com" in faviconUrl or ".net" in faviconUrl:
                            pass
                        else:
                            mainUrl = "http://www."+url
                            faviconUrl = mainUrl+faviconUrl                       
                        try:                                                      
                            apiFavicon = ApiFaviconUrl.objects.get(base_url__contains = url)
                            apiFavicon.favicon = faviconUrl                            
                        except:                            
                            apiFavicon = ApiFaviconUrl.objects.create(user = request.user,base_url =url,favicon = faviconUrl)
                        apiFavicon.save()
                    else:
                        print "error "
                        print faviconUrl
                        print mainUrl   
    messages.success(request, "Added all images have been added ")
    return HttpResponseRedirect("/home/")

import traceback
def searchTag(url,root,nameField,searchText):
    try:
        soupText = urllib2.urlopen(url,timeout = 2).read()
        soup = bs4.BeautifulSoup(soupText)
        faviconRoot = None
        for favicon in soup.select(root):        
                try:
                    
                    if searchText in favicon[nameField]:
                        
                        faviconRoot = favicon[nameField]
                                                             
                        return faviconRoot 
                except :
                    
                    pass
    except:
        pass
    
    return None      
    