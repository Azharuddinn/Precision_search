from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    borders = ['General:title','Website']
    placeholder = ['Exact','Related:nytimes.com']
    explanation = ['title','website']
    return render(request, "precise/index.html", {"borders": borders, "placeholder": placeholder, "explanation":explanation})


def data(request):
    
    if request.method == "POST":
        title = request.POST["title"] 
        phrase = request.POST["phrase"]
        website = request.POST["website"]
        file = request.POST["file"]
        location = request.POST["location"]
        
        if title != '':
            return HttpResponseRedirect('https://www.google.com/search?as_q='+str(title)+'&as_epq=&as_oq=&as_eq=&as_nlo=&as_nhi=&lr=&cr=&as_qdr=all&as_sitesearch='+str(website)+'&as_occt='+str(location)+'&safe=images&as_filetype='+str(file)+'&tbs=')
               
        if phrase != '':
            return HttpResponseRedirect('https://www.google.com/search?as_q=&as_epq='+str(phrase)+'&as_oq=&as_eq=&as_nlo=&as_nhi=&lr=&cr=&as_qdr=all&as_sitesearch='+str(website)+'&as_occt='+str(location)+'&safe=images&as_filetype='+str(file)+'&tbs=')

        if phrase == '' and title == '':
            return HttpResponseRedirect('https://www.google.com/doodles')